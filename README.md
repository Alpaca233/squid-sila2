# Microscope SiLA 2 connector

# Quickstart:

To get started quickly, you need to install the [UniteLabs Connector Framework](https://gitlab.com/unitelabs/connector-framework).
Make sure the pyproject.toml points to the correct installation folder of your UniteLabs Framework installation.
### Install Squid submodule
The repo includes a submodule for the Squid microscope software. After cloning this repo, do

```terminal
git submodule update --init
```

### Set up Poetry

[<img src="https://img.shields.io/badge/poetry->1.3.1-0052FF.svg?logo=LOGO&amp;labelColor=090422">](LINK)

If you run into trouble during the poetry installation process there's a detailed installation note on the official
[poetry website](https://python-poetry.org/docs/).

Install poetry by running the following code in your terminal (MacOS) or command line (Windows):

```terminal
curl -sSL https://install.python-poetry.org | python3 -
```

On Mac, create a .zshrc file in the home folder with the following:

```terminal
export PATH="$HOME/.local/bin:$PATH"
```

Check your poetry installation by running:

```commandline
poetry --version
```

### Start project

The repo includes a submodule for the Squid microscope software. You can clone the project with:

``` terminal
git clone https://github.com/Alpaca233/squid-sila2
git submodule update --init
```
The Squid microscope software will be cloned in `squid_sila2/src/squid` directory. We'll need to move a few folders to `squid_sila2` directory for it to work:

```terminal
cd squid_sila2
mkdir cache
cp -r ./src/squid/software/images .
cp -r "./src/squid/software/drivers and libraries" .
cp -r ./src/squid/software/objective_and_sample_formats .
```
You will also need to copy your microscope configuration file (`configuration*.ini` file), and optionally, the `acquisition_configurations` folder to `squid_sila2` directory if you want to use saved laser autofocus and channel configuration settings (it will be created automatically if not provided). 

After this, run the following to start the project:

``` terminal
poetry install
```

To use the connector, environment variables need to be set. This can be done by adding a .env file in the root directory.
Here are some standard variables that can be used for local testing in the [UniteLabs SiLA Browser](https://gitlab.com/unitelabs/integrations/sila2/sila-browser):

``` .env
SILA_SERVER__NAME="Squid"
CLOUD_SERVER_ENDPOINT__ENDPOINT = localhost:5000
CLOUD_SERVER_ENDPOINT__SECURE = True
SILA_SERVER__UUID = <Your generated uuid4>
SILA_SERVER__HOST = 0.0.0.0
SILA_SERVER__PORT = 50001
```
Change `CLOUD_SERVER_ENDPOINT__ENDPOINT` to your IP address as needed.
You can generate a uuid4 quickly with this online [generator](https://www.uuidgenerator.net/version4). If you're using 
the server-initiated cloud connectivity, enter the cloud endpoint of your client application.


After setting up the environment, you can start the connector by running

``` terminal
poetry run connector start
```
### Test with SiLA Browser
https://gitlab.com/unitelabs/sila2/sila-browser
