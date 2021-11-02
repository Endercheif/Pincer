# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""
sent when the user clicks a Rich Presence spectate invite in chat to
spectate a game
"""


from ..core.dispatch import GatewayDispatch


async def activity_spectate_middleware(self, payload: GatewayDispatch):
    """
    Middleware for ``on_activity_spectate`` event.

    :param self:
        The current client.

    :param payload:
        The data received from the activity spectate event.
    """
    secret: str = payload.data.get("secret")
    return "on_activity_spectate", [
        secret
    ]

def export():
    return activity_spectate_middleware


