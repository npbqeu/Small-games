import random

choice = input("Choose a number: ")
choice = int(choice)
gen_number = random.randint(1, 100)
for x in range(8):
    if choice == gen_number:
        print("Great job!")
    elif choice < gen_number:
        print("Higher!")
        choice = input("Choose a new number: ")
        choice = int(choice)
    elif choice > gen_number:
        print("Lower!")
        choice = input("Choose a new number: ")
        choice = int(choice)
if choice != gen_number:
    print("You ran out of tries! Try again!")
