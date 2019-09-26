from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler,
                          ConversationHandler)
from handlers import *
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

logger = logging.getLogger(__name__)


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():

    updater = Updater("833230157:AAHFAMDwUJpPnaH7YbgjiJNGZs234GGg5PU", use_context=True)

    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            START: [MessageHandler(Filters.regex('^(/start)$'), start)],

            KATO: [MessageHandler(Filters.regex('^(Kategoriler)$'), kato)],



        },

        fallbacks=[CommandHandler('main_menu_keyboard', main_menu_keyboard)]
    )

    dp.add_handler(conv_handler)
    dp.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    dp.add_handler(CallbackQueryHandler(bir_menu, pattern='m1')),
    dp.add_handler(CallbackQueryHandler(iki_menu, pattern='m2')),
    dp.add_handler(CallbackQueryHandler(uc_menu, pattern='m3'))
    dp.add_handler(CallbackQueryHandler(dort_menu, pattern='m4'))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()