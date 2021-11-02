# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when the client's voice settings update"""

from ..core.dispatch import GatewayDispatch
from ..objects.user import VoiceSettings
from ..utils.conversion import construct_client_dict


async def voice_settings_update_middleware(self, payload: GatewayDispatch):
    """
    Middleware for ``on_voice_settings_update`` event.

    :param self:
        The current client.

    :param payload:
        The data received from the voice settings update event.

    """
    return "on_voice_settings_update", [
        VoiceSettings.from_dict(construct_client_dict(self, payload.data))
    ]


def export():
    return voice_settings_update_middleware