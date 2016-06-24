# Lab 3 

Lab 3 from university data mining course

### What it does?

It implements KNN classifier for text. It classifies text using KNN algorythm, with TF-IDF used for words indexing

### How to run?

You need [https://github.com/tailhook/vagga](vagga) installed on machine you are running, or instance of `MongoDB` running on machine.

To set up `MongoDB` using `vagga`, just type:
```
    vagga mongo
```
*Note: internet connection is required for first run of vagga*

Otherwise, put into [config.json](config.json), host and port of your MongoDB instance.

After that, you have to set up python virtualenv
```
    virtualenv --clear -p python3.5 .venv
    . .venv/bin/activate
    pip install -r requirements.txt
```
*Note, you will need python3.5 installed on your machine. Otherwise, put version of python you have instead of python3.5. But not python2.7*

Than you type 
```
    ./main.py --data=<path to file you want to process> --config=<path to config, optional>
```

### Files walkthrough

- [docproc.py](docproc.py) - document processing functions
- [index.py](index.py) - indexing functions
- [main.py](main.py) - primary program file
- [config.json](config.json) - config holder
- directories [test](test/) and [doggy](doggy/) - dataset used for testing

