# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""
sent when the user clicks a Rich Presence spectate invite in chat to
spectate a game
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..objects.events.activity import ActivitySpectateEvent
from ..utils.types import Coro

if TYPE_CHECKING:
    from ..client import Client
    from ..core.gateway import Gateway
    from ..core.gateway import GatewayDispatch


async def activity_spectate_middleware(
    self: Client, gateway: Gateway, payload: GatewayDispatch
) -> tuple[str, ActivitySpectateEvent]:
    """|coro|

    Middleware for the ``on_activity_spectate`` event.

    Parameters
    ----------
    self :
        The client.
    payload :
        The data received from the activity spectate event.
    gateway :
        The gateway for the current shard.
    """  # noqa: E501
    return "on_activity_spectate", ActivitySpectateEvent.from_dict(payload.data)


def export() -> Coro:
    return activity_spectate_middleware
