# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""
non-subscription event sent when there is an error,
including command responses
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from ..objects.events.error import DiscordError
from ..utils.types import Coro

if TYPE_CHECKING:
    from ..client import Client
    from ..core.gateway import Gateway
    from ..core.gateway import GatewayDispatch


def error_middleware(
    self: Client, gateway: Gateway, payload: GatewayDispatch
) -> tuple[str, DiscordError]:
    """|coro|

    Middleware for the ``on_error`` event.

    Parameters
    ----------
    self :
        The client.
    payload :
        The data received from the ready event.
    gateway :
        The gateway for the current shard.
    """
    # noqa: E501

    return "on_error", DiscordError.from_dict(payload.data)


def export() -> Coro:
    return error_middleware
