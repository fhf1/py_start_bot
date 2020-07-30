# Импорты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings


# Глобальные настройки
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='py_start_bot.log'
                    )


# Функции
def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
    logging.info("User: %s, Chat_id: %s, Message: %s", update.message.chat.first_name,
                update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)


# Коннектимся к платформе Telegram, тело нашего бота
def main():
    my_bot = Updater(settings.API_KEY)

    logging.info('Бот запускается')

    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    my_bot.start_polling()
    my_bot.idle()

main()
