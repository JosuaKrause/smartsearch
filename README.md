smartsearch
===========

This repo contains a python based API server that provides various NLP APIs.

## Setup Python

In order to setup python install `python >= 3.10` and `conda`.
Create a new environment and activate it.
Then run:
```
make install
```

For contributing python code run:
```
make pre-commit
```
To set up the python pre-commit hook.

And ensure that all lints pass:
```
make lint-all
```
You can also call individual lints via make. See `make help`.

## Running the server

In order to get the language API to work, create the tables by running:
```
python -m app.system --init-location
```
Or to create tables for all APIs via:
```
python -m app.system --init-db
```

The first time you will get an error that the config file is missing.
It will create a config file for you. Locate it and fill in all correct values.

Once the config file and the tables are created run:
```
make run-api
```
To start the server. The server has an interactive mode. You can type commands
in the terminal. The most useful commands are `quit`, `restart`, and `help`.
