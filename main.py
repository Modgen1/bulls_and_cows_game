from engine import makeup_number, check_number, check_input

while True:
    makeup_number()
    turns_quantity = 0
    while True:
        while True:
            user_input = input('Введите число:')
            if check_input(user_input):
                result = check_number(user_input)
                print('Быки -', result[0], 'коровы -', result[1])
                break
            print('Вы ввели неправильное число!')
        turns_quantity += 1
        if result[0] == 4:
            print('Вы угадали число, количество ходов -', turns_quantity)
            user_wanna_play = input('Хотите заново сыграть?')
            break
    if user_wanna_play != 'да' and user_wanna_play != 'Да':
        break
