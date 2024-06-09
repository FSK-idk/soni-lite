# soni.lite

A simple audio player based on sqlite database.


## instalation

Clone repository to your local folder

```
git clone git@github.com:FSK-idk/soni.git
```

Download required packages from requirements.txt

```
pip install -r requirements.txt
```

Compile `soni/resources/resources.qrc` file

```
pyside6-rcc soni/resources/resources.qrc -o soni/resources/resources_rc.py
```

Launch program
```
python soni/main.py
```

## about

It is a project for my subject at university.

It is only a light version of the application. Using PySide doesn't seem to be a very good option. The project may be continued with a different gui framework.
