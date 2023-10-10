import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from KingX import LOGGER, app, userbot
from KingX.core.call import Hotty
from KingX.misc import sudo
from KingX.plugins import ALL_MODULES
from KingX.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("KingX.plugins" + all_module)
    LOGGER("KingX.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Hotty.start()
    try:
        await Hotty.stream_call("https://graph.org/file/d4ff97562ea67593e81c8.mp4")
    except NoActiveGroupCall:
        LOGGER("KingX").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Hotty.decorators()
    LOGGER("KingX").info(
        "ᴅʀᴏᴘ ʏᴏᴜʀ ɢɪʀʟꜰʀɪᴇɴᴅ'ꜱ ɴᴜᴍʙᴇʀ ᴀᴛ @ʙʀᴀɴᴅᴇᴅᴋɪɴɢ82 ᴊᴏɪɴ @ʙʀᴀɴᴅʀᴅ_ʙᴏᴛ , @ʙʀᴀɴᴅᴇᴅ_ᴡᴏʀʟᴅ ꜰᴏʀ ᴀɴʏ ɪꜱꜱᴜᴇꜱ"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("KingX").info("Stopping King Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
