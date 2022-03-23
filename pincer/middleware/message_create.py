# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when a message is created in a subscribed text channel"""
from __future__ import annotations

from typing import TYPE_CHECKING

from ..objects.message.user_message import UserMessage

if TYPE_CHECKING:
    from ..client import Client
    from ..core.gateway import Gateway
    from ..core.gateway import GatewayDispatch


async def message_create_middleware(
    self: Client, gateway: Gateway, payload: GatewayDispatch
) -> tuple[str, UserMessage]:
    """|coro|

    Middleware for the ``on_message`` event.

    Parameters
    ----------
    self :
        The client.
    payload :
        The data received from the message creation event.
    gateway :
        The gateway for the current shard.
    """  # noqa: E501
    return ("on_message", UserMessage.from_dict(payload.data))


def export():
    return message_create_middleware
