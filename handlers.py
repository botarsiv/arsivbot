import telegram
from message import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


STARTS = range(1)


def start(update, context):
    chat_id = update.message.chat_id
    name = str(update.message.from_user.first_name)
    text = "CAADBAADJwADhEa6Gq0m-NvEsdVGFgQ"
    text2 = "<b>Merhaba!</b>"
    keyboard = [['Kategoriler', 'Sohbet'],
                ['İletişim', 'Açıklama']]
    reply_markup = telegram.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    context.bot.send_document(chat_id, text)
    context.bot.send_message(chat_id, text2, reply_markup=reply_markup, parse_mode='html')
    context.bot.send_message(chat_id, name)
    return STARTS



def starts(update, context):
    update.message.reply_text(main_menu_message(),
                              reply_markup=main_menu_keyboard())


def main_menu_keyboard():
    markup = InlineKeyboardButton
    keyboard = [[markup('Grup Yönetimi', callback_data='m1'), markup('Müzik', callback_data='m2')],
                [markup('Oyun', callback_data='m3'), markup('Türkçe Botlar', callback_data='m4')]]
    return telegram.InlineKeyboardMarkup(keyboard)




############################ Buton #########################################
def main_menu(update, context):
    query = update.callback_query
    context.bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=main_menu_message(),
                          reply_markup=main_menu_keyboard())



def bir_menu(update, context):
    query = update.callback_query
    context.bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=bir_menu_message(),
                          reply_markup=bir_menu_keyboard())


def iki_menu(update, context):
    query = update.callback_query
    context.bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=iki_menu_message(),
                          reply_markup=iki_menu_keyboard())


def uc_menu(update, context):
    query = update.callback_query
    context.bot.edit_message_text(chat_id=query.message.chat_id,
                                  message_id=query.message.message_id,
                                  text=uc_menu_message(),
                                  reply_markup=uc_menu_keyboard())


def dort_menu(update, context):
    query = update.callback_query
    context.bot.edit_message_text(chat_id=query.message.chat_id,
                                  message_id=query.message.message_id,
                                  text=dort_menu_message(),
                                  reply_markup=dort_menu_keyboard())



############################ Buton #########################################


def bir_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Geri', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def iki_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Geri', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def uc_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Geri', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def dort_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Geri', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)

