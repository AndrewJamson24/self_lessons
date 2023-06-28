import telebot
import CustomErrors
import command_history
import response_validator

command_history.create_table_db()

API_KEY = ''

bot = telebot.TeleBot(API_KEY)

bot.set_my_commands([
    telebot.types.BotCommand("/start", "Рассказывает о боте"),
    telebot.types.BotCommand("/help", "примеры для поиска"),
    telebot.types.BotCommand("/low", "Сортирует рецепты  блюд по нарастающему количеству калорий"),
    telebot.types.BotCommand("/high", "Сортирует рецепты  блюд по уменьшающийся количеству калорий"),
    telebot.types.BotCommand("/custom", "Можете дать определенный диапазон калорий"),
    telebot.types.BotCommand("/history", "Показывает историю поиска последних 10 запросов")
])

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, """Добро пожаловать в поисковик блюд , выберите свой метод поиска:\n
команда /low - Ищет блюда и сортирует по нарастающему количеству калорий\n
команда /high - Ищет блюда и сортирует по уменьшающийся количеству калорий\n
команда /custom - Можете дать определенный диапазон калорий в блюде\n
команда /history - Показывает историю поиска последних 10 запросов
    """)
@bot.message_handler(commands=['low'])
def low(message):
    msg = bot.send_message(message.chat.id, "Введите блюда ко которому вы хотите поиска рецептов , число рецептов и приблизительное число калорий")
    bot.register_next_step_handler(msg, response, call_from='low')


def response(message, call_from):
    try:

        if message.text.startswith('/'):
            raise CustomErrors.Double_Commands

        result = response_validator.request_validator(message.text, call_from=call_from)
        list_message = message.text.split()
        if result is None:
            message = bot.send_message(message.chat.id, "Вы не ввели по примеру по пробуйте еще раз")
            bot.register_next_step_handler(message, response, call_from=call_from)
        else:
            command_history.insert_entry(user_data=message.from_user.username, search_data=list_message)
            keys = result[:int(list_message[1])]
            result = result[int(list_message[1]):]
            for key in keys:
                image_caption = f'{result[0][str(key)]["title"]}\n' \
                                f'calories: {key} '
                bot.send_photo(chat_id=message.chat.id, photo=result[0][str(key)]['image'],caption=image_caption)

    except CustomErrors.Double_Commands:
        bot.send_message(message.chat.id, "Вы ввель две комманды надо было ввесть деталь блюда и ккал "
                                                    "выберите комманду сново")
    except IndexError:
        message = bot.send_message(message.chat.id, "Блюда не найдено по пробуйте другое блюдо")
        bot.register_next_step_handler(message, response, call_from=call_from)



@bot.message_handler(commands=['high'])
def high(message):
    msg = bot.send_message(message.chat.id,
                           """Введите блюда ко которому вы хотите поиска рецептов , число рецептов и приблизительное число калорий """)
    bot.register_next_step_handler(msg, response, call_from='high')

@bot.message_handler(commands=['custom'])
def custom(message):
    msg = bot.send_message(message.chat.id, "Введите блюда ко которому вы хотите поиска рецептов , число рецептов и "
                                            "приблизительное число максимальных калорий калорий и минимальных калорий" )
    bot.register_next_step_handler(msg, response, call_from='custom')
@bot.message_handler(commands=['history'])
def history(message):
    history_tuple= command_history.get_history(name=message.from_user.username)
    response_string = ""
    for count, entry in enumerate(history_tuple):
        response_string += str(count + 1)+'. ' +entry[1] + ' '+entry[2]+' '+entry[3]+' '+entry[4] +'\n'
    bot.send_message(message.chat.id, response_string)

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, """примеры для поиска\n
    /low  \npasta 5 400\n
    /high \nbeans 6 500\n
    /custom \nbbq 10 400 900""")

@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(message):
    bot.send_message(message.chat.id, "Я не понимаю \"" + message.text + "\"\nпо пробуйте одну из комманд в меню")

bot.infinity_polling()

