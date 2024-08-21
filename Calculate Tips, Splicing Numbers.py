import random


''' Base Level: Finding Minimum'''
#
print('Kameron Ibraheem')
print('Base Level: Finding Minimum')

n1 = random.randrange(1, 101)
n2 = random.randrange(1, 101)
n3 = random.randrange(1, 101)

print(f'The computer generated {n1}, {n2}, {n3}')
minimum = n1
if n2 < minimum:
    minimum = n2
if n3 < minimum:
    minimum = n3
print(f'The smallest value is {minimum}')




'''Base Level: Parse into Digits'''
#
print()
print('Base Level: Parse into Digits')

rand_num = random.randrange(1000, 10001)

print(f'The computer generated the number {rand_num}')

thous = rand_num // 1000
hund = (rand_num % 1000) // 100
tens = (rand_num % 100) // 10
ones = rand_num % 10

print(f'The 1000s digit is {thous}, the 100s digit is {hund}, the 10s digit is {tens}, The 1s digit is {ones}')





''' Level Up: Calculate the Tip '''
#
print()
print('Level Up: Calculate the Tip')

dollars = random.randrange(10, 201)
cents = random.randrange(100)

bill = dollars + (cents / 100)
tip = bill * .20
total = tip + bill

#print(f"The computer generated ${dollars}.{cents:02d}")
print(f'The computer generated {dollars}, {cents}')
print(f'The bill is ${dollars}.{cents}')

#print(f"The bill is ${bill:.2f}")
print(f"The tip is ${tip:.2f}")
print(f"The total is ${total:.2f}")




'''Level Up: Determine Max Tax Bracket'''
#
print()
print('Level Up: Determine Max Tax Bracket')
inc = random.randrange(50000, 60001)
#inc = 215951

print(f'The income is ${inc}')

if inc <= 10275:
    tax = 10
elif inc < 41775:
    tax = 12
elif inc <= 89075:
    tax = 22
elif inc < 170050:
    tax = 24
elif inc <= 215950:
    tax = 32
elif inc < 539900:
    tax = 35
else:
    tax = 37

print(f'{tax} is the highest rate that a portion of the income will be taxed')
