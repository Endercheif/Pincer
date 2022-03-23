# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when a user in a subscribed voice channel speaks"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..objects.events.voice import SpeakingStartEvent
from ..utils.types import Coro

if TYPE_CHECKING:
    from ..client import Client
    from ..core.gateway import Gateway
    from ..core.gateway import GatewayDispatch


async def speaking_start_middleware(
    self: Client, gateway: Gateway, payload: GatewayDispatch
) -> tuple[str, SpeakingStartEvent]:
    """|coro|

    Middleware for the ``on_speaking_start`` event.

    Parameters
    ----------
    self :
        The client.
    payload :
        The data received from the speaking start event.
    gateway :
        The gateway for the current shard.
    """
    return ("on_speaking_start", SpeakingStartEvent.from_dict(payload.data))


def export() -> Coro:
    return speaking_start_middleware
