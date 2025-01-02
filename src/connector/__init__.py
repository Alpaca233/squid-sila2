from unitelabs.cdk import Connector

from .features.microscope_service import MicroscopeService
from software.control.microscope import Microscope


async def create_app():
    """Creates the connector application"""
    app = Connector(
        {
            "sila_server": {
                "name": "Squid test",
                "type": "Example",
                "description": "A UniteLabs SiLA Python Server for Squid microscope",
                "version": "0.1.0",
                "vendor_url": "https://www.cephla.com/",
            }
        }
    )

    scope = Microscope(is_simulation=True)
    scope.home_xyz()

    app.register(MicroscopeService(microscope=scope))


    return app
