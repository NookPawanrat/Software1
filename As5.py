#As 5, List structures and iterative loops (for)

#1
import random
numFromRoll = []
numDice = int(input("How many dice to roll?: "))
rollTimes = 0
numEachDice = 0
while rollTimes != numDice:
    numEachDice = random.randint(1,6)
    numFromRoll.append(numEachDice)
    rollTimes = rollTimes + 1
print("The numbers from rolling is ",numFromRoll)
totalSum = 0
for i in numFromRoll:
    totalSum = totalSum + i
print("The total sum is",totalSum)


#2
print()
numList = []
num = input("Enter the numbers 1-10 or ENTER to quit: ")
numList.append(num)
while num != "":
    print(num)
    num = input("Enter the numbers or ENTER to quit: ")
    numList.append(num)
numList.sort(reverse=True)
print("The five greatest numbers is",numList[0:5])


#3
print()
num = int(input("Enter the integer number: "))
result = True
for i in range(2,num-1):
    if (num % i) == 0:
        result = False
if num == 1:
    result = False

if result == False:
    print(num, "is not a prime")
elif result == True:
    print(num,"is a prime")


#4
print()
citiesList = []
recheck = True
Name = str(input("Enter the name of city:"))
if len(Name) <= 1:
    recheck = False
    print("Please enter the name of the city.")
if recheck == True:
    citiesList.append(Name)
    for i in range(4):
        Name = str(input("Enter the name of city:"))
        citiesList.append(Name)
    for citiesName in citiesList:
        print(citiesName)








