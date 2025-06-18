import random

# defining  the guessing game function
def guessing():
    guess_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    random_output = random.choice(guess_numbers)

    if random_output == input('Enter a number: '):
        print(random_output, ' Correct!')
    else:
        print(random_output, ' Try again')

guessing()