# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when a user parts a subscribed voice channel"""

from ..core.dispatch import GatewayDispatch
from ..objects.user import VoiceState
from ..utils.conversion import construct_client_dict


async def voice_state_delete_middleware(self, payload: GatewayDispatch):
    """
    Middleware for ``on_voice_delete_delete`` event.

    :param self:
        The current client.

    :param payload:
        The data received from the voice state delete event.

    """
    return "on_voice_state_delete", [
        VoiceState.from_dict(construct_client_dict(self, payload.data))
    ]


def export():
    return voice_state_delete_middleware