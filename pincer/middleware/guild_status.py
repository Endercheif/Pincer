# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""Event sent when a subscribed server's state changes"""

from ..objects.events.guild import GuildStatusEvent
from ..utils.conversion import construct_client_dict
from ..core.dispatch import GatewayDispatch


async def guild_status_middleware(self, payload: GatewayDispatch):
    """
    Middleware for ``on_guild_status`` event.

    :param self:
        The current client.

    :param payload:
        The data received from the guild status event.
    """
    return "on_guild_status", [
        GuildStatusEvent.from_dict(construct_client_dict(self, payload.data))
    ]
    
def export():
    return guild_status_middleware
