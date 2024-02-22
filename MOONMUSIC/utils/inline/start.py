from pyrogram.types import InlineKeyboardButton

import config
from MOONMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="⚡ʜᴇʟᴘ⚡", callback_data="settings_back_helper"),
            InlineKeyboardButton(
                text="sᴇᴛ", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="⚡ɢʀᴏᴜᴘ⚡", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="⚡ɢʀᴏᴜᴘ⚡", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="⚡ᴜᴘᴅᴀᴛᴇs⚡", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text="⚡ғᴇᴀᴛᴜʀᴇs⚡ ", callback_data="settings_back_helper")
        ],
    ]
    return buttons
