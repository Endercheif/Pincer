# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""
Sent in response to Guild Request Members. You can use the ``chunk_index``
and ``chunk_count`` to calculate how many chunks are left for your request.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..objects.events.guild import GuildMembersChunkEvent
from ..utils import Coro

if TYPE_CHECKING:
    from ..client import Client
    from ..core.gateway import Gateway
    from ..core.gateway import GatewayDispatch


async def guild_member_chunk_middleware(
    self: Client, gateway: Gateway, payload: GatewayDispatch
) -> tuple[str, GuildMembersChunkEvent]:
    """|coro|

    Middleware for the ``on_guild_member_chunk`` event.

    Parameters
    ----------
    self :
        The client.
    payload :
        The data received from the guild member chunk event.
    gateway :
        The gateway for the current shard.
    """  # noqa: E501

    return (
        "on_guild_member_chunk",
        GuildMembersChunkEvent.from_dict(payload.data),
    )


def export() -> Coro:
    return guild_member_chunk_middleware
