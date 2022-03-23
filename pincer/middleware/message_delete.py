# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when a message is deleted in a subscribed text channel"""
from __future__ import annotations

from typing import TYPE_CHECKING

from ..objects.events.message import MessageDeleteEvent

if TYPE_CHECKING:
    from ..client import Client
    from ..core.gateway import Gateway
    from ..core.gateway import GatewayDispatch


async def on_message_delete_middleware(
    self: Client, gateway: Gateway, payload: GatewayDispatch
) -> tuple[str, MessageDeleteEvent]:
    """|coro|
    Middleware for the ``on_message_delete`` event.

    Parameters
    ----------
    self :
        The client.
    payload :
        The data received from the message delete event
    gateway :
        The gateway for the current shard.
    """  # noqa: E501

    return ("on_message_delete", MessageDeleteEvent.from_dict(payload.data))


def export():
    return on_message_delete_middleware
