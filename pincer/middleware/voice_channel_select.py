# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when the client joins a voice channel"""

from ..core.dispatch import GatewayDispatch
from ..objects.events.voice import VoiceChannelSelectEvent
from ..utils.conversion import construct_client_dict


async def voice_channel_select_middleware(self, payload: GatewayDispatch):
    """|coro|

    Middleware for ``on_voice_channel_select`` event.

    Parameters
    ----------
    self : :class:`Client`
        The current client/bot.

    payload : :class:`GatewayDispatch`
        The data received from the voice channel select event.
        
    return :class:`VoiceChannelSelectEvent`
    """
    return "on_voice_channel_select", [
        VoiceChannelSelectEvent.from_dict(construct_client_dict(self, payload.data))
    ]


def export():
    return voice_channel_select_middleware
