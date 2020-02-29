from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

updater = Updater('1059616795:AAGP3EVSZhQ8dUiorByqRiy9fJ-fRteyySU', use_context=True)



logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = 'Вызван / start'
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
     user_text = "Приветствую тебя, {}! Твое последнее сообщение было: {}".format(update.message.chat.first_name, update.message.text)
     logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username, update.message.chat.id, update.message.text)
     update.message.reply_text(user_text)

def compliment(bot, update):
     nice_reply = '{}, сегодня ты выглядишь просто потрясающе'.format(update.message.chat.first_name, update.message.text)
     logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username, update.message.chat.id, update.message.text)
     update.message.reply_text(nice_reply)

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
   
    logging.info("Бот запускается")

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(MessageHandler(Filters.text, compliment))
   
    mybot.start_polling()
    mybot.idle()

main ()