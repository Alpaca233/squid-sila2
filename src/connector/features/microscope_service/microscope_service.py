from .microscope_service_base import MicroscopeServiceBase
from software.control.microscope import Microscope
import software.control.utils as utils
import numpy as np
import pandas as pd
import time

from unitelabs.cdk import sila
import asyncio


class MicroscopeService(MicroscopeServiceBase):
    """
    Microscope Service
    """
    def __init__(self, microscope: Microscope):
        super().__init__()
        self.microscope = microscope
        self.coordinates = None
        self.names = None

    async def get_stage_position(self) -> str:
        pos = ','.join([str(self.microscope.get_x()), str(self.microscope.get_y()), str(self.microscope.get_z())])
        return pos

    async def move_to_loading_position(self) -> bool:
        self.microscope.to_loading_position()
        return True

    async def move_to(self, x_mm: float, y_mm: float, z_um: float) -> bool:
        self.microscope.move_to_position(x, y, z_um / 1000)
        return True

    async def select_wells(self, wellplate_format: str, selection: str, scan_size_mm: float = None, overlap: float = 10) -> bool:
        self.coordinates, self.names = self.microscope.get_scan_coordinates_from_selected_wells(wellplate_format, selection, scan_size_mm, overlap)
        return True

    async def perform_scanning(self, path: str, z_pos_um: float, channels: str = '0') -> bool:
        self.microscope.perform_scanning(path, z_pos_um, channels.split(','), self.coordinates, self.names)
        return True
