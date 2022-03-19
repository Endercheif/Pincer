# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

from __future__ import annotations

from ._component import _Component
from ...objects.app.command import InteractableStructure

from ...utils.api_object import APIObject


class ActionRow(APIObject):
    """Represents an Action Row

    Parameters
    ----------
    \\*components : :class:`~pincer.objects.app.command.InteractableStructure`
        The components to add to the row.
    """

    def __init__(self, *components: InteractableStructure[_Component]):
        self.components = components

    def to_dict(self) -> dict:
        return {
            "type": 1,
            "components": [
                component.metadata.to_dict() for component in self.components
            ]
        }
