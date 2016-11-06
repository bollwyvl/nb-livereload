# coding: utf-8
# flake8: noqa
from ._version import __version__, __version_info__


# Jupyter Extension points
def _jupyter_server_extension_paths():
    return [dict(module="nblivereload.serverextension")]
