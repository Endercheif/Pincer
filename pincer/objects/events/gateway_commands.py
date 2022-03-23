# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

from __future__ import annotations

from dataclasses import dataclass
from enum import auto, Enum
from typing import TYPE_CHECKING

from ...utils.api_object import APIObject, GuildProperty
from ...utils.types import APINullable, MISSING

if TYPE_CHECKING:
    from typing import Any, Optional

    from .presence import Activity
    from ..app.intents import Intents
    from ...utils.snowflake import Snowflake


@dataclass(repr=False)
class Identify(APIObject):
    """Used to trigger the initial handshake with the gateway.

    Attributes
    ----------
    token : :class:`str`
        Authentication token.
    properties : :class:`dict`\\[:class:`str`, :class:`str`]
        Connection properties.
    intents : :class:`~pincer.objects.app.intents.Intents`
        The Gateway Intents you wish to receive.
    compress : APINullable[:class:`bool`]
        Whether this connection supports compression of packets.
    large_threshold : APINullable[:class:`int`]
        Value between 50 and 250, total number
        of members where the gateway will stop sending offline
        members in the guild member list.
    shard : APINullable[:class:`tuple`\\[:class:`int`, :class:`int`]]
        Used for Guild Sharding.
    presence : APINullable[Any]
        Presence structure for initial presence information.
    """

    token: str
    properties: dict[str, str]
    intents: Intents

    compress: APINullable[bool] = MISSING
    large_threshold: APINullable[int] = MISSING
    shard: APINullable[tuple[int, int]] = MISSING
    presence: APINullable[Any] = MISSING  # FIXME


@dataclass(repr=False)
class Resume(APIObject):
    """Used to replay missed events when a disconnected client resumes.

    Attributes
    ----------
    token : :class:`str`
        Session token.
    session_id : :class:`str`
        Session id.
    seq : :class:`int`
        Last sequence number received.
    """

    token: str
    session_id: str
    seq: int


@dataclass(repr=False)
class RequestGuildMembers(APIObject, GuildProperty):
    """Used to request all members for a guild or a list of guilds.

    Attributes
    ----------
    guild_id : :class:`~pincer.utils.snowflake.Snowflake`
        ID of the guild to get members for.

    query : APINullable[:class:`str`]
        String that username starts with, or an empty string
        to return all members.

    limit : int
        Maximum number of members to send matching the ``query``;
        a limit of ``0`` can be used with an empty string ``query``
        to return all members.

    presences : APINullable[:class:`bool`]
        Used to specify if we want the presences of the matches members.

    user_ids : APINullable[:class:`~pincer.utils.snowflake.Snowflake` | :class:`list`\\[:class:`~pincer.utils.snowflake.Snowflake`]]
        Used to specify which users you wish to fetch.

    nonce : APINullable[:class:`str`]
        Nonce to identify the Guild Members Chunk response.
    """

    guild_id: Snowflake
    limit: int

    query: APINullable[str] = MISSING
    presences: APINullable[bool] = MISSING
    user_ids: APINullable[Snowflake | list[Snowflake]] = MISSING
    nonce: APINullable[str] = MISSING


@dataclass(repr=False)
class UpdateVoiceState(APIObject, GuildProperty):
    """Sent when a client wants to join, move,
    or disconnect from a voice channel.

    Attributes
    ----------
    guild_id : :class:`~pincer.utils.snowflake.Snowflake`
        ID of the guild.

    channel_id : Optional[:class:`~pincer.utils.snowflake.Snowflake`]
        ID of the voice channel client
        wants to join (null if disconnecting).

    self_mute : bool
        Is the client muted.

    self_deaf : bool
        Is the client deafened.
    """

    guild_id: Snowflake
    self_mute: bool
    self_deaf: bool

    channel_id: Optional[Snowflake] = None


class StatusType(Enum):
    """
    Attributes
    ----------
    online :
        Online

    dnd :
        Do Not Disturb

    idle :
        AFK

    invisible :
        Invisible and shown as offline

    offline :
        Offline
    """

    online = auto()
    dnd = auto()
    idle = auto()
    invisible = auto()
    offline = auto()


@dataclass(repr=False)
class UpdatePresence(APIObject):
    """Sent by the client to indicate a presence or status update.

    Attributes
    ----------
    since : :class:`list`\\[:class:`~pincer.objects.events.presence.Activity`]
        Unix time (in milliseconds) of when the client went idle,
        or null if the client is not idle.

    activities : :class:`~pincer.objects.events.gateway_commands.StatusType`
        The user's activities.

    status : :class:`bool`
        The user's new status.

    afk : :class:`~typing.Optional`\\[:class:`int`]
        Whether the client is afk.
    """

    activities: list[Activity]
    status: StatusType
    afk: bool
    since: Optional[int] = None
