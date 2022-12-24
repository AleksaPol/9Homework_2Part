import telebot
token = '5861258570:AAG2p0n2p4YG_uLrWqvwST1bM5N7G3CMUcE'
bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['start', 'help', 'hi'])
def send_welcome(message):
    log(message)
    bot.reply_to(message, "Как дела?")


@ bot.message_handler(content_types=["text", "sticker", "pinned_message", "photo", "audio"])
def function_name(message):
    log(message)
    hello = ['привет', 'здравствуйте', 'здарова', 'добрый день', 'здрасьте']
    for h in hello:
        if h in message.text:
            bot.reply_to(message, f'{message.from_user.first_name}, привет!')
            break


def log(message):
    file = open('db.csv', encoding='utf-8', mode='a')
    file.write(
        f'{message.from_user.first_name},{message.from_user.id},{message.text}\n')
    file.close()


bot.infinity_polling()
