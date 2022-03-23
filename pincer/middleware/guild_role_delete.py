# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when a guild role was deleted."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..objects.events.guild import GuildRoleDeleteEvent
from ..utils import Coro

if TYPE_CHECKING:
    from ..client import Client
    from ..core.gateway import Gateway
    from ..core.gateway import GatewayDispatch


async def guild_role_delete_middleware(
    self: Client, gateway: Gateway, payload: GatewayDispatch
) -> tuple[str, GuildRoleDeleteEvent]:
    """|coro|

    Middleware for the ``on_guild_role_delete`` event.

    Parameters
    ----------
    self :
        The client.
    payload :
        The data received from the guild role delete event.
    gateway :
        The gateway for the current shard.
    """  # noqa: E501

    event = GuildRoleDeleteEvent.from_dict(payload.data)
    guild = self.guilds.get(event.guild_id)

    if guild:
        guild.roles = [
            role
            for role in self.guilds[event.guild_id].roles
            if role.id != event.role_id
        ]

    return ("on_guild_role_delete", event)


def export() -> Coro:
    return guild_role_delete_middleware
