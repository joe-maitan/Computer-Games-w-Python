import random 

print("Hello! What is your name?")
user_name = input()

lo = 1
hi = 20
random_number = random.randint(lo, hi)

print(f"Hello {user_name}. I am thinking of a number between {lo} and {hi}.")

for num_guesses in range(6):
    print(f"Take a guess --- {6 - num_guesses} tries remaining")
    guess = int(input())

    if guess < random_number:
        print("Your guess is too low.")
    elif guess > random_number:
        print("Your guess is too high.")
    elif guess == random_number:
        break

if guess == random_number:
    print(f"Good job, {user_name}! You guessed my number in {num_guesses} guesses!")
elif guess != random_number:
    print(f"Nope.  The number I was thinking of was {random_number}")