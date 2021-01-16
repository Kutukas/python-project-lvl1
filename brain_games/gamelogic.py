import prompt
import random


def is_even(number):
    #return 'yes' if a number is even and 'no' if odd
    if (number % 2) == 0:
        return 'yes'
    return 'no'


def game_is_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    cac = 0 # cac - correct answer counter
    while cac < 3:
        random_number = random.randrange(99)
        print('Question: {}'.format(random_number))
        answer = prompt.string('Your answer: ')
        correct_answer = is_even(random_number)
        if correct_answer == answer:
            print('Correct!')
            cac += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answer, correct_answer))
            print("Let's try again, {}!".format(name))
            break
    else:
        print('Congratulations, {}!'.format(name))

