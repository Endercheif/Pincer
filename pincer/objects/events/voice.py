# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

from ...utils.api_object import APIObject
from ...utils.snowflake import Snowflake
from ...utils.types import MISSING


@dataclass
class VoiceServerUpdateEvent(APIObject):
    """
    Sent when a guild's voice server is updated.
    This is sent when initially connecting to voice,
    and when the current voice instance fails over to a new server.

    :param token:
        voice connection token

    :param guild_id:
        the guild this voice server update is for

    :param endpoint:
        the voice server host
    """

    token: str
    guild_id: Snowflake
    endpoint: Optional[str] = None


@dataclass
class VoiceChannelSelectEvent(APIObject):
    """
    Sent when the client joins a voice channel

    :param channel_id:
        id of channel

    :param guild_id:
        id of guild
    """

    channel_id: Snowflake = MISSING
    guild_id: Snowflake = MISSING


class VoiceConnectionStates(Enum):
    """
    :param DISCONNECTED:
        TCP disconnected

    :param AWAITING_ENDPOINT:
        Waiting for voice endpoint

    :param AUTHENTICATING:
        TCP authenticating

    :param CONNECTING:
        TCP connecting

    :param CONNECTED:
        TCP connected

    :param VOICE_DISCONNECTED:
        TCP connected, Voice disconnected

    :param VOICE_CONNECTING:
        TCP connected, Voice connecting

    :param VOICE_CONNECTED:
        TCP connected, Voice connected

    :param NO_ROUTE:
        No route to host

    :param ICE_CHECKING:
        WebRTC ice checking
    """

    DISCONNECTED = "DISCONNECTED"
    AWAITING_ENDPOINT = "AWAITING_ENDPOINT"
    AUTHENTICATING = "AUTHENTICATING"
    CONNECTING = "CONNECTING"
    CONNECTED = "CONNECTED"
    VOICE_DISCONNECTED = "VOICE_DISCONNECTED"
    VOICE_CONNECTING = "VOICE_CONNECTING"
    VOICE_CONNECTED = "VOICE_CONNECTED"
    NO_ROUTE = "NO_ROUTE"
    ICE_CHECKING = "ICE_CHECKING"


@dataclass
class VoiceConnectionStatusEvent(APIObject):
    """
    Sent when the client's voice connection status changes

    :param state:
        one of the voice connection states listed below

    :param hostname:
        hostname of the connected voice server

    :param pings:
        last 20 pings (in ms)

    :param average_ping:
        average ping (in ms)

    :param last_ping:
        last ping (in ms)
    """

    state: VoiceConnectionStates
    hostname: str
    pings: List[int]
    average_ping: int
    last_ping: int
