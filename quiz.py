#Introduction
print("Hello! Welcome to the bible quiz by Meleane")

q1 = input("1. In what city was Jesus Born?\na) Nazareth \nb) Bethlehem \nc) Gethsamane \nd) Egypt\n>> ")

if q1 == "a" or q1 == "Nazareth":
    print("Incorrect")
elif q1 == "b" or q1 == "Bethlehem":
    print("Correct")
elif q1 == "c" or "Gethsamane":
    print("Incorrect")
elif q1 == "d" or "Egypt":
    print("Incorrect")
else:
    print("That is not an option")

