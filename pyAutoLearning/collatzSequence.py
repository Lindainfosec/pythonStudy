#2019年3月29日16:00
# def collatz(n):
#     print(n)
#     if n % 2 == 1 and n > 1:
#         collatz(3*n + 1)
#     elif n % 2 == 0:
#         collatz(n // 2)
#
# if __name__ == '__main__':
#     n = input('Enter a number: ')
#     n = int(n)
#     collatz(n)

#https://segmentfault.com/q/1010000006713803
# Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1.
#
# Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1. (Amazingly enough, this sequence actually works for any integer—sooner or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why. Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”)
#
# Remember to convert the return value from input() to an integer with the int() function; otherwise, it will be a string value.
#
# Hint: An integer number is even if number % 2 == 0, and it’s odd if number % 2 == 1.
#
# The output of this program could look something like this:
#
#
# Enter number:
# 3
# 10
# 5
# 16
# 8
# 4
# 2
# 1
# Add try and except statements to the previous project to detect whether the user types in a noninteger string. Normally, the int() function will raise a ValueError error if it is passed a noninteger string, as in int('puppy'). In the except clause, print a message to the user saying they must enter an integer.

def collatz(n):
    if n % 2 == 0:
        print(n // 2)
        return n // 2
    elif n % 2 == 1:
        print(3 * n + 1)
        return 3 * n + 1

while True:
    try:
        number = input('Enter an int number: ')
        while int(number) != 1:
            number = int(collatz(int(number)))
        if number == 1:
            break
    except ValueError:
        print('must be an int number! ')
    continue


# def collatz(number):
#     while number != 1:
#         if number % 2 == 0 and number > 1:
#             number = number // 2
#             print(number)
#         elif number % 2 == 1:
#             number = 3 * number + 1
#             print(number)
#         else:
#             print('You are enter the wrong number!!')
#             break
#
# while True:
#     try:
#         shu = int(input('pls enter the number:'))
#         collatz(shu)
#     except ValueError:
#         print('Error,you must enter a number!!')

