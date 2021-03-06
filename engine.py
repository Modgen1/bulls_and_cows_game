from random import randint

numbers = []


def makeup_number():
    global numbers
    numbers = list()
    numbers.append(randint(1, 9))
    while len(numbers) < 4:
        number = randint(0, 9)
        if number not in numbers:
            numbers.append(number)
    return numbers


def check_number(user_input):
    global numbers
    bulls = 0
    cows = 0
    for index, number in enumerate(numbers):
        if int(user_input[index]) == number:
            bulls += 1
        if int(user_input[index]) in numbers:
            cows += 1
    cows = cows - bulls
    result = [bulls, cows]
    return result


def check_input(user_input):
    conditions = 0
    if user_input[0] != 0:
        conditions += 1
    if len(user_input) == 4:
        conditions += 1
    if user_input[0] != user_input[1:3] and user_input[1] != user_input[2:3] and user_input[2] != user_input[3]:
        conditions += 1
    if conditions == 3:
        return True
    else:
        return False
