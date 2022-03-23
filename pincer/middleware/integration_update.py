# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when an integration is updated"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..objects.events.integration import IntegrationUpdateEvent
from ..utils.types import Coro

if TYPE_CHECKING:
    from ..client import Client
    from ..core.gateway import Gateway
    from ..core.gateway import GatewayDispatch


async def integration_update_middleware(
    self: Client, gateway: Gateway, payload: GatewayDispatch
) -> tuple[str, IntegrationUpdateEvent]:
    """|coro|

    Middleware for the ``on_integration_update`` event.

    Parameters
    ----------
    self :
        The client.
    payload :
        The data received from the integration update event
    gateway :
        The gateway for the current shard.
    """  # noqa: E501
    return (
        "on_integration_update",
        IntegrationUpdateEvent.from_dict(payload.data),
    )


def export() -> Coro:
    return integration_update_middleware
