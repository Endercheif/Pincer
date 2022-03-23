# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when a guild integration is updated."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..objects.events.guild import GuildIntegrationsUpdateEvent
from ..utils import Coro

if TYPE_CHECKING:
    from ..client import Client
    from ..core.gateway import Gateway
    from ..core.gateway import GatewayDispatch


async def guild_integrations_update_middleware(
    self: Client, gateway: Gateway, payload: GatewayDispatch
) -> tuple[str, GuildIntegrationsUpdateEvent]:
    """|coro|

    Middleware for the ``on_guild_integrations_update`` event.

    Parameters
    ----------
    self :
        The client.
    payload :
        The data received from the guild integrations update event.
    gateway :
        The gateway for the current shard.
    """  # noqa: E501

    return (
        "on_guild_integrations_update",
        GuildIntegrationsUpdateEvent.from_dict(payload.data),
    )


def export() -> Coro:
    return guild_integrations_update_middleware
