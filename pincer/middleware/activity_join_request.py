# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when the user receives a Rich Presence Ask to Join request"""

from ..objects.user.user import User
from ..utils.conversion import construct_client_dict
from ..core.dispatch import GatewayDispatch


async def activity_join_request_middleware(self, payload: GatewayDispatch):
    """
    Middleware for ``on_activity_join_request`` event.

    :param self:
        The current client.

    :param payload:
        The data received from the activity join request event.
    """
    return "on_activity_join_request", [
        User.from_dict(construct_client_dict(self, payload.data))
    ]

def export():
    return activity_join_request_middleware
