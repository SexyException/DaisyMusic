import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from MOONMUSIC import LOGGER, app, userbot
from MOONMUSIC.core.call import MOON
from MOONMUSIC.misc import sudo
from MOONMUSIC.plugins import ALL_MODULES
from MOONMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(name).error("Session String toh Phle Laga Le Bhai😆")
        
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
        importlib.import_module("MOONMUSIC.plugins" + all_module)
    LOGGER("MOONMUSIC.plugins").info("ALL ARE LOADED...")
    await userbot.start()
    await MOON.start()
    await MOON.decorators()
    LOGGER("MOONMUSIC").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  ᴍᴀᴅᴇᴇ ʙʏ ᴇxᴄᴇᴘᴛɪᴏɴ ♨\n╚═════ஜ۩۞۩ஜ════╝"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("MOONMUSIC").info("╔═════ஜ۩۞۩ஜ════╗\n  ♨ᴍᴀᴅᴇ ʙᴛ ᴇxᴄᴇᴘᴛɪᴏɴ\n╚═════ஜ۩۞۩ஜ════╝")
    

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
