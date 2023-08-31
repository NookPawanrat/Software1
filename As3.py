#Assignment 3 - Conditional structures (if)

#1
print()
zanderLength = int(input("Enter the zander's length in centimeters: "))
belowSizeLimit = 42 - zanderLength

if zanderLength < 42:
    print("Please release the fish back into the lake, This fish is", belowSizeLimit,
          "centimeters below the size limit.")
else:
    print("The fish is fulfill the size limit.")

#2
print()
cabinClass = str(input("Please enter your cabin class: "))

if cabinClass == "LUX":
    print("Upper-deck cabin with a balcony.")
elif cabinClass == "A":
    print("Above the car deck, equipped with a window.")
elif cabinClass == "B":
    print("Windowless cabin above the car deck.")
elif cabinClass == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")

#3
print()
gender = str(input("What's your the biological gender (female/male): "))
hemonglobin = int(input("What's your hemoglobin value(g/l):"))

if gender == "female":
    if 117 <= hemonglobin <= 155:
        print("You have normal hemoglobin value for adult females.")
    elif hemonglobin > 155:
        print("You have high hemoglobin value for adult females.")
    elif hemonglobin < 117:
        print("You have low hemoglobin value for adult females.")
if gender == "male":
    if 134 <= hemonglobin <= 167:
        print("You have normal hemoglobin value for adult males.")
    elif hemonglobin > 167:
        print("You have high hemoglobin value for adult males.")
    elif hemonglobin < 134:
        print("You have low hemoglobin value for adult males.")

#4
print()
year = int(input("Please enter a year: "))
if year % 4 == 0:
    print(year, "is a leap year.")
elif year % 100 == 0 and year % 400 == 0:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
