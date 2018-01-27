[![Build Status](https://travis-ci.org/DaveTCode/confluence-archiving-python-lib.svg?branch=master)](https://travis-ci.org/DaveTCode/confluence-archiving-python-lib)
[![PyPI version](https://badge.fury.io/py/confluence-archiving.svg)](https://badge.fury.io/py/confluence-archiving)

# Confluence Archiving Python Library

This is a simple wrapper around the REST API which the Confluence Archiving plugin from midori provides.

You can see the documentation on that API [here](http://www.midori-global.com/products/confluence-archiving-plugin/documentation/api)

## Installation

~~~~
pip install confluence-archiving
~~~~

## Usage

```python
from midori.archiving.client import ArchivingClient
with ArchivingClient('http://localhost:8080/confluence', ('user', 'pass')) as client:
    content_status = client.get_page_content_status(1000)

```

## Development and Deployment

See the [Contribution guidelines for this project](CONTRIBUTING.md) for details on how to make changes to this library.

### Testing Locally

For now there are only some basic unit tests included. These can be run using
```
python setup.py test
```