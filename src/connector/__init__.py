from unitelabs.cdk import Connector

from .features.microscope_service import MicroscopeService


async def create_app():
    """Creates the connector application"""
    app = Connector(
        {
            "sila_server": {
                "name": "Squid test",
                "type": "Example",
                "description": "A UniteLabs SiLA Python Example Server",
                "version": "0.1.0",
                "vendor_url": "https://unitelabs.io/",
            }
        }
    )

    app.register(MicroscopeService())

    return app
