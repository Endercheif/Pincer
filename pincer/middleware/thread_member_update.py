# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when the thread member object for the current user is updated"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..objects import ThreadMember

if TYPE_CHECKING:
    from ..client import Client
    from ..core.gateway import Gateway
    from ..core.gateway import GatewayDispatch


async def thread_member_update_middleware(
    self: Client, gateway: Gateway, payload: GatewayDispatch
) -> tuple[str, ThreadMember]:
    """|coro|

    Middleware for the ``on_thread_member_update`` event.

    Parameters
    ----------
    self :
        The client.
    payload :
        The data received from the thread member update event.
    gateway :
        The gateway for the current shard.
    """

    return (
        "on_thread_member_update",
        ThreadMember.from_dict(payload.data),
    )


def export():
    return thread_member_update_middleware
