# import the argv module
from sys import argv

# add argv parameters to two variables
script, filename = argv

# open the file passed through the filename argv, store it in the txt variable
txt = open(filename)

# print some text with the filename variable
print(f"Here's your file {filename}:")
# "read" the contents of the file in the txt variable and print it
print(txt.read())

#
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt.close()
txt_again.close()