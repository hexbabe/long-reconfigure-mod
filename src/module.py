from threading import Thread
import time
from typing import Any, ClassVar, Coroutine, List, Mapping, SupportsBytes, SupportsFloat, Optional
from typing_extensions import Self

from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.components.generic import Generic, Reconfigurable
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily
from viam.utils import ValueTypes

from viam.logging import getLogger

LOGGER = getLogger(__name__)

class HeartBeatModule(Generic, Reconfigurable):
    """
    Generic component, which represents any type of component that can execute arbitrary commands
    """
    MODEL: ClassVar[Model] = Model(ModelFamily("seanorg", "generic"), "long-reconfigure")

    # Constructor
    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        LOGGER.info("Initializing module")
        module_obj = cls(config.name)
        return module_obj

    @classmethod
    def validate(cls, config: ComponentConfig):
        LOGGER.info("Validating")

    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        LOGGER.info("Reconfiguring")
        time.sleep(60)
        LOGGER.info("Reconfigured")

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Coroutine[Any, Any, Mapping[str, ValueTypes]]:
        LOGGER.info("Pinged do_command")
        return {
            "message": "Pong"
        }

    async def close(self):
        LOGGER.info("Closing component")
