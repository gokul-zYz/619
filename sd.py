import telebot
from pytube import YouTube


#print('TOKEN:', TOKEN)
bot = telebot.TeleBot('5455229767:AAFq-tl0UkmbyFkw-lzPTYMQLWoS2MoLmUc')


@bot.message_handler(commands=['ytdl'])
def test(message):
    link=message.text.split(" ")
    print(link[1])
    youtubeObject = YouTube(link[1])
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(filename="1.mp4")
    except:
        print("An error has occurred")
    print("Download is completed successfully")
    #send video function
    chat_id=message.chat.id
    file_path = '1.mp4'
    bot.send_video(chat_id, video=open(file_path, 'rb'))
    bot.send_message(chat_id,"Sending videos...")
   
@bot.message_handler(func=lambda message: True and message.text=='raja')
def echo_message(message):
    print(message)
    chat_id=message.chat.id
    message_text = message.text
    bot.send_message(chat_id, f"You said: {message_text}")
@bot.message_handler(func=lambda message: True and str(message.text).upper()=='SUBA')
def echo_message(message):
    chat_id=message.chat.id
    message_text = message.text
    bot.send_message(chat_id, "Suba Is Very Gud Girl💕")
            
bot.polling()