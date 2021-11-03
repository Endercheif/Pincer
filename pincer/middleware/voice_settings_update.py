# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when the client's voice settings update"""

from ..core.dispatch import GatewayDispatch
from ..objects.events.voice_settings import VoiceSettingsUpdateEvent
from ..utils.conversion import construct_client_dict


async def voice_settings_update_middleware(self, payload: GatewayDispatch):
    """|coro|

    Middleware for ``on_voice_settings_update`` event.

    Parameters
    ----------
    self : :class:`Client`
        The current client/bot.

    payload : :class:`GatewayDispatch`
        The data received from the voice settings update event.
        
    return :class:`VoiceSettingsUpdateEvent`
    """
    return "on_voice_settings_update", [
        VoiceSettingsUpdateEvent.from_dict(construct_client_dict(self, payload.data))
    ]


def export():
    return voice_settings_update_middleware
