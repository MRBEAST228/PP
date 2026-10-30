import random
import datetime
import time
import json

date_time = datetime.datetime.now()
name = input('Как тебя зовут? ')
print(f' Привет {name}')
while True:

    print('1 - Find out time')
    print('2 - Find out date')
    print('3 - Calculator')
    print('4 - Magic ball')
    print('5 - R.P.S')
    print('6 - Guess the number')
    print('7 - multiplication table')
    print('8 - hacker time')
    print('9 - who want to be a millionaire')
    print('10 - notes')
    print('11 - Random Password')
    print('0 - Exit')
    ch = int(input('how can I help you? '))
    if ch == 1:
        print(date_time.time())
        time.sleep(2)
    elif ch == 2:
        print(date_time.date())
        time.sleep(2)
    elif ch == 3:
        number1 = int(input('ведите первое число или цифру'))
        number2 = int(input('ведите второе число или цифру'))

        print("сумма", number1 + number2)

        print("разность", number1 - number2)

        print("произведение", number1 * number2)

        print("частное", number1 / number2)
        time.sleep(2)
    elif ch == 4:
        print(f'привет {name} хочешь узнать грядущее')
        input('задай вопрос')
        Magic_ansewers = ['спроси друга', 'скорее всего', 'да', 'нет']
        num = random.randint(0, len(Magic_ansewers) - 1)
        print(Magic_ansewers[num])
        time.sleep(2)
    elif ch == 5:
        list = ['Камень', "Ножницы", "Бумага"]
        print("Добро пожаловать в игру Камень-Ножницы-Бумага")
        print("выберете один из вринтов:")
        print(f' 1 - {list[0]} \n 2 - {list[1]} \n 3 - {list[2]}')
        user = int(input('ваш выбор (Введите число от 1-3"): '))
        user = list[user - 1]
        print('ваш выбор: ' + user)
        time.sleep(1)
        bot = random.randint(1, 3)
        bot = list[bot - 1]
        print('выбор бота : ' + bot)
        time.sleep(1)
        if user == bot:
            print('Ничия :|')
            time.sleep(2)
        elif (user == "Камень" and bot == 'Ножницы') or \
                (user == "Ножницы" and bot == 'бумага') or \
                (user == "бумага" and bot == 'Камень'):
            print('Победа :)!')
            time.sleep(2)
        else:
            print('Проигрыш :(')
            time.sleep(2)
    elif ch == 6:
        number = random.randint(0, 100)
        while True:
            guess = int(input('угадай число от 0 до 100'))
            if guess > number:
                print('Слишком большое число, попробуйте еще раз')
            elif guess < number:
                print('Слишком маленькое число, попробуйте еще раз')
            else:
                print('Поздравляю! Вы угадали число')
                time.sleep(2)
                break
    elif ch == 7:
        for num1 in range(1, 11):
            for num2 in range(1, 11):
                print(f'{num1}*{num2} = {num1}*{num2}')
            print('-----------------')
        time.sleep(2)
    elif ch == 8:


        actions = ['взламываю apple', 'скачиваю пин-код илонмаска', 'примеменяю enetiti-404',
                   'включаю режим BlockTerminator',
                   'завершаю взлом Трампа', 'актватия режима AlienTerminator', 'включяю мод дваичный-преаразователь',
                   'дваичный код инопланетян вычеслен',
                   'включяю мод дваичнытерминатор', 'взлом иноплонетян завершон']
        for action in actions:
            print(action + random.choice(['⍻', '☒']))
            time.sleep(random.randint(1, 2))
    elif ch == 9:

        questions = {'Who is on 10 place in rich?': {
            'A': 'Ilon mask',
            'B': 'Rock',
            'C': 'Mr Beast',
            'D': 'Mark Rober'},
            'What is the most popular aviacompany?': {
                'A': 'Aeroflot',
                'B': 'Wizzair',
                'C': 'Emirates',
                'D': 'Flyone'},
            'how many teslas were made in 2024?': {
                'A': '2.22mln',
                'B': '2.17mln',
                'C': '1.29mln',
                'D': '1.77mln'}}
        correct_answers = {'Who is on 10 place in rich?': 'C',
                           'What is the most popular aviacompany?': 'C',
                           'how many teslas were made in 2024?': 'D', }
        money = 0
        lvl = 1
        for question, answers in questions.items():
            print(question)
            for num, ans in answers.items():
                print(f'{num}: {ans}')
            answers = input('Your answer: ')
            if answers == correct_answers[question]:
                print(f'Correct!')
                money += 100000 * lvl
                print(f'You answed {money}')
            else:
                print(f'Incorrect!')
                break
            lvl += 1
    elif ch == 10:



        def save_notes():
            with open('notes.json', 'w') as file:
                json.dump(notes, file)


        def update_notes():
            global notes
            with open('notes.json', 'r') as file:
                notes = json.load(file)


        notes = dict()


        def add_note(tittle, text):
            global notes
            notes[tittle] = text
            print('note is added')


        def display_notes():
            update_notes()
            if len(notes) < 1:
                print('no notes added')
            else:
                for tittle, text in notes.items():
                    print(f'{tittle}: {text}')


        def delete_note(tittle):
            if tittle in notes.keys():
                del notes[tittle]
                print(f'note {tittle} is deleted')
            else:
                print(f'note {tittle} is not found')


        def main():
            while True:
                print('1 add a note')
                print('2 see all notes')
                print('3 delete a note')
                print('4 exit')
                choice = input('Enter your choice: ')
                if choice == '1':
                    note_name = input('Enter note title: ')
                    note_text = input('Enter note text: ')
                    add_note(note_name, note_text)
                    save_notes()
                elif choice == "2":
                    display_notes()
                    save_notes()
                elif choice == '3':
                    update_notes()
                    for tittle in notes.keys():
                        print(tittle)
                    tittle_to_delete = input('Enter tittle to delete: ')
                    delete_note(tittle_to_delete)
                    save_notes()
                elif choice == '4':
                    break
                else:
                    print('Invalid choice!Try again!')


        main()
    elif ch == 11:

        low_Lett = 'abcdefghijklmnopqrstuvwxyz'
        up_lett = low_Lett.upper()
        chars = '!@#$%^&*()'
        didits = '1234567890'
        num = int(input('Enter a length of the password: '))
        password = ''
        for i in range(num):
            random_type = random.randint(1, 4)
            if random_type == 1:
                random_letter = random.choice(low_Lett)
                password += random_letter
            if random_type == 2:
                random_letter = random.choice(up_lett)
                password += random_letter
            if random_type == 3:
                random_char = random.choice(chars)
                password += random_char
            if random_type == 4:
                random_didit = random.choice(didits)
                password += random_didit
        print(password)
        time.sleep(2)


    elif ch == 0:
        break
    else:
        print('Something went wrong. please try again')