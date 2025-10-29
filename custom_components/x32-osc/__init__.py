from homeassistant.core import HomeAssistant, ServiceCall, callback
from homeassistant.helpers.typing import ConfigType

from .x32 import *

DOMAIN = "x32_osc"

ATTR_NAME = "name"
DEFAULT_NAME = "World"


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up is called when Home Assistant is loading our component."""

    @callback
    def load_scene(call: ServiceCall) -> None:
        """Handle the service action call."""
        scene_id = int(call.data.get("scene_id", "1"))
        ip = call.data.get("ip", "")
        port = 10023

    @callback
    def set_main_vol(call: ServiceCall) -> None:
        """Handle the service action call."""
        scene_id = float(call.data.get("volume", "0.0"))
        ip = call.data.get("ip", "")
        port = 10023

    hass.services.async_register(DOMAIN, "load_scene", load_scene)
    hass.services.async_register(DOMAIN, "set_main_vol", set_main_vol)

    # Return boolean to indicate that initialization was successful.
    return True
