# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

from __future__ import annotations

from ._component import _Component
from ...utils.types import Singleton
from ...objects.app.command import InteractableStructure


class ComponentHandler(metaclass=Singleton):
    """Handles registered components

    Attributes
    ----------
    register : :class:`dict`\\[:class:`str`, :class:`Callable`]
        dictionary of registered buttons.
    """

    register: dict[str, InteractableStructure[_Component]] = {}
