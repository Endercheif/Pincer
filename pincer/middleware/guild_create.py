# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when a guild is created/joined on the client"""

from ..core.dispatch import GatewayDispatch
from ..objects.guild import Guild
from ..utils.conversion import construct_client_dict
from ..utils.types import Coro


async def guild_create_middleware(self, payload: GatewayDispatch):
    """|coro|

    Middleware for ``on_guild_member_update`` event.

    Parameters
    ----------
    self : :class:`Client`
        The current client/bot.

    payload : :class:`GatewayDispatch`
        The data received from the guild member update event.
        
    return :class:`Guild`
    """
    guild = Guild.from_dict(construct_client_dict(self, payload.data))
    self.guilds[guild.id] = guild
    return "on_guild_create", [guild]


def export() -> Coro:
    return guild_create_middleware
