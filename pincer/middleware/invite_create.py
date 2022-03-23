# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when an invite was created"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..objects.events.invite import InviteCreateEvent
from ..utils.types import Coro

if TYPE_CHECKING:
    from ..client import Client
    from ..core.gateway import Gateway
    from ..core.gateway import GatewayDispatch


async def invite_create_middleware(
    self: Client, gateway: Gateway, payload: GatewayDispatch
) -> tuple[str, InviteCreateEvent]:
    """|coro|

    Middleware for the ``on_invite_create`` event.

    Parameters
    ----------
    self :
        The client.
    payload :
        The data received from the invite create event
    gateway :
        The gateway for the current shard.
    """  # noqa: E501
    return ("on_invite_create", InviteCreateEvent.from_dict(payload.data))


def export() -> Coro:
    return invite_create_middleware
