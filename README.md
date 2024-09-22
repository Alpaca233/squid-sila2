# Microscope SiLA 2 connector

# Quickstart:

To get started quickly, you need to install the [UniteLabs Connector Framework](https://gitlab.com/unitelabs/connector-framework).
Make sure the pyproject.toml points to the correct installation folder of your UniteLabs Framework installation.

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

### Start project

You can clone, install, and start the project with:

``` terminal
$ git clone https://github.com/Alpaca233/sila2_test
$ cd sila2_test
$ poetry install
```

To use the connector, environment variables need to be set. This can be done by adding a .env file in the root directory.
Here are some standard variables that can be used for local testing in the [UniteLabs SiLA Browser](https://gitlab.com/unitelabs/integrations/sila2/sila-browser):

``` .env
SILA_SERVER__NAME="BlueSens"
CLOUD_SERVER_ENDPOINT__ENDPOINT = localhost:5000
CLOUD_SERVER_ENDPOINT__SECURE = True
SILA_SERVER__UUID = <Your generated uuid4>
SILA_SERVER__HOST = 0.0.0.0
SILA_SERVER__PORT = 50001
```
You can generate a uuid4 quickly with this online [generator](https://www.uuidgenerator.net/version4). If you're using 
the server-initiated cloud connectivity, enter the cloud endpoint of your client application.


After setting up the environment, you can start the connector by running

``` terminal
$ poetry run connector start
```
