#BrilliantImagery

A DNG based photo editing package

##TESTING

Install all of the dependencies:
```
$ pip install -r requirements-dev.txt
```

Go to the parent directory of BrilliantImagery and install it by running:
```
$ pip install -e brilliantimagery
```
To run all tests, with a working directory of ```./brilliantimagery/tests```, run pytest:
```
$ pytest
```
##DEVELOPMENT

##DOCS

After making changes to the docs, to update them, assuming `./brilliantiamgery` is the current working directory,
change the working directory to the `docs` folder:
```
$ cd docs
```
And then run clean and make the html docs.
```
& make clean && make html
```
