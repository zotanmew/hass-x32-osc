from homeassistant.core import HomeAssistant, ServiceCall, callback
from homeassistant.helpers.typing import ConfigType

from .x32 import *

DOMAIN = "x32_osc"

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up is called when Home Assistant is loading our component."""

    @callback
    def load_scene(call: ServiceCall) -> None:
        """Handle the service action call."""
        scene_id = int(call.data.get("scene_id", "1"))
        ip = call.data.get("ip", "")
        port = 10023
        x32_load_scene(ip, port, scene_id)

    @callback
    def set_main_vol(call: ServiceCall) -> None:
        """Handle the service action call."""
        vol = float(call.data.get("volume", "0.0"))
        ip = call.data.get("ip", "")
        port = 10023
        x32_set_main_vol(ip, port, vol)

    hass.services.async_register(DOMAIN, "load_scene", load_scene)
    hass.services.async_register(DOMAIN, "set_main_vol", set_main_vol)

    # Return boolean to indicate that initialization was successful.
    return True
