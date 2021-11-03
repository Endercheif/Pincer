# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.


from dataclasses import dataclass

from pincer.utils.conversion import construct_client_dict

from ...objects.message import UserMessage
from ...utils.snowflake import Snowflake
from ...utils.api_object import APIObject


@dataclass
class NotificationCreateEvent(APIObject):
    """
    Represents a notification

    :param channel_id:
        id of channel where notification occurred

    :param message:
        message that generated this notification

    :param icon_url:
        icon url of the notification

    :param title:
        title of the notification

    :param body:
        body of the notification
    """

    channel_id: Snowflake
    message: UserMessage
    icon_url: str
    title: str
    body: str
