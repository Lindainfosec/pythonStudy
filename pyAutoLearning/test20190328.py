def hello():
    print('hello01')
    print('hello02')
    print('hello03')

hello()
#

#
import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'test01'
    elif answerNumber == 2:
        return 'test02'
    elif answerNumber == 3:
        return 'test03'
    elif answerNumber == 4:
        return 'test04'
    elif answerNumber == 5:
        return 'test05'
    elif answerNumber == 6:
        return 'test06'
    elif answerNumber == 7:
        return 'test07'
    elif answerNumber == 8:
        return 'test08'
    elif answerNumber == 9:
        return 'test09'

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)
#

print('1','2','3','4',sep='-')
#sep可以用来定义输出的内容之间的间隔字符


#关于错误异常的处理
def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('erro,invaild argument')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))


# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break    # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))

#

#输出一个值，循环的输出，直到最后输出1,需要加入try except
# def collatz(number):
#         if number % 2 == 0:
#             number = number // 2
#             print(number)
#         elif number % 2 == 1:
#             number = 3 * number + 1
#             print(number)
# number = int(input('input a numbe:'))

def collatz(number):
    while number != 1:
        if number % 2 == 0 and number > 1:
            number = number // 2
            print(number)
        elif number % 2 == 1:
            number = 3 * number + 1
            print(number)
        else:
            print('You are enter the wrong number!!')
            break

while True:
    try:
        shu = int(input('pls enter the number:'))
        collatz(shu)
    except ValueError:
        print('Error,you must enter a number!!')
