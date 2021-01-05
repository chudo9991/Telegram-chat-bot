import telebot
import random
 
bot = telebot.TeleBot("ХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХ") # Ключ от бота
 
score = 0 # Счет равен 0 при запуске
 
# список добрых слов для пользователя
goodword = [
            'Молодец!',
            'У тебя хорошо получается!',
            'Ты уже много знаешь!',
            'Давай ещё!',
            'Ух-ты!',
            'Вот это да!',
            'Отлично!',
            'Умница!',
            'Не останавливайся на достигнутом!',
            'Хорошая работа!',
            'Грандиозно!',
            'Так держать',
            'Впечатляюще!',
            'Браво!',
            'Восхитительно!'
]
 
# В words лежат слова и их перевод. Потом будем брать их другого раздела.
words = {
    'начать' : 'begin began begun', 
    'сломать': 'break broke broken', 
    'купить' : 'buy bought bought',
    'выбрать' : 'choose chose chosen',
    'резать' : 'cut cut cut',
    'делать' : 'do did done',
    'говорить' : 'speak spoke spoken',
    'надевать' : 'wear wore worn',
    'летать' : 'fly flew flown',
    'писать' : 'write wrote written',
    'знать' : 'know knew known',
    'бросать' : 'throw threw thrown',
    'есть' : 'eat ate eaten',
    'прятаться' : 'hide hid hidden',
    'падать' : 'fall fell fallen',
    'давать' : 'give gave given',
    'видеть' : 'see saw seen',
    'брать' : 'take took taken',
    'хранить' : 'keep kept kept',
    'спать' : 'sleep slept slept',
    'чувствовать' : 'feel felt felt',
    'встречать' : 'meet met met',
    'мечтать' : 'dream dreamt dreamt',
    'иметь в виду' : 'mean meant meant',
    'читать' : 'read read read',
    'слышать' : 'hear heard heard',
    'находить' : 'find found found',
    'рассказывать' : 'tell told told',
    'приносить' : 'bring brought brought',
    'покупать' : 'buy bought bought',
    'ловить' : 'catch caught caught',
    'думать' : 'think thought thought',
    'начинать' : 'begin began begun',
    'пить' : 'drink drank drunk',
    'петь' : 'sing sang sung',
    'плавать' : 'swim swam swum',
    'бить' : 'beat beat beaten',
    'становиться' : 'become became become',
    'ломать' : 'break broke broken',
    'строить' : 'build built built',
    'ездить' : 'drive drove driven',
    'прощать' : 'forgive forgave forgiven',
    'замерзать' : 'freeze froze frozen',
    'идти' : 'go went gone'
    }
 
toAsk = list(words.keys()) # спиок слов для вопросов пользователю
 
x = random.randint(0, len(toAsk)-1) # Выбираем случайное слово из словаря
 
@bot.message_handler(commands=['start', 'help']) # Обработчик при запуске бота
def send_welcome(message):
  bot.reply_to (message, "Здравствуйте, я - ваш бот-помощник в изучении неправильных английских глаголов! Напиши /startgame, чтобы начать игру. Если хочешь закончить - /stopgame. Как играть? Я пишу глагол на русском - Вы присылаете три формы на английском через пробел. Если Вы правильно ответили, я дам вам 1 балл")
 
@bot.message_handler(commands=['startgame']) # Обработчик для старта игры
def startgame (message):
      global score
      score = 0 
      bot.send_message(message.from_user.id, "Игра начинается!")
      bot.send_message(message.from_user.id, "Я приготовил " + str(len(toAsk)) + " слов.")
      bot.send_message(message.from_user.id, "Сейчас твой результат " + str(score) + " баллов.") 
      bot.send_message(message.from_user.id, "Напиши команду /next, чтобы получить первое слово.")
 
@bot.message_handler(commands=['next']) # Обработчик для получения следующего слова
def effective (message):
      bot.send_message(message.from_user.id, "Следующий вопрос!")
      bot.send_message(message.from_user.id, "Напиши перевод слова '" + str(toAsk[x]) + "'") # Отправляем пользователю в чат
      
      
@bot.message_handler(func=lambda m: True) # Обработчик для введенных слов
def game(message):
    global x, score
    if len(words)!=0:
        if message.text.lower() == words[toAsk[x]]: # проверяем что ввел пользователь и что загадано
          score = score + 1 # увеличиваем счет на 1
          bot.send_message(message.from_user.id, ""+goodword[random.randint(0,len(goodword)) ] ) # шлем подбадривающие слова
          bot.send_message(message.from_user.id, "Правильно! +1 балл. Всего баллов "+ str(score))
          bot.send_message(message.from_user.id, "Напиши команду /next, чтобы получить следующее слово.")
          toAsk.pop(x) # выкидываем угаданное слово из списка
          bot.send_message(message.from_user.id, "Я знаю ещё " + str(len(toAsk)) + " слов.")
          x = random.randint(0, len(toAsk)-1) # Пользователь отгадал и теперь мы выбираем случайное слово из словаря
        elif message.text == "/stopgame":
          bot.send_message(message.from_user.id, "Игра окончена! Твой результат " + str(score) + " баллов.")
        else:
          bot.send_message(message.from_user.id, "Неправильно! Правильный ответ: "+ str(words[toAsk[x]]))
          bot.send_message(message.from_user.id, "Я загадал новое слово. Пришли /next, чтобы узнать его.")
          x = random.randint(0, len(toAsk)-1) # Пользователь не отгадал и бот взял новое слово. Прислать правильный ответ от старого и заработать балл не получиться.
    else:
      bot.send_message(message.from_user.id, "Игра окончена! Твой результат " + str(score) + " баллов.")
      bot.send_message(message.from_user.id, "Ты идеально знаешь формы неправильных английских глаголов!")
      
bot.polling()