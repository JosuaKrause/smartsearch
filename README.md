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
