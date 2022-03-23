# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when anyone is added to or removed from a thread"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..objects.events.thread import ThreadMembersUpdateEvent

if TYPE_CHECKING:
    from ..client import Client
    from ..core.gateway import Gateway
    from ..core.gateway import GatewayDispatch


async def thread_members_update_middleware(
    self: Client, gateway: Gateway, payload: GatewayDispatch
) -> tuple[str, ThreadMembersUpdateEvent]:
    """|coro|

    Middleware for the ``on_thread_members_update`` event.

    Parameters
    ----------
    self :
        The client.
    payload :
        The data received from the thread members update event.
    gateway :
        The gateway for the current shard.
    """  # noqa: E501
    return (
        "on_thread_members_update",
        ThreadMembersUpdateEvent.from_dict(payload.data),
    )


def export():
    return thread_members_update_middleware
