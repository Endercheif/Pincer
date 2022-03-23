# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.


from dataclasses import dataclass

from ...objects.message import UserMessage
from ...utils.api_object import APIObject, ChannelProperty
from ...utils.snowflake import Snowflake


@dataclass(repr=False)
class NotificationCreateEvent(APIObject, ChannelProperty):
    """
    Represents a notification

    Attributes
    ----------
    channel_id : :class:`~pincer.utils.snowflake.Snowflake`
        ID of channel where notification occurred.

    message : :class:`UserMessage`
        Message that generated this notification.

    icon_url : :class:`str`
        Icon url of the notification.

    title : :class:`str`
        Title of the notification.

    body : :class:`str`
        Body of the notification.
    """

    channel_id: Snowflake
    message: UserMessage
    icon_url: str
    title: str
    body: str
