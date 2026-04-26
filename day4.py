# Day 4: My first loops

# A while loop - runs until a condition is no longer true
count = 1
while count <= 5:
    print("Count is " + str(count))
    count = count + 1

print("_ _ _")


# A for loop - runs a set number of times
for number in range (1, 6):
    print("Number is " + str(number))

print("_ _ _")

# A for loop over a list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print("I like " + fruit)