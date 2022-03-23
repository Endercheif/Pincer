# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

from dataclasses import dataclass

from ...utils import APIObject


@dataclass(repr=False)
class ActivityJoinEvent(APIObject):
    """
    Sent when the user clicks a Rich Presence join invite in chat to join a game.

    Attributes
    ----------
    secret : :class:`str`
        The ``join_secret`` for the given invite.
    """

    secret: str


@dataclass(repr=False)
class ActivitySpectateEvent(APIObject):
    """
    Sent when the user clicks a Rich Presence spectate invite in chat to spectate a game.

    Attributes
    ----------
    secret : :class:`str`
        The ``spectate_secret`` for the given invite.
    """

    secret: str
