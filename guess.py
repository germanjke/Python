import random

a = False
user = None
number_start = None
number_end = None
i = 0
guess_limit = None
while guess_limit is None:
    try:
        guess_limit = abs(int(input("How many guess do you want: ")))
        if guess_limit == 0:
            print('You only have one chance since you put 0')
            guess_limit = 1
    except ValueError:
            print('You only have one')
            guess_limit = 1
while i == 0:
    while number_start is None and number_end is None:
        try:
            number_start = int(input("From which number do you want to start: "))
            number_end = int(input("From which number do you want to end: "))
        except ValueError:
            print("Pick a number")
    if number_start == number_end or number_start > number_end:
        print("The first number must be higher than the second number")
        number_start = None
        number_end = None
    else:
        i += 1
        computer = int(random.randrange(number_start, number_end, ))
        x = 0
        print("You should chose numbers from " + str(number_start) + " to " + str(number_end) + " : ")
        while x == 0:
            while guess_limit != 0:
                user = None
                while user is None:
                    try:
                        user = int(input("Pick your number: "))
                    except ValueError:
                        a = True
                    if a:
                        print('Pls answer with a number')
                        user = None
                        a = False
                    else:
                        if user == computer:
                            print("YEAH YOU GOT IT")
                            x += 1
                            guess_limit = 0
                        elif number_start <= user <= number_end and user > computer:
                            print("THE SYSTEM CHOSE LOWER NUMBER")
                            guess_limit -= 1
                            print("You have " + str(guess_limit) + " more")
                        elif number_start <= user <= number_end and user < computer:
                            print("THE SYSTEM CHOSE HIGHER NUMBER")
                            guess_limit -= 1
                            print("You have " + str(guess_limit) + " more")
                        elif user > number_end or user < number_start:
                            print("Pick a number between " + str(number_start) + "-" + str(number_end))
                            guess_limit -= 1
                            print("You have " + str(guess_limit) + " more")
            if guess_limit == 0 and x == 0:
                print("You lost the game")
                break
            else:
                print("You won the game")
            break