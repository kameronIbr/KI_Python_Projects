import random
print('Kameron Ibraheem')
print('You have 3 attempts to guess a random number between 1 and 20')

number = random.randrange(1,21)

guess = int(input('Guess a number: '))

if guess == number:
    print('Congratualtions!')

else:
    guess2 = int(input('Wrong, Guess a number: '))
    if guess2 != number:
            guess3 = int(input('Wrong, Guess a number: '))
            if guess3 == number:
                print('Congratulations!')
            else:
                    print('Wrong!')
    else:
        print('Congratulations!')

print('Your number: ', number)

print()
print('Code Using While Loops')
print('You have 3 attempts to guess a random number between 1 and 20')

range_num = random.randrange(1, 21)

n = 2

guess = int(input('Enter a guess: '))

while n>0 and guess !=range_num:
    guess = int(input('Wrong, Guess Again: '))
    n = n - 1
if guess == range_num:
    print('Congratualtions!')
else:
    print('Wrong, You have Lost.')
    print(f'The Number was {range_num}')
