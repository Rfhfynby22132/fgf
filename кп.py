import telebot

bot = telebot.TeleBot("7771898758:AAEDE-EqrqGzr_eFiojNe3al4H2X7WIPZiw")

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')


@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(commads=["bye"])
def send_bye(message):
    bot.reply_to(message, "Пока👋! Удачи👋!")


@bot.message_handler(fun=lambda message :True)
def echo_all(message):
    bot.reply_to(message, message.text)

def is_api_group(chat_id):
    return chat_id == GROUP_CHAT_ID
@bot.message_handler(func=lambda m: True, content_types=['new_chat_participant'])
def on_user_joins(message):
    if not is_api_group(message.chat.id):
        return


bot.polling()
