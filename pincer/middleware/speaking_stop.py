# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when a user in a subscribed voice channel stops speaking"""

from ..core.dispatch import GatewayDispatch


async def speaking_stop_middleware(self, payload: GatewayDispatch):
    """
    Middleware for ``on_speaking_stop`` event.

    :param self:
        The current client.

    :param payload:
        The data received from the speaking stop event.

    """
    user_id: int = payload.data.get("user_id")
    return "on_speaking_stop", [
        user_id
    ]
    
def export():
    return speaking_stop_middleware