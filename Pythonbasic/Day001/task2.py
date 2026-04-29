print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    total = 15
elif size == "M":
    total = 20
elif size == "L":
    total = 25
else:
    total = 0

if pepperoni == "Y" and size == "S":
    total += 2
elif pepperoni == "Y" and (size == "M" or size == "L"):
    total += 3

if extra_cheese == "Y":
    total += 1

print(f"Your final bill is: {total}")

