# Flask-Shell

Flask extension to improve shell command for the Flask CLI.

## Features

- Support ipython/bpython

## Requirements

- flask >= 0.11

## Installation

```
pip install flask-shell
```

## Usage

```
> flask shell --help

Usage: flask shell [OPTIONS]

  Runs an interactive Python shell in the context of a given Flask
  application.  The application will populate the default namespace of this
  shell according to it's configuration. This is useful for executing small
  snippets of management code without having to manually configuring the
  application.

Options:
  --ipython / --no-ipython
  --bpython / --no-bpython
  --help                    Show this message and exit.
```
