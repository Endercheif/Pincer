# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when the client gains access to a channel"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..objects.events.thread import ThreadListSyncEvent

if TYPE_CHECKING:
    from ..client import Client
    from ..core.gateway import Gateway
    from ..core.gateway import GatewayDispatch


async def thread_list_sync(
    self: Client, gateway: Gateway, payload: GatewayDispatch
) -> tuple[str, ThreadListSyncEvent]:
    """|coro|

    Middleware for the ``on_thread_list_sync`` event.

    Parameters
    ----------
    self :
        The client.
    payload :
        The data received from the thread list sync event.
    gateway :
        The gateway for the current shard.
    """  # noqa: E501

    event = ThreadListSyncEvent.from_dict(payload.data)
    guild = self.guilds.get(event.guild_id)

    if guild:
        guild.threads = event.threads

    return "on_thread_list_sync", event


def export():
    return thread_list_sync
