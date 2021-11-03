# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

from ..core.dispatch import GatewayDispatch


async def payload_middleware(self, payload: GatewayDispatch):
    """|coro|

    Middleware for ``on_payload`` event. Invoked when basically anything is received from gateway.

    Parameters
    ----------
    self : :class:`Client`
        The current client/bot.

    payload : :class:`GatewayDispatch`
        The data received from the guild member update event.
        
    return :class:`GatewayDispatch`
    """
    return "on_payload", [payload]


def export():
    return payload_middleware
