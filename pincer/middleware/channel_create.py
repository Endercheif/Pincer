# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""Sent when a channel is created/joined on the client."""
from __future__ import annotations

from typing import TYPE_CHECKING

from ..objects.guild.channel import Channel

if TYPE_CHECKING:
    from ..core.gateway import GatewayDispatch
    from ..client import Client
    from ..core.gateway import Gateway


async def channel_create_middleware(
    self: Client, gateway: Gateway, payload: GatewayDispatch
) -> tuple[str, Channel]:
    """|coro|

    Middleware for the ``on_channel_creation`` event.

    Parameters
    ----------
    self :
        The client.
    payload :
        The data received from the ready event.
    gateway :
        The gateway for the current shard.
    """

    channel: Channel = Channel.from_dict(payload.data)

    self.guilds[channel.guild_id].channels.append(channel)
    self.channels[channel.id] = channel

    return "on_channel_creation", channel


def export():
    return channel_create_middleware
