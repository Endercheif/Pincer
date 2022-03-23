# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""Sent when a stage instance is deleted or closed."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..objects import StageInstance
from ..utils.types import Coro

if TYPE_CHECKING:
    from ..client import Client
    from ..core.gateway import Gateway
    from ..core.gateway import GatewayDispatch


async def stage_instance_delete_middleware(
    self: Client, gateway: Gateway, payload: GatewayDispatch
) -> tuple[str, StageInstance]:
    """|coro|

    Middleware for the ``on_stage_instance_delete`` event.

    Parameters
    ----------
    self :
        The client.
    payload :
        The data received from the stage instance delete event
    gateway :
        The gateway for the current shard.
    """

    stage = StageInstance.from_dict(payload.data)

    guild = self.guilds.get(stage.guild_id)
    if guild:
        guild.stage_instances = [
            _stage for _stage in guild.stage_instances if _stage.id != stage.id
        ]

    return "on_stage_instance_delete", stage


def export() -> Coro:
    return stage_instance_delete_middleware
