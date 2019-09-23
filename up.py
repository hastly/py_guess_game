import random

secret = random.randint(1, 101)
print(f"secret: {secret}")  # TODO: remove upon debug is finished

while 1:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        continue
    if guess > secret:
        print("Too big")
    elif guess < secret:
        print("Too small")
    else:
        print("You win!")
        break
