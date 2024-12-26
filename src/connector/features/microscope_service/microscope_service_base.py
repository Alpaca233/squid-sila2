import abc
import asyncio
from unitelabs.cdk import sila


class MicroscopeServiceBase(sila.Feature, metaclass=abc.ABCMeta):
    """
    Microscope Service
    """

    def __init__(self):
        super().__init__(
            originator="org.silastandard",
            category="examples",
            version="1.0",
            maturity_level="Draft",
        )

    @abc.abstractmethod
    @sila.UnobservableProperty()
    async def get_stage_position(self) -> str:
        """
        Retrieve the position of the stage once.
        .. return: coordinates as a string
        """

#    @abc.abstractmethod
#    @sila.UnobservableProperty()
#    async def get_device_status(self) -> int:
#        """
#        Retrieve the status of the microscope once.
#        .. return: 0: ready; 1: moving to loading postion; 2: scanning
#        """

    @abc.abstractmethod
    @sila.UnobservableCommand()
    @sila.Response(name="Result")
    async def move_to_loading_position(self) -> bool:
        """
        Move stage to loading position.

        .. return:: execution result. True: successful; False: failed
        """

    @abc.abstractmethod
    @sila.UnobservableCommand()
    @sila.Response(name="Result")
    async def select_wells(self, wellplate_format: str, selection: str, scan_size_mm: float = None, overlap: float = 10) -> bool:
        """
        Select wells and generate fov coordinates to scan
        .. parameter:: wellplate_format: a str such as '384 well plate', '96 well plate' or the name of your custom wellplate
                       seletion: a str indicating your selected wells, such as 'A2,B3:B6'
                       scan_size_mm: scan size for one well. If is None, it will be set to a default value based on the wellplate settings
                       overlap: overlap percentage between each fov
        .. return:: execution result. True: successful; False: failed
        """

    @abc.abstractmethod
    @sila.UnobservableCommand()
    @sila.Response(name="Result")
    async def perform_scanning(self, path: str, z_pos_um: float) -> bool:
        """
        Start scanning at with xy coordinates generated previously and a given z position. Save acquired images.
        .. parameter:: path: path to save images
                       z_pos_um: z position in um.
        .. return:: execution result. True: successful; False: failed
        """