# Icss - Userbot
# translater for Icss - Userbot
# Owner ~ <@rruuurr>

from telethon.utils import pack_bot_file_id

@asst_cmd("الايدي")
@owner
async def _(e):
    if e.reply_to_msg_id:
        await e.get_input_chat()
        r_msg = await e.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await asst.send_message(
                e.chat_id,
                "Current Chat ID: `{}`\nFrom User ID: `{}`\nBot API File ID: `{}`".format(
                    str(event.chat_id), str(r_msg.sender_id), bot_api_file_id
                ),
            )
        else:
            await asst.send_message(
                e.chat_id,
                "Current Chat ID: `{}`\nFrom User ID: `{}`".format(
                    str(event.chat_id), str(r_msg.sender_id)
                ),
            )
    else:
        await asst.send_message(
            e.chat_id, "Current Chat ID: `{}`".format(str(event.chat_id))
        )