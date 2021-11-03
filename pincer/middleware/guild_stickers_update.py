# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

"""sent when a guild sticker is updated."""

from ..core.dispatch import GatewayDispatch
from ..objects.events.guild import GuildStickersUpdateEvent
from ..utils import Coro
from ..utils.conversion import construct_client_dict


async def guild_stickers_update_middleware(self, payload: GatewayDispatch):
    """|coro|

    Middleware for ``on_guild_stickers_update`` event.

    Parameters
    ----------
    self : :class:`Client`
        The current client/bot.

    payload : :class:`GatewayDispatch`
        The data received from the guild stickers update event.

    Returns
    -------
    Tuple[:class:`str`, List[:class:`~pincer.objects.events.guild.GuildStickersUpdateEvent`]]
        ``on_guild_sticker_update`` and a ``GuildStickersUpdateEvent`` object
    """

    return (
        "on_guild_stickers_update",
        [
            GuildStickersUpdateEvent.from_dict(
                construct_client_dict(self, payload.data)
            )
        ],
    )


def export() -> Coro:
    return guild_stickers_update_middleware