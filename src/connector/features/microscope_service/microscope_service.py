from .microscope_service_base import MicroscopeServiceBase
from ...squid import Squid

from unitelabs.cdk import sila
import asyncio


class MicroscopeService(MicroscopeServiceBase):
    """
    Microscope Service
    """
    def __init__(self, microscope: Squid):
        super().__init__()
        self.microscope = microscope

    async def get_stage_position(self) -> str:
        return self.microscope.attribute

    async def move_to_loading_position(self) -> bool:
        return False

    async def perform_scanning(self) -> bool:
        return False

