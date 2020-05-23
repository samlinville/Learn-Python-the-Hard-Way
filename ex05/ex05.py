name = 'Sam Linville'
age = 24 # not a lie
height = 69 # inches
weight = 150 # lbs
eyes = 'Hazel'
teeth = 'White'
hair = 'Brown'

metric_height = round(height * 2.54)
metric_weight = round(weight / 2.205)

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"Actually, that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right.
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

print(f"In metric measurements, I am {metric_height} centimeters tall and I weigh {metric_weight} kilograms.")