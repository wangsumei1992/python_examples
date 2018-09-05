import random
import sys
max = 100
min = 1
MAX = 5

while True:
    target_number = random.randint(1, 100)
    #用户尝试的次数
    times = 0
    print('I am thinking of a number between 1 and 100')

    while True:
        if times == MAX:
            sys.exit('Game over, the correct number is %s' % target_number)
        while True:
            guess_number = 0
            user_input = input("take a guess or enter 'q' to quit\n")
            if user_input.strip().lower() == 'q':
                sys.exit('Goodbye')
            if user_input.isdigit():
                guess_number = int(user_input)
                break
            else:
                print('invalid input')

        if guess_number > target_number:
            print("Your guess is too high")
            times = times + 1
        elif guess_number < target_number:
            print("Your guess is too low.")
            times = times + 1
        else:
            print("Good job, the correct number is %s" % target_number)
            break

