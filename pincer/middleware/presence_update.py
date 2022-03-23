# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when a user is updated"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..objects.events.presence import PresenceUpdateEvent
from ..utils.types import Coro

if TYPE_CHECKING:
    from ..client import Client
    from ..core.gateway import Gateway
    from ..core.gateway import GatewayDispatch


async def presence_update_middleware(
    self: Client, gateway: Gateway, payload: GatewayDispatch
) -> tuple[str, PresenceUpdateEvent]:
    """|coro|

    Middleware for the ``on_presence_update`` event.

    Parameters
    ----------
    self :
        The client.
    payload :
        The data received from the presence update event.
    gateway :
        The gateway for the current shard.
    """  # noqa: E501
    return ("on_presence_update", PresenceUpdateEvent.from_dict(payload.data))


def export() -> Coro:
    return presence_update_middleware
