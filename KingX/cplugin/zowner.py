from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from KingX import app
from KingX.utils.database import add_served_chat_clone, delete_served_chat_clone
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from KingX.utils.database import get_assistant
import asyncio
from KingX.misc import SUDOERS
from KingX.mongo.afkdb import LOGGERS as OWNERS
from KingX.core.userbot import Userbot
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from KingX import app
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from KingX import app
from KingX.utils.Hotty_ban import admin_filter
from KingX.utils.decorators.userbotjoin import UserbotWrapper
from KingX.utils.database import get_assistant, is_active_chat


@Client.on_message(filters.command("repo") & filters.group)
async def repo(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱𝐒 𝐎𝐔𝐑𝐂𝐄 🌱", url=f"https://github.com/KrishnaxMusic/KingX"
                    )
                ]
            ]
        ),
    )


@Client.on_message(filters.command("repo") & filters.group)
async def help(client: Client, message: Message):

    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱 𝐒𝐎𝐔𝐑𝐂𝐄 🌱", url=f"https://github.com/KrishnaxMusic/KingX"
                    )
                ]
            ]
        ),
    )


@Client.on_message(filters.command("repo") & filters.private)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱 𝐒𝐎𝐔𝐑𝐂𝐄 🌱", url=f"https://github.com/KrishnaxMusic/KingX"
                    )
                ]
            ]
        ),
    )


# --------------------------------------------------------------------------------- #


@Client.on_message(
    filters.command(
        ["hi", "hii", "hello", "hui", "good", "gm", "ok", "bye", "welcome", "thanks"],
        prefixes=["/", "!", "%", ",", "", ".", "@", "#"],
    )
    & filters.group
)
async def bot_check(_, message):
    chat_id = message.chat.id
    await add_served_chat_clone(chat_id)


# --------------------------------------------------------------------------------- #


import asyncio
import time


@Client.on_message(filters.command("gadd") & filters.user(int(OWNERS)))
async def add_all(client, message):
    command_parts = message.text.split(" ")
    if len(command_parts) != 2:
        await message.reply(
            "**⚠️ ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ғᴏʀᴍᴀᴛ. ᴘʟᴇᴀsᴇ ᴜsᴇ ʟɪᴋᴇ » `/gadd `**"
        )
        return

    bot_username = command_parts[1]
    try:
        userbot = await get_assistant(message.chat.id)
        bot = await client.get_users(bot_username)
        app_id = bot.id
        done = 0
        failed = 0
        lol = await message.reply("🔄 **ᴀᴅᴅɪɴɢ ɢɪᴠᴇɴ ʙᴏᴛ ɪɴ ᴀʟʟ ᴄʜᴀᴛs!**")

        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == -1002198719573:
                continue
            try:
                await userbot.add_chat_members(dialog.chat.id, app_id)
                done += 1
                await lol.edit(
                    f"**🔂 ᴀᴅᴅɪɴɢ {bot_username}**\n\n**➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅**\n**➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ❌**\n\n**➲ ᴀᴅᴅᴇᴅ ʙʏ»** @{userbot.username}"
                )
            except Exception as e:
                failed += 1
                await lol.edit(
                    f"**🔂 ᴀᴅᴅɪɴɢ {bot_username}**\n\n**➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅**\n**➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ❌**\n\n**➲ ᴀᴅᴅɪɴɢ ʙʏ»** @{userbot.username}"
                )
            await asyncio.sleep(3)  # Adjust sleep time based on rate limits

        await lol.edit(
            f"**➻ {bot_username} ʙᴏᴛ ᴀᴅᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ🎉**\n\n**➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅**\n**➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ❌**\n\n**➲ ᴀᴅᴅᴇᴅ ʙʏ»** @{userbot.username}"
        )
    except Exception as e:
        await message.reply(f"Error: {str(e)}")
