## blueprint-database-postgresql

![ci](https://github.com/FabienArcellier/blueprint-database-postgresql/workflows/ci/badge.svg)

blueprint which contains the prerequisite to manage a database according
to the pattern of evolutionary database design.

* build the database if it doesn't exists
* apply migration on the database if required

This blueprint could be used to :

* create a web application that depends on a database
* build a database for analytics with metabase as frontend
* ...

The implementation requires :

* ``make``
* ``postgresql``
* ``python3.8``

## Getting started

1. clone this repository

2. remove .git directory

## The latest version

You can find the latest version to ...

```bash
git clone https://github.com/FabienArcellier/blueprint-database-postgresql.git
```

## Usage

You load a local postgresql development database with the following command.

```bash
make up
```

This command will execute the following workflow :

1. load a postgresql instance through ``docker``
2. ensure the database `postgres` exists (or the one configured through the environment variable ``DATABASE_URL``)
3. stop the postgresql
4. load the postgresql instance and keep it running


## Developper guideline

### Add a dependency

Write the dependency in ``setup.py``. As it's the distribution standard for pypi,
I prefer to keep ``setup.py`` as single source of truth.

I encourage avoiding using instruction as ``pipenv install requests`` to register
a new library. You would have to write your dependency in both ``setup.py`` and ``Pipfile``.

### Install development environment

Use make to instanciate a python virtual environment in ./venv and install the
python dependencies.

```bash
make install_requirements_dev
```

### Update release dependencies

Use make to instanciate a python virtual environment in ./venv and freeze
dependencies version on requirement.txt.

```bash
make update_requirements
```

### Activate the python environment

When you setup the requirements, a `venv` directory on python 3 is created.
To activate the venv, you have to execute :

```bash
make activate
```
### Run the automatic tests

```bash
make test
```

### Run the dev environment

```bash
make up
```

## References

* [Heroku Dev Center - The Procfile](https://devcenter.heroku.com/articles/procfile)
* [Honcho: manage Procfile-based applications](https://honcho.readthedocs.io/en/latest/)

## Contributors

* Fabien Arcellier

## License

MIT License

Copyright (c) 2021 Fabien Arcellier

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
