# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when a guild role was created."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..objects.events.guild import GuildRoleCreateEvent
from ..utils import Coro

if TYPE_CHECKING:
    from ..client import Client
    from ..core.gateway import Gateway
    from ..core.gateway import GatewayDispatch


async def guild_role_create_middleware(
    self: Client, gateway: Gateway, payload: GatewayDispatch
) -> tuple[str, GuildRoleCreateEvent]:
    """|coro|

    Middleware for the ``on_guild_role_create`` event.

    Parameters
    ----------
    self :
        The client.
    payload :
        The data received from the guild role create event.
    gateway :
        The gateway for the current shard.
    """  # noqa: E501

    event = GuildRoleCreateEvent.from_dict(payload.data)
    guild = self.guilds.get(event.guild_id)

    if guild:
        guild.roles.append(event.role)

    return ("on_guild_role_create", event)


def export() -> Coro:
    return guild_role_create_middleware
