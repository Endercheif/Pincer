# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""
sent when the client receives a notification
(mention or new message in eligible channels)
"""

from ..utils.conversion import construct_client_dict
from ..objects.events.notification import NotificationCreateEvent
from ..core.dispatch import GatewayDispatch


async def notification_create_middleware(self, payload: GatewayDispatch):
    """
    Middleware for ``on_notification_create`` event.

    :param self:
        The current client.

    :param payload:
        The data received from the notification create event.
    """
    channel_id: int = payload.data.get("channel_id")
    payload.data["message"]["channel_id"] = channel_id
    return "notification_create", [
        NotificationCreateEvent.from_dict(construct_client_dict(self, payload.data))
    ]

def export():
    return notification_create_middleware