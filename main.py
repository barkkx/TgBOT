from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import os
from dotenv import load_dotenv
load_dotenv()



TOKEN = os.getenv("TOKEN")
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

ZODIACS = {
    'овен': 'Сегодня день для решительных действий! Вас ждёт успех.',
    'телец': 'Проведите день спокойно, подумайте о будущем. Хороший день для планирования.',
    'близнецы': 'Будьте осторожны с новыми знакомыми, не все они искренни.',
    'рак': 'Сегодня удачный день для улучшения отношений с близкими.',
    'лев': 'Постарайтесь избежать конфликтов на работе, они могут затянуться.',
    'дева': 'Сегодня удачный день для финансовых вложений и покупок.',
    'весы': 'Возможно, вам придется принять важное решение, доверьтесь интуиции.',
    'скорпион': 'Не бойтесь рисковать сегодня, это принесет свои плоды.',
    'стрелец': 'Сегодня отличный день для путешествий и новых впечатлений.',
    'козерог': 'Уделите внимание здоровью, не перегружайте себя на работе.',
    'водолей': 'Вы найдете решение проблемы, которая давно вас беспокоит.',
    'рыбы': 'Сегодня вас ждет приятный сюрприз от близкого человека.'
}

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет, введи свой знак чтобы получить предсказание!")


def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Введи свой знак зодиака чтобы получить предсказание')


def zodiac_prediction(update, context):
    user_sign = update.message.text.lower()
    if user_sign in ZODIACS:
        prediction = ZODIACS[user_sign]
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'Предсказание на сегодня для знака {user_sign}: {prediction}')

    else:
        zodiac_sign = ZODIACS.keys()
        zodiac_list = ", ".join(zodiac_sign)
        context.bot.send_message(chat_id=update.effective_chat.id, 
                            text=f'Введите доступный знак: {zodiac_list}')
    


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

zodiac_handler = MessageHandler(Filters.text & (~Filters.command), zodiac_prediction)
dispatcher.add_handler(zodiac_handler)

updater.start_polling()