#Introduction
print("Hello! Welcome to the bible quiz by Meleane")

#Input 
name = input("Enter your Name: ")
print("Welcome {}!".format(name))
print("\n")

score = 0

# QUESTION 1
q1 = input("1. In what city was Jesus Born?\na) Nazareth \nb) Bethlehem \nc) Gethsamane \nd) Egypt\nAnswer: ")

#If-and-else statements
if q1 =="b" or q1 =="Bethlehem":
    score += 1 
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer is b. Bethlehem")
    print("Score: ", score)
    print("\n")

# QUESTION 2
q2 = input("2. After Jesus was arrested, which apostle disowned him three time?\na) Judas Iscariot \nb) John \nc) Thomas \nd) Peter\nAnswer: ")

if q2 =="d" or q2 =="Peter":
    score += 1 
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer is d. Peter")
    print("Score: ", score)
    print("\n")

# QUESTION 3
q3 = input("3. How many books are there in the old testament?\na) 27 \nb) 40 \nc) 38 \nd) 39\nAnswer: ")

if q3 =="d" or q3 =="39":
    score += 1 
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer is d. 39")
    print("Score: ", score)
    print("\n")

# QUESTION 4
q4 = input("4. What is the shortest book in the New Testament?\na) 1 John \nb) 2 John \nc) 3 John\nAnswer: ")

if q4 =="b" or q4 =="2 John":
    score += 1 
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer is b. 2 John")
    print("Score: ", score)
    print("\n")

# QUESTION 5
q5 = input("5. Who is the author of the book of Revelation?\na) John \nb) Joseph \nc) Paul \nd) Timothy\nAnswer: ")

if q5 =="a" or q5 =="John":
    score += 1 
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer is a. John")
    print("Score: ", score)
    print("\n")

# QUESTION 6
q6 = input("6. What language was most of the Old Testament originally written in?\na) Greek \nb) Hebrew \nc) Latin \nd) Aramaic\nAnswer: ")

if q6 =="b" or q6 =="Hebrew":
    score += 1 
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer is b. Hebrew")
    print("Score: ", score)
    print("\n")

# QUESTION 7
q7 = input("Matthew was a _______?\na) Tax Collector \nb) Fisherman \nc) Carpenter \nd) Murderer\nAnswer: ")

if q7 =="a" or q7 =="Tax Collector":
    score += 1 
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer is a. Tax Collector")
    print("Score: ", score)
    print("\n")

# QUESTION 8
q8 = input("Why did God put a mark on Cain?\na) To curse him \nb) To shame him \nc) To protect him \nd) To mark him for slaughter\nAnswer: ")

if q8 =="c" or q8 =="To protect him":
    score += 1 
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer is c. To protect him")
    print("Score: ", score)
    print("\n")

# QUESTION 9
q9 = input("Name the place where Jesus walked on water?\na) Sea of Galilee \nb) Jordan River \nc) The Red Sea\nAnswer: ")

if q9 =="a" or q9 =="Sea of Galilee":
    score += 1 
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer is a. Sea of Galilee")
    print("Score: ", score)
    print("\n")

# QUESTION 10
q10 = input("Which book did Jesus directly write?\na) Matthew \nb) Mark \nc) Luke \nd) John \ne) None\nAnswer: ")

if q9 =="e" or q9 =="none" or q9 =="None":
    score += 1 
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! The answer is e. None")
    print("Score: ", score)
    print("\n")

# FINAL MESSAGE
if score <= 5:
    print ("Your total score is:", score, "- Not bad!")
elif score == 8:
    print("Your total score is:", score, "- Well done!")
else:
    print("Your total score is", score, "- You are awesome!")