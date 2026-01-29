import random

x = random.randint(1, 101)
print(f'The number is {x}')
guess_string = input('Guess a number between 1 - 100: ')
guess = int(guess_string)
guess_distance = abs(x - guess)

if guess < 1 or guess > 100:
    print('OUT OF BOUNDS!')
elif guess == x:
    print('You guessed correctly! It only took you one try!')
elif guess_distance <= 10:
    print('WARM')
else:
    print('COLD')

counter = 1

while x != guess:
    old_guess_distance = abs(guess - x)
    guess_string = input('Guess a number between 1 - 100: ')
    guess = int(guess_string)
    guess_distance = abs(guess - x)     
    counter += 1
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS!')
    elif guess == x:
        print(f'You guessed correctly! It only took you {counter} tries!')
    elif guess_distance <= old_guess_distance:
        print('WARMER')
    else:
        print('COLDER')

