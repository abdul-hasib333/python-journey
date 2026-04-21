#Day 2: Varisbles, inputs and Basic Math

name = input("What is your name?  ")
age = input("How Old are you?")

age_number = int(age)
years_until_30 = 30 - age_number

print("Hello " + name + "!")
print("You will be 30 in" + str(years_until_30) + "years.")
