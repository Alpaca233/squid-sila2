from .microscope_service_base import MicroscopeServiceBase

from unitelabs.cdk import sila
import asyncio


class MicroscopeService(MicroscopeServiceBase):
    """
    Microscope Service
    """
    def __init__(self, microscope: Squid):
        super().__init__()
        self.microscope = microscope