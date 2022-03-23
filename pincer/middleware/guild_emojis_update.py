# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when a guild emoji is updated."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..objects.events.guild import GuildEmojisUpdateEvent
from ..utils import Coro

if TYPE_CHECKING:
    from ..client import Client
    from ..core.gateway import Gateway
    from ..core.gateway import GatewayDispatch


async def guild_emojis_update_middleware(
    self: Client, gateway: Gateway, payload: GatewayDispatch
) -> tuple[str, GuildEmojisUpdateEvent]:
    """|coro|

    Middleware for the ``on_guild_emojis_update`` event.

    Parameters
    ----------
    self :
        The client.
    payload :
        The data received from the guild emojis update event.
    gateway :
        The gateway for the current shard.
    """  # noqa: E501

    event = GuildEmojisUpdateEvent.from_dict(payload.data)
    guild = self.guild.get(event.guild_id)

    if guild:
        guild.emojis = event.emojis

    return ("on_guild_emojis_update", event)


def export() -> Coro:
    return guild_emojis_update_middleware
