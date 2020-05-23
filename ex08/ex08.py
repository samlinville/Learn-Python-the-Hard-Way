formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "So if you care to find me,",
    "Look to the western sky!",
    "As someone told me lately,",
    "Everyone deserves the chance to fly!"
))