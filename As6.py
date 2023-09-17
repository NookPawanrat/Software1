#As6 - Functions

#1

import random
def randomDice():
    dice = random.randint(1,6)
    print(f"Result is {dice} ")
    return dice

#Main program
result = 0
ready = True
while ready == True:
    result = randomDice()
    if result == 6:
        print("You got 6, Congratulations!")
        break
    else:
        ready = False
        print("Sorry,The result is not 6.")
        ans = input("Do you want to try again (yes/no): ")
        if ans == "yes":
            ready = True
        else:
            print("Goodbye")
            break


#2

import random
def randomDice(numSide):
    dice = random.randint(1,numSide)
    print(f"Result is {dice} ")
    return dice

#Main program
numSide = int(input("How many sides on the dice do you want?: "))
result = 0
while result != numSide:
        result = randomDice(numSide)
        if result == numSide:
            print(f"You got {numSide}, Congratulations!")
            break
        else:
            print(f"This is not the maximum, Roll again")

#3

def convert(gallon):
    litres = gallon * 3.78541178
    return litres

#Main Program
while True:
    print("Input the positive number converted to litres OR input negative number to quit. ")
    gallon = float(input("How many gallon of gasoline?: "))
    if gallon > 0 :
        litres = convert(gallon)
        print(f'{gallon} gallon(US) = {litres} litre')
    elif gallon < 0 :
        print("Goodbye")
        break


#4

def sum(list):
    sum = 0
    for num in list:
        sum += num
    return sum

list =[]
while len(list) < 5:
    inputNum = int(input("Input 5 numbers into the list: "))
    list.append(inputNum)
print(f'The sum is {sum(list)}')



#5

def removeOddnum(numlist):
    if numlist % 2 == 0:
        return False

newlist = []
list =[]

while len(list) < 5:
    inputNum = int(input("Input numbers into the list: "))
    list.append(inputNum)

result = True
for i in list:
    result = removeOddnum(i)
    if result == False:
        newlist.append(i)
print(f"Original list = {list}")
print(f"Cut-down list = {newlist}")



#6

from math import pi
def calculate(size,price):
    m = size * 0.01
#    print(m)
    area = (pi*m*m)/4
#    print(area)
    result = price/area
    return result

size1 = float(input("Enter the diameter of 1st pizza (centimeters): "))
price1 = float(input("Enter the price of 1st pizza (euros): "))
size2 = float(input("Enter the diameter of 2nd pizza (centimeters): "))
price2 = float(input("Enter the price of 2nd pizza (euros): "))

pizza1 = calculate(size1,price1)
pizza2 = calculate(size2,price2)
print(f'The 1st pizza, 1 square meter = {pizza1:.2f} euros')
print(f'The 2nd pizza, 1 square meter = {pizza2:.2f} euros')

while True:
    if pizza1 < pizza2:
        print(f'the 1st pizza provides better value for money than the 2nd pizza')
    elif pizza2 == pizza1:
        print(f'Both of them provides the same value for money')
    else:
        print(f'the 2nd pizza provides better value for money than the 1st pizza')
    break

