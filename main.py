import asyncio
import os

from telethon import TelegramClient, events

"""
docs:
- https://github.com/LonamiWebs/Telethon
- https://docs.telethon.dev/en/stable/index.html

this setup uses a sqlite data store:
# apk add sqlite
# sqlite3 /jkr.session
# > .tables
# > select * from entities;
# > .quit
"""

api_id = os.environ["API_ID"]
api_hash = os.environ["API_HASH"]
client = TelegramClient("jkr", api_id, api_hash)


# handle @lkmex_egld_trade_bot (LKMEX - EGLD) bot
@client.on(events.NewMessage(incoming=True, chats="@lkmex_egld_trade_bot"))
async def handler(event):
    if event.text == "Type the amount you'd like to swap:":
        await event.reply("1000000")
    if event.text.startswith("For 1,000,000.000 LKMEX tokens you will get:"):
        rate = float(event.text.split(" ")[7])
        print(f"1m LKMEX = {rate:.3f} EGLD")


# handle @lkmex_trade_bot (LKMEX - MEX) bot
@client.on(events.NewMessage(incoming=True, chats="@lkmex_trade_bot"))
async def handler(event):
    if event.text == "Type the amount you'd like to swap:":
        await event.reply("1")
    if event.text.startswith("For 1.000 LKMEX tokens you will get:"):
        rate = float(event.text.split(" ")[7])
        print(f"1 LKMEX = {rate:.3f} MEX")


async def main():
    await client.start()
    # get data
    await client.send_message("@lkmex_egld_trade_bot", "/quote")
    await client.send_message("@lkmex_trade_bot", "/quote")
    await asyncio.sleep(2) # wait 2s for bots to reply
    # cleanup
    async for message in client.iter_messages("@lkmex_egld_trade_bot"):
        await client.delete_messages("@lkmex_egld_trade_bot", message.id)
    async for message in client.iter_messages("@lkmex_trade_bot"):
        await client.delete_messages("@lkmex_trade_bot", message.id)

asyncio.run(main())
