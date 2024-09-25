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
    @sila.ObservableCommand()
    @sila.IntermediateResponse(name="Process status")
    @sila.Response(name="Execution result")
    async def perform_scanning(self, *, status: sila.Status, intermediate: sila.Intermediate[str]) -> bool:   
        """
        Start scanning at current position.
        .. yield:: The current progress of scanning.
        .. return:: execution result. True: successful; False: failed
        """

