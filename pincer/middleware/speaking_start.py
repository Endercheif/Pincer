# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when a user in a subscribed voice channel speaks"""

from ..core.dispatch import GatewayDispatch


async def speaking_start_middleware(self, payload: GatewayDispatch):
    """
    Middleware for ``on_speaking_start`` event.

    :param self:
        The current client.

    :param payload:
        The data received from the speaking start event.

    """
    user_id: int = payload.data.get("user_id")
    return "on_speaking_start", [
        user_id
    ]
    
def export():
    return speaking_start_middleware
