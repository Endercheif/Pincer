# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when the client's voice connection status changes"""

from ..objects.events.voice import VoiceConnectionStatusEvent
from ..utils.conversion import construct_client_dict
from ..core.dispatch import GatewayDispatch


async def voice_connection_status_middleware(self, payload: GatewayDispatch):
    """|coro|

    Middleware for ``on_voice_connection_status`` event.

    Parameters
    ----------
    self : :class:`Client`
        The current client/bot.

    payload : :class:`GatewayDispatch`
        The data received from the voice connection status event.
        
    return :class:`VoiceConnectionStatusEvent`
    """
    return "on_voice_connection_status", [
        VoiceConnectionStatusEvent.from_dict(construct_client_dict(self, payload.data))
    ]


def export():
    return voice_connection_status_middleware
