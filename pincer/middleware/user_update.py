# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when properties about a user changes"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..objects.user import User
from ..utils.types import Coro

if TYPE_CHECKING:
    from ..client import Client
    from ..core.gateway import Gateway
    from ..core.gateway import GatewayDispatch


async def user_update_middleware(
    self: Client, gateway: Gateway, payload: GatewayDispatch
) -> tuple[str, User]:
    """|coro|

    Middleware for the ``on_user_update`` event.

    Parameters
    ----------
    self :
        The client.
    payload :
        The data received from the user update event.
    gateway :
        The gateway for the current shard.
    """
    return ("on_user_update", User.from_dict(payload.data))


def export() -> Coro:
    return user_update_middleware
