import random
from colorama import init
init()
from termcolor import colored


class Interactive():
    def __init__(self, quest, right, ans=[]):
        self.quest = quest
        self.ans = ans
        self.right = right
        self.right_after_testing = ''  # очищенный номер ответа
        self.ans_after_testing = []  # собраны очищ. ответы
        self.right_answers = []  # собраны фактические верн.ответы

    def isint(self, a):
        # проверяем ответ пользователя на число
        try:
            int(a)
            return 'true'
        except ValueError:
            return 'false'

    def color_t(self, text, color, back_color):
        back_color = 'on_' + back_color
        print(colored(text, color, back_color))

    def question(self):
        users_answer = ''

        # наполняем список правильных ответов из ответов
        for i in str(self.right):
            result = self.isint(i)
            if result == 'true':
                i = int(i)
                self.right_after_testing += str(i)
                self.right_answers.append(self.ans[i - 1])
            elif result == 'false':
                pass

        print('========================================================')
        # выводим вопрос наружу
        text = '\n {} \n'.format(self.quest)
        self.color_t(text, 'white', 'blue')
        # print(self.right_answers)

        for i in self.ans:
            # выводим варианты ответов наружу
            if i != '\n':
                text = '{}'.format(i)
                self.color_t(text, 'red', 'green')
                self.ans_after_testing.append(i)
            else:
                pass
        text_insert = '\nВыбери номера ответов, последовательно,'
        text_insert += ' напр. 12 если два верных ответа или 2 если один\n'
        text_insert += 'Введи свой ответ, или answer если хочешь узнать ответ'
        print(text_insert)

        while str(users_answer) != str(self.right_after_testing):
            testing = ''
            # проверяем является ли ответ пользователя числом
            while testing != 'true':
                users_answer = input(
                    '>')
                if users_answer == 'answer':
                    for i in self.right_answers:
                        text = '\nВерный ответ - {}\n'.format(i)
                        self.color_t(text, 'white', 'green')
                        users_answer = 111
                    break
                testing = self.isint(users_answer)
                if testing != 'true':
                    print('Введено ошибочное значение')

            # проверяем введеный пользователем ответ
            if int(users_answer) == int(self.right_after_testing):
                    text = 'Это правильный ответ!'
                    self.color_t(text, 'red', 'green')
            elif users_answer == 111:
                pass
            else:
                text = 'Ответ неверен..'
                self.color_t(text, 'white', 'red')

                with open('wrongs.txt', 'a') as f:
                    f.write('\n {} \n'.format(self.quest))
                    f.write('Правильный ответ: ')
                    for i in self.right_answers:
                        f.write('{}\n'.format(i))
            if users_answer == 111:
                break


intro = 'Кликни правой кнопкой мыши на верхнюю шапку, там где название.\n'
intro += 'Выбери - СВОЙСТВА.\n'
intro += 'Кликни вкладку шрифт и выбери шрифт CONSOLAS\n'
intro += '(или любой который будет читабелен, '
intro += 'в этой же вкладке увидишь как он выглядит.)\n'
intro += 'Размер выбери 16 (или опять более читабельный)\n'
intro += 'Дальше кликни на вкладку РАСПОЛОЖЕНИЕ.\n'
intro += 'Там в области РАЗМЕР ОКНА выбери подходящий\n'
intro += '(например ширину 80 и высоту 30)\n'
intro += 'Все, готово!\n'
intro += 'В данной папке есть два текстовых файла\n'
intro += '1.txt это вопросы. Можно редактировать следуя логике конструкции\n'
intro += 'wrongs.txt это те вопросы на которые ты ошибочно ответил\n'
intro += 'они сохраняются с ответами. Можно редактировать и их все удалять\n'
intro += 'Если заметил какую то ошибку или что то не работает\n'
intro += 'обязательно все запиши, что за ошибка и все ее данные\n'
intro += 'Все, готово!\n'
intro += 'Введи 1 если все сделал и готов начать\n'
begin = input(intro)


active = True
while active:
    ans = []
    quest_ran = ''
    right_ran = ''
    ans_ran = ''
    ran = str(random.randrange(51, 101))
    quest_ran = 'quest' + ran
    right_ran = 'r' + ran + 'right'
    ans_ran = 'a' + ran + 'ans'
    quest = ''
    right = ''
    with open('2.txt', 'r') as f:
        list_text = f.readlines()
        # print(list_text)
    for w in list_text:
        a = ''
        b = ''
        if quest_ran in w:
            a, b, c = w.split('=')
            quest = b
        elif right_ran in w:
            a, b, c = w.split('=')
            right = b
        elif ans_ran in w:
            a, b, c = w.split('=')
            ans.append(b)

    t1 = Interactive(quest, right, ans)
    t1.question()
    continued_answer = input(
        'Если закончить то quit, иначе следующий вопрос: ')
    if continued_answer == 'quit':
        active = False
