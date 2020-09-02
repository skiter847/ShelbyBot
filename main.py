from pyrogram import Client, filters
import os
import tools

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

app = Client(session_name='session', api_hash=api_hash, api_id=api_id)


@app.on_message(filters.me & filters.reply & filters.command('voice_to_str'))
def voice_to_str_handle(client, message):
    """ in reply message must be contain voice if true, convert voice to text and sends to chat"""
    if message.reply_to_message.voice:
        client.download_media(message.reply_to_message, file_name='voice.ogg')
        voice_text = tools.voice_to_str()
        client.send_message(message.chat.id, ' **Текст**: ' + voice_text)
    else:
        client.send_message(message.chat.id, 'Голосовое сообщение не найдено.')


app.run()
