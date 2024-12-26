import asyncio

from unitelabs.cdk import compose_app

from . import create_app


async def main():
    """Creates and starts the connector application"""
    app = await compose_app(create_app)
    await app.start()


if __name__ == "__main__":
    asyncio.run(main())