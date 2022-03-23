# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""
Sent when a user is removed from a guild (leave/kick/ban).
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..objects.events.guild import GuildMemberRemoveEvent
from ..utils import Coro

if TYPE_CHECKING:
    from ..client import Client
    from ..core.gateway import Gateway
    from ..core.gateway import GatewayDispatch


async def guild_member_remove_middleware(
    self: Client, gateway: Gateway, payload: GatewayDispatch
) -> tuple[str, GuildMemberRemoveEvent]:
    """|coro|

    Middleware for the ``on_guild_member_remove`` event.

    Parameters
    ----------
    self :
        The client.
    payload :
        The data received from the guild member remove event.
    gateway :
        The gateway for the current shard.
    """

    return (
        "on_guild_member_remove",
        GuildMemberRemoveEvent.from_dict(payload.data),
    )


def export() -> Coro:
    return guild_member_remove_middleware
