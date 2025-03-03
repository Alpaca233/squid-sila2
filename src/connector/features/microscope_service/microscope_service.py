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
        self.channel_names = {
            '0': 'BF LED matrix full',
            '1': 'DF LED matrix',
            '2': 'BF LED matrix low NA',
            '405': 'Fluorescence 405 nm Ex',
            '488': 'Fluorescence 488 nm Ex',
            '561': 'Fluorescence 561 nm Ex',
            '638': 'Fluorescence 638 nm Ex',
            '730': 'Fluorescence 730 nm Ex',
        }

    async def get_stage_position(self) -> str:
        pos = ','.join([str(self.microscope.get_x()), str(self.microscope.get_y()), str(self.microscope.get_z())])
        return pos

    async def move_to_loading_position(self) -> bool:
        self.microscope.to_loading_position()
        return True

    async def move_to(self, x_mm: float, y_mm: float, z_um: float) -> bool:
        self.microscope.move_to_position(x_mm, y_mm, z_um / 1000)
        return True
    
    async def load_profile(self, profile_name: str) -> bool:
        self.microscope.configurationManager.load_profile(profile_name)
        return True

    async def set_objective(self, objective_name: str) -> bool:
        self.microscope.set_objective(objective_name)
        return True

    async def select_wells_to_scan(self, wellplate_format: str, selection: str, scan_size_mm: float = None, overlap: float = 10) -> bool:
        self.coordinates, self.names = self.microscope.set_coordinates(wellplate_format, selection, scan_size_mm, overlap)
        return True

    async def perform_scanning(self, path: str, experiment_ID: str, z_pos_um: float, channels: str = '0', use_laser_af: bool = True) -> bool:
        channel_list = [self.channel_names[ch.strip()] for ch in channels.split(',')]
        self.microscope.perform_scanning(path, experiment_ID, z_pos_um, channel_list, use_laser_af)
        return True
