#Introduction
print("Hello! Welcome to the bible quiz by Meleane")

name = input("Enter your Name: ")
print("Welcome {}".format(name))

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

q2 = input("2. After Jesus was arrested, which apostle disowned him three time?\na) Judas Iscariot \nb) John \nc) Thomas \nd) Peter\n>> ")

if q2 == "a" or q1 == "Judas Iscariot":
    print("Incorrect")
elif q1 == "b" or q1 == "John":
    print("Incorrect")
elif q1 == "c" or "Thomas":
    print("Incorrect")
elif q1 == "d" or "Peter":
    print("Correct")
else:
    print("That is not an option")