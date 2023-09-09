#Assignment 4 - While loops (while)

#1
numbers = 1
while numbers <= 1000:
    if numbers % 3 == 0:
        print(numbers)
    numbers = numbers + 1

#2
print()
inches = float(input("Enter how much inches: "))
centimeters = float(inches * 5.08)
while inches >= 0:
    print(inches, "inches =", centimeters, "centimeters")
    inches = float(input("Enter how much inches: "))

#3
print()
numInput = input("Enter the numbers: ")
numHighest = float(numInput)
numLowest = float(numInput)
while numInput != " ":
    numInput = float(numInput)
    if numInput > numHighest:
        numHighest = numInput
    if numInput < numLowest:
        numLowest = numInput
    numInput = (input("Enter the numbers: "))
else:
    print("Quit")
    print("The largest number is ",numHighest)
    print("The lowest number is ",numLowest)

#4
print()
import random
correctAnswer = random.randint(1,10)
guess = int(input("Guess the number between 1-10: "))
while guess != correctAnswer:
    if guess > correctAnswer:
        print("Too high")
    elif guess < correctAnswer:
        print("Too low")
    guess = int(input("Guess the number between 1-10: "))
else:
    print("Correct")

#5
print()
username = input("Username: ")
password = input("Password: ")
correctUsername = "python"
correctPassword = "rules"
loginTimes = 1
while username != correctUsername or password != correctPassword:
    if loginTimes == 5:
        print("Access denied")
        break
    print("Please enter the username and password again")
    username = input("Username: ")
    password = input("Password: ")
    loginTimes = loginTimes + 1
else:
    print("Welcome")

#6
print()
import random
numPoint = int(input("How many random point to generate?:"))
generatePoint = 0
numTotalCircleA = 0
while generatePoint != numPoint:
    xPoint = int(random.randint(-10 ,10))
    yPoint = int(random.randint(-10 ,10))
    generatePoint = generatePoint + 1
    print(xPoint , yPoint )
    if xPoint^2 + yPoint^2 < 1:
        print('(', xPoint, ',', yPoint, ') this point is fall inside circle A')
        numTotalCircleA = numTotalCircleA + 1
N = int(numPoint)
n = int(numTotalCircleA)
print("The total number of random points is ",N ,"\n"
      "The total number of points that fall inside circle A is", n)
pi = float(4 * n / N)
print('The approximation of pi is ', pi)







