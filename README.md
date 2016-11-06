# nb-livereload
Adds `livereload/files`, which can hot-reload `html` files and linked `css`
assets in the Jupyter notebook.

## Using

After [installing](#installing), all of the files in the directory where you
launch `jupyter notebook` will be live-reloadable at, for example:
```
http://localhost:8888/livereload/files/index.html
```

## Uses
Inside a notebook, you can use anything that generates an html file, such as
nbconvert:
```
!jupyter nbconvert ThisNotebook.ipynb --to-html
```
...and (after loading the file in a second tab the first time) immediately
see the result loaded in a second browser pane at:
```
http://localhost:8888/livereload/files/ThisNotebook.html
```

## Installing
```
conda install -c conda-forge livereload notebook
pip install git+https://github.com/bollwybl/nb-livereload#egg=nb-livereload
jupyter serverextension enable --py --sys-prefix nblivereload
jupyter notebook
```

## Developing
```shell
conda env update
source activate nb-livereload
python setup.py develop
jupyter serverextension enable --py --sys-prefix nblivereload
```
