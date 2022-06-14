#!/usr/bin/python3

import random
import operator

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

ops = { "+": operator.add,
        "-": operator.sub }
        
consecutive_correct = 0
msg = "Lets See if you can solve this"
success_message = ["YooHooooooo!!!","Rocking!!!","Excellent","Brilliant","You are on a roll","WOW","OH MY GOD"]

print(bcolors.HEADER + f"{msg}".center(50) + bcolors.ENDC)
while(consecutive_correct<5):
    number1 = random.randint(0,99)
    number2 = random.randint(0,9)
    op = random.choice(list(ops.keys()))
    print("-"*50)
    print(bcolors.BOLD + f"{number1}".center(50) + bcolors.ENDC)
    print(bcolors.BOLD + f"{op} {number2}".center(50) + bcolors.ENDC)
    print("-"*50)
    print("What will be the answer: ",end='')
    answer = int(input())
    correct_answer = ops[op](number1,number2)
    print(answer,correct_answer)
    if answer == correct_answer:
        print(bcolors.OKGREEN + f"{random.choice(success_message)}".center(50) + bcolors.ENDC)
        if consecutive_correct == 5:
            print(bcolors.OKGREEN + f"Congratulations You have answered 5 consecutive questions correctly.".center(50) + bcolors.ENDC)
        else:
            print(bcolors.OKGREEN + "Lets see if you can solve next one".center(50) + bcolors.ENDC)
        consecutive_correct += 1
    else:
        print(bcolors.FAIL + "You can do better".center(50) + bcolors.ENDC)
        print(bcolors.FAIL + "Lets try again".center(50) + bcolors.ENDC)
        consecutive_correct = 0
    if consecutive_correct == 5:
        print(bcolors.OKGREEN + f"Congratulations You have answered 5 consecutive questions correctly.".center(50) + bcolors.ENDC)
