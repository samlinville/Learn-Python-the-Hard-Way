from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

gross = input("What's your least favorite fruit?")

print("This script is called:", script)
print("Your favorite fruit is", first)
print("Your second favorite fruit is", second)
print("Your third favorite fruit is", third)
print("Your least favorite fruit is", gross)

print(f"So that's pretty cool! Your favorite is {first} and your least favorite is {gross}.")

