# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when an integration is created"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..objects.events.integration import IntegrationCreateEvent
from ..utils.types import Coro

if TYPE_CHECKING:
    from ..client import Client
    from ..core.gateway import Gateway
    from ..core.gateway import GatewayDispatch


async def integration_create_middleware(
    self: Client, gateway: Gateway, payload: GatewayDispatch
) -> tuple[str, IntegrationCreateEvent]:
    """|coro|

    Middleware for the ``on_integration_create`` event.

    Parameters
    ----------
    self :
        The client.
    payload :
        The data received from the integration create event
    gateway :
        The gateway for the current shard.
    """  # noqa: E501
    return (
        "on_integration_create",
        IntegrationCreateEvent.from_dict(payload.data),
    )


def export() -> Coro:
    return integration_create_middleware
