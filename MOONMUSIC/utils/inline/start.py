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
            InlineKeyboardButton(text="⚡🅗ᴇʟᴘ⚡", callback_data="settings_back_helper"),
            InlineKeyboardButton(
                text="🅢ᴇᴛ", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="⚡🅖ʀᴏᴜᴘ⚡", url=config.SUPPORT_CHAT),
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
            InlineKeyboardButton(text="⚡🅖ʀᴏᴜᴘ⚡", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="⚡🅤ᴘᴅᴀᴛᴇs⚡", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text="⚡ғᴇᴀᴛᴜʀᴇs⚡ ", callback_data="settings_back_helper")
        ],
    ]
    return buttons
