import random
answer = random.randint(1, 100)
guess=0
while guess!=answer:
    guess = int(input('guess='))
    print('Your guess is', guess)
    if guess == answer :
        print('Good guess')
    elif guess < answer:
        print('Too low')
    else:
        print('Too high')