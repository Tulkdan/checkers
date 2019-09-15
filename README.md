# Checkers

### How to install

First, you need to create a python virtual environment with virtualenv and python 3, must be version 3.6 above
(if you don't know what it is, [you could check it out here](https://docs.python-guide.org/dev/virtualenvs/)).

To create the environmento with python 3, you should run the command (after installed virtualenv):

```
virtualenv venv --python=python3
```

After that, you should be able to activate the virtual environment with the command

```
source venv/bin/active
```

And to exit of the environment

```
deactivate
```

### How to run

After you'd installed and initiated the environment you can simply run the `main.py` file with

```
python main.py
```

### How to play

The board and positions are gonna be represented like this

```
  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
--|---|---|---|---|---|---|---|---|
0 | x |   | x |   | x |   | x |   |
--|---|---|---|---|---|---|---|---|
1 |   | x |   | x |   | x |   | x |
--|---|---|---|---|---|---|---|---|
2 | x |   | x |   | x |   | x |   |
--|---|---|---|---|---|---|---|---|
3 |   |   |   |   |   |   |   |   |
--|---|---|---|---|---|---|---|---|
4 |   |   |   |   |   |   |   |   |
--|---|---|---|---|---|---|---|---|
5 |   | y |   | y |   | y |   | y |
--|---|---|---|---|---|---|---|---|
6 | y |   | y |   | y |   | y |   |
--|---|---|---|---|---|---|---|---|
7 |   | y |   | y |   | y |   | y |
--|---|---|---|---|---|---|---|---|
```