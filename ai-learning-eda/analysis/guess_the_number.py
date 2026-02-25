import numpy as np

x = np.random.randint(10)

z = True

print("Guess number between 0 to 10")

while(z):
    y = int(input("Enter a number to guess"))
    
    if(y==x):
        print("Your guess is correct")
        z=False
    elif(y>x):
        print("Your guess is huge bro")
    else:
        print("Your guess is short bro")
