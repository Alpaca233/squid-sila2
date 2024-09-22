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
    async def get_stage_position_once(self) -> str:
        """
        Retrieve the position of the stage once.
        """

    @abc.abstractmethod
    @sila.UnobservableCommand()
    @sila.Response(name="Result")
    async def perform_scanning(self) -> bool:
        """
        Start scanning at current position.

        .. return:: execution result
        """

    @abc.abstractmethod
    @sila.UnobservableCommand()
    @sila.Response(name="Result")
    async def move_to_loading_position(self) -> bool:
        """
        Move stage to loading position.

        .. return:: execution result
        """

    @abc.abstractmethod
    @sila.UnobservableCommand()
    @sila.Response(name="Result")
    async def move_to_scanning_position(self) -> bool:
        """
        Move stage to scanning position.

        .. return:: execution result
        """