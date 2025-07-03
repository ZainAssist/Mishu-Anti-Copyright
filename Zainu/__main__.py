import asyncio
import importlib
from pyrogram import idle
from Zainu import Zainu
from Zainu.modules import ALL_MODULES

LOGGER_ID = -1001283805612

loop = asyncio.get_event_loop()

async def JARVIS():
    for all_module in ALL_MODULES:
        importlib.import_module("Zainu.modules." + all_module)
    print("Bot Started Successfully")
    await idle()
    print("MAI HU PIRO CODER BOLO NHI AAYA ERROR")
    await Zainu.send_message(LOGGER_ID, "**ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ ʏᴏᴜʀ ʙᴏᴛ ᴅᴇᴘʟᴏʏᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ✅ \n ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ  [ZAIN](https://t.me/Uff_Zainu)**")

if __name__ == "__main__":
    loop.run_until_complete(JARVIS())
    
