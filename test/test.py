import random

# tries = 10
random_number = str(random.randrange(1, 10, 2))
tries = int(input('Enter the count of tries'))
while tries > 0:
        input_number = (input('Enter the number between 0 and 10'))
        if input_number > random_number:
            tries -= 1
            print('The number is lower then' + input_number)
            continue
        elif input_number < random_number:
            tries -= 1
            print('The number is higher then' + input_number)
            continue
        elif input_number == random_number:
            print('Bingo! the number is' + random_number)
        break
