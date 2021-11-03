# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""
non-subscription event sent immediately after connecting,
contains server information
"""

from ..commands import ChatCommandHandler
from ..core.dispatch import GatewayDispatch
from ..exceptions import InvalidPayload
from ..objects import User
from ..utils import Coro
from ..utils.conversion import construct_client_dict


async def ready_middleware(self, payload: GatewayDispatch):
    """|coro|
    
    Middleware for ``on_ready`` event.

    Parameters
    ----------
    self : :class:`Client`
        The current client/bot

    payload : :class:`GatewayDispatch`
        The data recieved from the stage instance create event
        
    Returns
    -------
    Tuple[:class:`str`]
        ``on_ready``
    """
    user = payload.data.get("user")
    guilds = payload.data.get("guilds")

    if not user or guilds is None:
        raise InvalidPayload(
            "A `user` and `guilds` key/value pair is expected on the "
            "`ready` payload event."
        )

    self.bot = User.from_dict(construct_client_dict(self, user))
    self.guilds = dict(map(lambda i: (i["id"], None), guilds))

    await ChatCommandHandler(self).initialize()
    return ("on_ready",)


def export() -> Coro:
    return ready_middleware
