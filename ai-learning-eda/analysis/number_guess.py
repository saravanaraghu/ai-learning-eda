import numpy as np


def choose_difficulty():
    while True:
        level = input("Enter difficulty (E = Easy, M = Medium, H = Hard): ").upper()

        if level == "E":
            return 10
        elif level == "M":
            return 6
        elif level == "H":
            return 4
        else:
            print("Invalid input. Please enter E, M, or H.")


difficult = choose_difficulty()
rand_int = np.random.randint(1, 101)
print("\nGuess the number between 1 and 100")
count = 0
flag = False
while difficult > 0:
    count += 1
    dummy_int = int(input("Tell the Guesses"))
    if dummy_int == rand_int:
        flag = True
        break
    elif dummy_int > rand_int:
        print("Guess smaller ones")
        difficult -= 1
    else:
        print("Guess bigger ones")
        difficult -= 1
if flag:
    print("You made it in {} Guesses!!".format(count))
else:
    print(f"\n❌ You lost! The number was {rand_int}")
