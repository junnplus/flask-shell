# Flask-Shell

Flask extension to improve shell command for the Flask CLI.

## Features

- Support ptipython/ptpython/ipython/bpython

## Requirements

- flask >= 1.0.0

## Installation

To install using pip:
```
pip install flask-shell[ipython]
```

## Usage

```
> export FLASK_APP=happy.py
> flask shell --help

Usage: flask shell [OPTIONS]

  Runs an interactive Python shell in the context of a given Flask
  application.  The application will populate the default namespace of this
  shell according to it's configuration. This is useful for executing small
  snippets of management code without having to manually configuring the
  application.

Options:
  --use-shell [ptipython|ptpython|ipython|bpython|plain]
  --help                    Show this message and exit.
```
