# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""
Sent when the user clicks a Rich Presence join invite in chat
to join a game.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from ..objects.events.activity import ActivityJoinEvent
from ..utils.types import Coro

if TYPE_CHECKING:
    from ..client import Client
    from ..core.gateway import Gateway
    from ..core.gateway import GatewayDispatch


async def activity_join_middleware(
    self: Client, gateway: Gateway, payload: GatewayDispatch
) -> tuple[str, ActivityJoinEvent]:
    """|coro|

    Middleware for the ``on_activity_join`` event.

    Parameters
    ----------
    self :
        The client.
    payload :
        The data received from the activity join event.
    gateway :
        The gateway for the current shard.
    """  # noqa: E501
    return (
        "on_activity_join",
        ActivityJoinEvent.from_dict(payload.data),
    )


def export() -> Coro:
    return activity_join_middleware
