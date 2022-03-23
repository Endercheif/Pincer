# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when a guild ban is add."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..objects.events.guild import GuildBanAddEvent
from ..utils import Coro

if TYPE_CHECKING:
    from ..client import Client
    from ..core.gateway import Gateway
    from ..core.gateway import GatewayDispatch


async def guild_ban_add_middleware(
    self: Client, gateway: Gateway, payload: GatewayDispatch
) -> tuple[str, GuildBanAddEvent]:
    """|coro|

    Middleware for the ``on_guild_ban_add`` event.

    Parameters
    ----------
    self :
        The client.
    payload :
        The data received from the guild ban add event.
    gateway :
        The gateway for the current shard.
    """

    return ("on_guild_ban_add", GuildBanAddEvent.from_dict(payload.data))


def export() -> Coro:
    return guild_ban_add_middleware
