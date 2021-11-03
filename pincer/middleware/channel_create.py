# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""Sent when a channel is created/joined on the client."""
from pincer.core.dispatch import GatewayDispatch
from pincer.objects import Channel
from pincer.utils.conversion import construct_client_dict


def channel_create_middleware(self, payload: GatewayDispatch):
    """|coro|

    Middleware for ``on_channel_create`` event.

    Parameters
    ----------
    self : :class:`Client`
        The current client/bot.

    payload : :class:`GatewayDispatch`
        The data received from the channel create event.
        
    return :class:`Channel`
    """

    return "on_channel_creation", [
        Channel.from_dict(construct_client_dict(self, payload.data))
    ]
