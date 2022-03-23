# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""
non-subscription event sent immediately after connecting,
contains server information
"""
from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..utils.types import Coro
    from ..client import Client
    from ..core.gateway import Gateway
    from ..core.gateway import GatewayDispatch

_log = logging.getLogger(__package__)


async def on_resumed(
    self: Client, gateway: Gateway, payload: GatewayDispatch
) -> tuple[str]:
    """|coro|

    Middleware for the ``on_resumed`` event.

    Parameters
    ----------
    self :
        The client.
    payload :
        The data received from the stage instance create event
    gateway :
        The gateway for the current shard.
    """

    _log.debug(
        "%s Successfully reconnected to Discord gateway. Restarting heartbeat.",
        gateway.shard_key,
    )
    gateway.start_heartbeat()

    return ("on_resumed",)


def export() -> Coro:
    return on_resumed
