# Connector starter template

The device-template repository contains the device specific code for the driver implementation. Each device driver
starts off as a copy off this template and must be stored in a separate repository in the
[connectors namespace of the UniteLabs GitLab](https://gitlab.com/unitelabs/connectors).

## Quickstart

To get started quickly, you need to install the [UniteLabs Connector Framework](https://gitlab.com/unitelabs/connector-framework).
Make sure the pyproject.toml points to the correct installation folder of your UniteLabs Framework installation.
You can clone, install, and start the project with:

```
$ git clone https://gitlab.com/unitelabs/connector-starter.git <my-connector-name>
$ cd <my-connector-name>
$ poetry install
$ poetry run connector start
```

## Installation

This is a more detailed installation description. If you're starting out from scratch, this is for you.

### Set up Python

[<img src="https://img.shields.io/badge/python-3.9.2-0052FF.svg?logo=LOGO&amp;labelColor=090422">](LINK)
[<img src="https://img.shields.io/badge/pip->22.3.1-0052FF.svg?logo=LOGO&amp;labelColor=090422">](LINK)

The device template requires Python 3.9.2.

#### MacOS

If you already have a system python installation, you can configure an additional python version using pyenv and skip to
the next subsection.
If you don't have a python installation installed on your machine, install python
using [homebrew](https://brew.sh/#install). Homebrew is a package manager for MacOS. You can install python version 3.9.2 by
running the following command in a terminal session:

`$ brew install python@3.9.2`

##### Setup with multiple python versions

Install the python version manager [pyenv](https://github.com/pyenv/pyenv) using homebrew:

```commandline
$ brew install pyenv
```

Add the path where the python versions are installed through pyenv to the PATH environmental variable:

```commandline
$ export PATH="$HOME/.local/bin:$PATH"
$ eval "$(pyenv init -)"
```

Install the python version through pyenv using:

```commandline
$ pyenv install 3.9.2
```

Make the newly installed python version globally available:

```commandline
$ pyenv global 3.9.2
```

#### Windows

Download python from the official [python website](https://www.python.org/downloads/release/python-3108/) or use a
package manager like conda (not recommended). Install the downloaded executable.

#### MacOS / Windows

Check that your environmental variables and aliases are set up correctly with the following commands:

```commandline
$ python --version
Python 3.9.2
```

Which should point to your python 3 executable and return the python version.

Pip is the python package management system. It is installed automatically with python. Make sure "pip"
is pointing to the pip version of your python 3 installation:

```commandline
$ pip --version
pip 22.3.1  (python 3.9)
```

### Set up Poetry

[<img src="https://img.shields.io/badge/poetry->1.3.1-0052FF.svg?logo=LOGO&amp;labelColor=090422">](LINK)

If you run into trouble during the poetry installation process there's a detailed installation note on the official
[poetry website](https://python-poetry.org/docs/).

Install poetry by running the following code in your terminal (MacOS) or command line (Windows):

`$ curl -sSL https://install.python-poetry.org | python3 -`

Check your poetry installation by running:

```commandline
$ poetry --version
Poetry (version 1.3.1)
```

### Clone the repository

Make sure navigate to the same folder in which your _driver_ repository is located. The local _driver_ and the _device
template_ repository must be on the same level. You need to have set up a personal access token to clone your repository
from GitHub. Otherwise, you will get a SSLCertificate Error. Once you have set up a token, store it somewhere safe.
When running the following command, you will be prompted for a password. Paste the token instead.

### Install the device-template package

Navigate to the root folder of your local device-template repository. This folder contains the pyproject.toml in which the virtual
environment is defined.

> **_NOTE:_** If you're using a non-system python version managed by pyenv, poetry must be pointed to this version by using the following command:  
> `$ poetry env use 3.9.2`

Install the environment with:

`$ poetry install`

Make sure the poetry lock is up-to-date by updating it with:

`$ poetry update`

> **_NOTE:_** Poetry installs the _connector-framework_ package dependency as an editable package. If you make changes to the
> _connector-framework_ package, they will be available in this _<my-connector-name>_ project immediately.  
> -> See pyproject.toml  
> unitelabs = { path = "../connector-framework", develop = true }

### Starting a driver

The connector is defined in the _\_\_main\_\_.py_ file in the ./device folder. Features of the connector must be registered
in this file. The start method in the _cli.py_ file in the connector framework starts the application:

`$ poetry run connector start`

## Testing

### Run code tests

There are no tests at the moment.

🧱🚧🏗️ This is still work in progress 🧱🚧🏗️

`$ poetry run pytest`

## Committing your work

🧱🚧🏗️ This is still work in progress 🧱🚧🏗️

### Code formatting

Run a black check to see which files don't comply to the formatting rules.

`$ poetry run black --check .`

You can use black to reformat all files or a selection thereof using either one of the following commands:

```commandline
$ poetry run black
$ poetry run black connector/greeting_provider.py
```

`$ poetry run pylint connector`

### Naming convention

🧱🚧🏗️ This is still work in progress 🧱🚧🏗️
