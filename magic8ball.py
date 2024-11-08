import random
question = input("Ask the Magic 8 Ball a question.")
answer = random.randint(1, 8)
if answer == 1:
    print("It is certain.")
elif answer == 2:
    print("Outlook good.")
elif answer ==  3:
    print("You may rely on it.")
elif answer == 4:
    print("Ask again later.")
elif answer == 5:
    print("Concentrate and ask again.")
elif answer == 6:
    print("You will die.")
elif answer == 7:
    print("My sources say no.")
else: 
    print("That's not a question.")
print("The end.")
