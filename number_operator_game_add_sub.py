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

thresholds = 5
consecutive_correct = 0
level = 1
window_width = 80

success_message = ["YooHooooooo!!!","Rocking!!!","Excellent","Brilliant","You are on a roll","WOW","OH MY GOD"]


while True:
    msg_line1 = f"This is number game."
    msg_line2 = f"You are currently in level {level}."
    msg_line3 = f"Answer {thresholds} consecutive questions correctly to go to next level."
    # msg = msg.format(level,thresholds)
    print("\n" + bcolors.HEADER + "#"*window_width + bcolors.ENDC)
    print(bcolors.HEADER + "#" + f"{msg_line1}".center(window_width-2) + "#" + bcolors.ENDC)
    print(bcolors.HEADER + "#" + f"{msg_line2}".center(window_width-2) + "#" + bcolors.ENDC)
    print(bcolors.HEADER + "#" + f"{msg_line3}".center(window_width-2) + "#" + bcolors.ENDC)
    print(bcolors.HEADER + "#"*window_width + bcolors.ENDC + "\n")
    while(consecutive_correct<thresholds):
        number1 = random.randint(0,99)
        number2 = random.randint(0,9)
        op = random.choice(list(ops.keys()))
        print("-"*window_width)
        print(bcolors.BOLD + f"{number1}".center(window_width) + bcolors.ENDC)
        print(bcolors.BOLD + f"{op} {number2}".center(window_width) + bcolors.ENDC)
        print("-"*window_width)
        print("What will be the answer: ",end='')
        while True:
            try:
                answer = int(input())
            except ValueError:
                print("The entered value is not correct")
                continue
            else:
                break
        correct_answer = ops[op](number1,number2)
        if answer == correct_answer:
            print(bcolors.OKGREEN + f"{random.choice(success_message)}".center(window_width) + bcolors.ENDC)
            consecutive_correct += 1
            if consecutive_correct == thresholds:
                print(bcolors.OKGREEN + f"Congratulations You have answered 5 consecutive questions correctly.".center(window_width) + bcolors.ENDC)
            else:
                print(bcolors.OKGREEN + f"{consecutive_correct}/{thresholds}.. Lets see if you can solve next one".center(window_width) + bcolors.ENDC)
        else:
            print(f"The correct answer is {correct_answer}")
            print(bcolors.FAIL + "You can do better. Reset to 0.".center(window_width) + bcolors.ENDC)
            print(bcolors.FAIL + "Lets try again".center(window_width) + bcolors.ENDC)
            consecutive_correct = 0

    print("Do you want to play again ? To continue, type 'yes' :  ",end="")
    while True:
        try:
            answer = input()
            if "yes" in answer:
                thresholds += 5
                level += 1
                consecutive_correct = 0
                break
            else:
                continue
        except ValueError:
            print("The entered value is not correct")
            continue
        else:
            break
    if "yes" not in answer:
        break
