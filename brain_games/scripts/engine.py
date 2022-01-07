#!/usr/bin/env python3
import prompt
import random
import operator
import math


def welcome(task_text):
    global name
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    greeting = '{}, {}!'.format('Hello', name)
    print(greeting)
    print(task_text)
    return name


def question(task):
    global answer
    print('Question: ' + str(task))
    answer = prompt.string('You answer: ')
    return answer


def random_numbers():
    global random_number_from_1_to_100
    global random_number_from_1_to_49
    global random_number_from_50_to_1000
    global random_number_from_0_to_9
    global random_number_fom_2_to_6
    random_number_from_1_to_100 = random.randrange(1, 101)
    random_number_from_1_to_49 = random.randrange(1, 50)
    random_number_from_50_to_1000 = random.randrange(50, 1001)
    random_number_from_0_to_9 = random.randrange(0, 10)
    random_number_fom_2_to_6 = random.randrange(2, 7)
    return random_number_from_0_to_9
    return random_number_from_1_to_100
    return random_number_from_1_to_49
    return random_number_from_50_to_1000
    return random_number_fom_2_to_6


def random_operator():
    global str_operator
    global int_operator
    operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
    str_operator, int_operator = random.choice(operators)
    return str_operator, int_operator


def gcd(number_one, number_two):
    return math.gcd(number_one, number_two)


def is_prime(task):
    diviser = 2
    if task <= 1:
        return False
    while task % diviser != 0:
        diviser += 1
    return task == diviser
