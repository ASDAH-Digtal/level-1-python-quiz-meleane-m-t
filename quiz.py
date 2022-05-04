#Introduction
print("Hello! Welcome to the bible quiz by Meleane")

name = input("Enter your Name: ")
print("Welcome {}!".format(name))

q1 = input("1. In what city was Jesus Born?\na) Nazareth \nb) Bethlehem \nc) Gethsamane \nd) Egypt\n>> ")

if q1 == "a" or q1 == "Nazareth":
    print("Incorrect")
elif q1 == "b" or q1 == "Bethlehem":
    print("Correct")
elif q1 == "c" or q1 == "Gethsamane":
    print("Incorrect")
elif q1 == "d" or q1 == "Egypt":
    print("Incorrect")
else:
    print("That is not an option")

q2 = input("2. After Jesus was arrested, which apostle disowned him three time?\na) Judas Iscariot \nb) John \nc) Thomas \nd) Peter\n>> ")

if q2 == "a" or q2 == "Judas Iscariot":
    print("Incorrect")
elif q2 == "b" or q2 == "John":
    print("Incorrect")
elif q2 == "c" or q2 == "Thomas":
    print("Incorrect")
elif q2 == "d" or q2 == "Peter":
    print("Correct")
else:
    print("That is not an option")

q3 = input("3. How many books are there in the old testament?\na) 27 \nb) 40 \nc) 38 \nd) 39\n>> ")

if q2 == "a" or q3 == "27":
    print("Incorrect")
elif q3 == "b" or q3 == "40":
    print("Incorrect")
elif q3 == "c" or q3 == "38":
    print("Incorrect")
elif q3 == "d" or q3 == "39":
    print("Correct")
else:
    print("That is not an option")