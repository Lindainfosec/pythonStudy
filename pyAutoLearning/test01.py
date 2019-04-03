def collatz(number):
    while number != 1:
        if number % 2 == 0 and number > 1:
            number = number // 2
            print(number)
        elif number % 2 == 1:
            number =  3 * number + 1
            print(number)
        else:
            print('You are enter the wrong number!!')
            break

while True:
    try:
        number = int(input('pls enter the number:'))
        collatz(number)
    except ValueError:
        print('Error,you must enter a number!!')

