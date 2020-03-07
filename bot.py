from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem

from datetime import date

updater = Updater(settings.API_KEY, use_context=True)

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = 'Вызван / start'
    logging.info(text)
    update.message.reply_text(text)

def position_recognition(bot, update):
    today = date.today().strftime("%Y/%m/%d")
    planet_name = update.message.text.split()
    planet = getattr(ephem, planet_name[1])(today)
    print(planet)
    update.message.reply_text(f'Созвездие: {ephem.constellation(planet)[-1]}')



def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
   
    logging.info("Бот запускается")

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", position_recognition))
   
    mybot.start_polling()
    mybot.idle()

main ()