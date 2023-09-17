#Assignment 7 -Tuple, set, and dictionary

#1
season =[]
season.append(("winter",12,1,2))
season.append(("spring",3,4,5))
season.append(("summer",6,7,8))
season.append(("autumn",9,10,11))
#print(season)
def checkSeason(numMonth):
    if numMonth in season[0]:
        print(f"The month {numMonth} is winter.")
    elif numMonth in season[1]:
        print(f"The month {numMonth} is spring.")
    elif numMonth in season[2]:
        print(f"The month {numMonth} is summer.")
    elif numMonth in season[3]:
        print(f"The month {numMonth} is autumn.")
    else:
        print("Sorry,Please the number of the months (1-12)")

while True:
    numMonth = int(input("Enter the number of the months (1-12) or negative number to quit: "))
    if numMonth in range(1,13):
        checkSeason(numMonth)
    elif numMonth < 0:
        print("Goodbye")
        break
    else:
        print("Sorry,Please enter the number of the months (1-12)or negative number to quit: ")



#2
nameset = set([])
while True:
    name = input("Enter name: ")
    if name != "":
        if name not in nameset:
            nameset.add(name)
            print(f'{name} is a new name, {name} added.')
        else:
            print(f'{name} is a existing name.')
    else:
        print("End the program")
        break
print('Here is the list of the name:')
for i,name in enumerate(nameset):
    print(i+1,name)



#3
data = {
    "EFHK" : "Helsinki-Vantaa Airport",
    "VTBS" : "Suvarnabhumi Airport",
    "RJTT" : "Haneda Airport"
}

print("Choose the option you want to do\n" 
      "1.Add a new airport\n"
      "2.Fetch the information of an existing airport\n"
      "3.Quit")
while True:
    choose = input("Choose the number of option: ")
    if choose == "1":
        print("1.Add a new airport")
        code = input("Enter the new ICAO code: ")
        airport = input("Enter the new airport name: ")
        if code in data.keys() or airport in data.values():
            if code in data.keys():
                print(f"Code {code} is already exit")
            elif airport in data.values():
                print(f"Name {airport} is already exit")
        else:
            data.update({code:airport})
            print(f'ICAO code: {code} Name: {airport}\nAdded')
    elif choose == "2":
        print("2.Fetch the information of an existing airport")
        inputCode = input("Enter the ICAO code: ")
        print(f"Code {inputCode} is {data[inputCode]}")
    elif choose == "3":
        print("3.Quit")
        print("End program")
        break



