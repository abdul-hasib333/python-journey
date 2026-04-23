# Day 3: My first conditional program

age = input("How old are you? ")
age_number = int(age)

if age_number >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

if age_number >= 65:
    print("You qualify for a senior discount.")
elif age_number >= 18:
    print("You pay the standard price.")
else:
    print("You pay the child price.")            