# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, IntEnum, auto

from ...utils.api_object import APIObject


@dataclass(repr=False)
class AvailableDevices(APIObject):
    """
    Represents an available device for voice settings.

    Attributes
    ----------
    id : :class:`str`
        ID of the available device.

    name : :class:`str`
        Name of the available device.
    """

    id: str
    name: str


@dataclass(repr=False)
class VoiceSettingsInput(APIObject):
    """
    Represents a voice setting input object.

    Attributes
    ----------
    device_id : :class:`str`
        The device's ID.

    volume : :class:`float`
        Input voice level (min: 0, max: 100).

    available_devices : :class:`list`\\[:class:`AvailableDevices`]
        Array of read-only device objects containing id and name string keys.
    """

    device_id: str
    volume: float
    available_devices: list[AvailableDevices]


@dataclass(repr=False)
class VoiceSettingsOutput(APIObject):
    """
    Represents a voice setting output object.

    Attributes
    ----------
    device_id : :class:`str`
        The device's ID.

    volume : :class:`float`
        Input voice level (min: 0, max: 100).

    available_devices : :class:`list`\\[:class:`AvailableDevices`]
        Array of read-only device objects containing id and name string keys.
    """

    device_id: str
    volume: float
    available_devices: list[AvailableDevices]


class VoiceSettingsModeType(Enum):
    """Represents a voice settings mode type."""

    PUSH_TO_TALK = auto()
    VOICE_ACTIVITY = auto()


class KeyTypes(IntEnum):
    """Represents a key type"""

    KEYBOARD_KEY = 0
    MOUSE_BUTTON = 1
    KEYBOARD_MODIFIER_KEY = 2
    GAMEPAD_BUTTON = 3


@dataclass(repr=False)
class ShortcutKeyCombo(APIObject):
    """
    Represents a shortcut key combo for the voice mode settings from a user.

    Attributes
    ----------
    type : :class:`KeyTypes`
        Type of shortcut key combo.

    code : :class:`str`
        Key code.

    name : :class:`str`
        Key name.
    """

    type: KeyTypes
    code: int
    name: str


@dataclass(repr=False)
class VoiceSettingsMode(APIObject):
    """
    Represents the voice mode settings from a user.

    Attributes
    ----------
    type : :class:`VoiceSettingsModeType`
        Voice setting mode type.

    auto_threshold : :class:`bool`
        Voice activity threshold automatically sets its threshold.

    threshold : :class:`float`
        Threshold for voice activity (in dB).

    shortcut : :class:`ShortcutKeyCombo`
        Shortcut key combos for PTT.

    delay : :class:`float`
        The PTT release delay (in ms) (min: 0, max: 2000).
    """

    type: VoiceSettingsModeType
    auto_threshold: bool
    threshold: float
    shortcut: ShortcutKeyCombo
    delay: float


@dataclass(repr=False)
class VoiceSettingsUpdateEvent(APIObject):
    """
    Represents a user's voice settings.

    Attributes
    ----------
    input : :class:`VoiceSettingsInput`
        Input settings.

    output : :class:`VoiceSettingsOutput`
        Output settings.

    mode : :class:`bool`
        Voice mode settings.

    automatic_gain_control : :class:`bool`
        State of automatic gain control.

    echo_cancellation : :class:`bool`
        State of echo cancellation.

    noise_suppression : :class:`bool`
        State of noise suppression.

    qos : :class:`bool`
        State of voice quality of service.

    silence_warning : :class:`bool`
        State of silence warning notice.

    deaf : :class:`bool`
        State of self-deafen.

    mute : :class:`bool`
        State of self-mute.
    """

    input: VoiceSettingsInput
    output: VoiceSettingsOutput
    automatic_gain_control: bool
    echo_cancellation: bool
    noise_suppression: bool
    qos: bool
    silence_warning: bool
    deaf: bool
    mute: bool
