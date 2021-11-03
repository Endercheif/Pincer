# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when a message is updated in a subscribed text channel"""

from ..core.dispatch import GatewayDispatch
from ..objects import UserMessage
from ..utils.conversion import construct_client_dict
from ..utils.types import Coro


async def message_update_middleware(self, payload: GatewayDispatch):
    """|coro|

    Middleware for ``on_message_update`` event.

    Parameters
    ----------
    self : :class:`Client`
        The current client/bot.

    payload : :class:`GatewayDispatch`
        The data received from the message update event.
        
    return :class:`UserMessage`
    """
    return "on_message_update", [
        UserMessage.from_dict(construct_client_dict(self, payload.data))
    ]


def export() -> Coro:
    return message_update_middleware
