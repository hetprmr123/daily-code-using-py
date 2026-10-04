import random

jackport = random.randint(1,100)  #using random module to generate a random number between 1 to 100
guess = int(input("guess the numberbetween 1 to 100 "))
counter=1   #counter variable to count the number of attemps

while jackport != guess:
    if guess < jackport:
        print("guess higher ")
    else:
        print("guess lower ")
        
    guess = int(input("guess the number "))
    counter+=1
        
print("your guess Is correct!")
print("you guess the correct number In",counter,"attemp!")