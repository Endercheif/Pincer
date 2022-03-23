# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""Sent when a stage instance is created."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..objects import StageInstance
from ..utils.types import Coro

if TYPE_CHECKING:
    from ..client import Client
    from ..core.gateway import Gateway
    from ..core.gateway import GatewayDispatch


async def stage_instance_create_middleware(
    self: Client, gateway: Gateway, payload: GatewayDispatch
) -> tuple[str, StageInstance]:
    """|coro|

    Middleware for the ``on_stage_instance_create`` event.

    Parameters
    ----------
    self :
        The client.
    payload :
        The data received from the stage instance create event
    gateway :
        The gateway for the current shard.
    """

    stage = StageInstance.from_dict(payload.data)

    guild = self.guilds.get(stage.guild_id)
    if guild:
        guild.stage_instances.append(stage)

    return "on_stage_instance_create", stage


def export() -> Coro:
    return stage_instance_create_middleware
