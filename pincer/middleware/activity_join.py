# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""
Sent when the user clicks a Rich Presence join invite in chat
to join a game.
"""

from ..core.dispatch import GatewayDispatch


async def activity_join_middleware(self, payload: GatewayDispatch):
    """
    Middleware for ``on_activity_join`` event.

    :param self:
        The current client.

    :param payload:
        The data received from the activity join event.
    """
    secret: str = payload.data.get("secret")
    return "on_activity_join", [
        secret
    ]

def export():
    return activity_join_middleware
