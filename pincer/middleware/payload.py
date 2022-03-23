# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import Client
    from ..core.gateway import Gateway
    from ..core.gateway import GatewayDispatch


async def payload_middleware(
    self: Client,
    gateway: Gateway,
    payload: GatewayDispatch,
) -> tuple[str, GatewayDispatch]:
    """Invoked when anything is received from gateway.


    Parameters
    ----------
    self :
        The client.
    payload :
        The data received from the ready event.
    gateway :
        The gateway for the current shard.
    """
    return "on_payload", payload


def export():
    return payload_middleware
