import random

choice = input("Choose a number: ")
choice = int(choice)
gen_number = random.randint(1, 6)
if choice == gen_number:
    print("You win!")
else:
    print("You lose!")

print("The number was:", gen_number)
