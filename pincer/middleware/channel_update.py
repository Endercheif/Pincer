# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when a channel is updated"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..objects import Channel
from ..utils import replace

if TYPE_CHECKING:
    from ..client import Client
    from ..core.gateway import Gateway
    from ..core.gateway import GatewayDispatch


async def channel_update_middleware(
    self: Client, gateway: Gateway, payload: GatewayDispatch
) -> tuple[str, Channel]:
    """|coro|

    Middleware for the ``on_channel_update`` event.

    Parameters
    ----------
    self :
        The client.
    payload :
        The data received from the channel update event.
    gateway :
        The gateway for the current shard.
    """

    channel = Channel.from_dict(payload.data)
    guild = self.guilds.get(channel.guild_id)

    if guild:
        guild.channels = replace(
            lambda _channel: _channel.id == channel.id,
            self.guilds[channel.guild_id].channels,
            channel,
        )
        self.channels[channel.id] = channel

    return "on_channel_update", channel


def export():
    return channel_update_middleware
