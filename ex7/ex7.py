print("Mary had a little lamb.") # print a string
print("Its fleece was white as {}.".format('snow')) # print a string with an empty variable slot wit the formattted string "snow" added into the empty slot.
print("And everywhere that Mary went.") # print a string
print("." * 10) # print a string ten times in a row

end1 = "C" # set variable equal to a string
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. Try removing it and see what happens.
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ') # print each variable after the other (they're all strings), set the end character to a space (will not go to a new line)
print(end7 + end8 + end9 + end10 + end11 + end12, end=' ') # same as line 20
print("is so good!") # print a string (will be on the previous line since the previous end character was not a newline.)