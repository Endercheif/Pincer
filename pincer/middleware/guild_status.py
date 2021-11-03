# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""Event sent when a subscribed server's state changes"""

from ..core.dispatch import GatewayDispatch
from ..objects.events.guild import GuildStatusEvent
from ..utils.conversion import construct_client_dict
from ..utils.types import Coro


async def guild_status_middleware(self, payload: GatewayDispatch):
    """|coro|

    Middleware for ``on_guild_status`` event.

    Parameters
    ----------
    self : :class:`Client`
        The current client/bot.

    payload : :class:`GatewayDispatch`
        The data received from the guild status event.
        
    return :class:`GuildStatusEvent`
    """
    return "on_guild_status", [
        GuildStatusEvent.from_dict(construct_client_dict(self, payload.data))
    ]


def export() -> Coro:
    return guild_status_middleware
