from tornado.web import escape
from notebook.notebookapp import (
    NotebookApp,
    url_path_join as ujoin
)
from livereload.handlers import (
    ForceReloadHandler,
    LiveReloadHandler,
    LiveReloadJSHandler,
    StaticFileHandler,
)
from livereload.watcher import get_watcher_class
from livereload.server import LiveScriptInjector

from jinja2 import Template


PREFIX = 'livereload'

LIVE_SCRIPT_TEMPLATE = Template("""
    <script type="text/javascript">
        ;(function(host){
            document.write(
                '<script src="//' + host + ':{{ port }}' +
                '{{ base_url }}{{ prefix }}' +
                '/livereload.js?port={{ port }}&host=' + host + '">' +
                '</' + 'script>'
            );
        })(window.location.hostname);
        </script>
""")


def load_jupyter_server_extension(nbapp: NotebookApp):
    nbapp.log.info("[nblivereload] ENABLED")
    web_app = nbapp.web_app
    base_url = nbapp.base_url

    restart_delay = 2
    watcher = get_watcher_class()()

    def prefixed(*bits):
        return ujoin(base_url, PREFIX, *bits)

    class ConfiguredTransform(LiveScriptInjector):
        script = escape.utf8(LIVE_SCRIPT_TEMPLATE.render(
            base_url=base_url,
            port=nbapp.port,
            prefix=PREFIX
        ))

        def __init__(self, request):
            self.attempt_transform = request.uri.startswith(prefixed("files"))

        def transform_first_chunk(self, status_code, headers, chunk,
                                  finishing):
            if self.attempt_transform:
                return super(ConfiguredTransform, self).transform_first_chunk(
                    status_code,
                    headers,
                    chunk,
                    finishing)
            return status_code, headers, chunk

    web_app.transforms.append(ConfiguredTransform)

    LiveReloadHandler.watcher = watcher
    LiveReloadHandler.live_css = True

    watcher._changes.append(('__livereload__', restart_delay))
    LiveReloadHandler.start_tasks()

    web_app.add_handlers(".*", [
        (prefixed("?$"), LiveReloadHandler),
        (prefixed("forcereload"), ForceReloadHandler),
        (prefixed("livereload.js"), LiveReloadJSHandler),
        (prefixed("files", "(.*)"), StaticFileHandler, {
            "path": nbapp.notebook_dir,
            "default_filename": "index.html",
        }),
    ])
