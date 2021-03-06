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

3. change the database name from ``simple`` to your own name into `dbcli/dbcli/env.py`

## Advanced usage

### Deploy dbcli on a remote server

If you want to deploy an application that rely on dbcli, there is 2 options :

* If you can override the environment variable ``DATABASE_URL``, through a docker-compose.yml file for exemple
* If you can't, you should use a ``.env`` file at the root using the ``.env.tpl`` as base

If you want to change the name of database on dev environnement, change the default value of `dbcli/dbcli/env.py`

### Manage 2 databases or more

You should write a init.sh script that use the following configuration and create one
alembic directory for each configuration.

```bash
export DATABASE_URL="postgresql://postgres:1234@localhost:5432/base1"
export DATABASE_ALEMBIC_PATH="alembic/base1"
dbcli init
dbcli alembic:upgrade

export DATABASE_URL="postgresql://postgres:1234@localhost:5432/base2"
export DATABASE_ALEMBIC_PATH="alembic/base2"
dbcli init
dbcli alembic:upgrade
```

To create the new alembic configuration, copy the existing one in ``dbcli/alembic`` or use ``alembic init``

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
