types_of_people = 10 # sets the variable types_of_people equal to 10
x = f"There are {types_of_people} types of people." # sets the variable x equal to the string "There are {types_of_people} types of people." inserting the value in place of the variable types_of_people

binary = "binary" # sets the variable binary equal to the string "binary"
do_not = "don't" # sets the variable do_not equal to the string "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x) # prints the variable x, whose value is a string
print(y) # prints the variable y, whose value is a string

print(f"I said: '{x}'") # prints the string "I said: {x}" with the value in place of the variable x
print(f"I also said: '{y}'") # prints the string "I also said: {y}" with the value in place of the variable y

hilarious = "I mean, kinda..." # sets the variable hilarious to a Boolean value of False
joke_evaluation = "Isn't that joke so funny?! {}" # sets the variable joke_evaluation equal to the string "Isn't that joke so funny?! {}" with an empty variable slot

print(joke_evaluation.format(hilarious)) # prints the variable joke_evaluation, whose value is a string, formatting the empty variable slot to display the value of the variable hilarious

w = "This is the left side of..." # sets the variable w equal to the string "This is the left side of..."
e = "a string with a right side." # sets the variable e equal to the string "A string with a ride side..."

print(w + e) #prints the variable w, whose value is a string, and then prints the variable e, whose value is a string.