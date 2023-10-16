#Assignment 8 - Using relational databases

#1

import mysql.connector
def get_code(code):
    sql = "SELECT  name ,municipality FROM airport"
    sql += " WHERE ident='" + code + "'"
#    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        return result[0]
    else:
        print("Sorry we could not found it!")

# Main program
connection = mysql.connector.connect(
        host ='127.0.0.1',
        port = 3306,
        database='flight_game',
        user='Nook',
        password='nook1996',
        autocommit = True
         )

code = input("Enter the ICAO code of an airport: ")
result = get_code(code)
if result:
    print(f'The airport name is {result[0]}')
    print(f'The town is {result[1]}')


#2
import mysql.connector
def get_airport(area):
    sql = "SELECT  name ,type FROM airport"
    sql += " WHERE iso_country='" + area + "'"
    sql += "ORDER BY TYPE DESC"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(row)

# Main program
connection = mysql.connector.connect(
        host ='127.0.0.1',
        port = 3306,
        database='flight_game',
        user='Nook',
        password='nook1996',
        autocommit = True
         )
area = input("Enter the area code: ")
get_airport(area)


#3
import mysql.connector
import geopy.distance
def get_location(code):
    sql = "SELECT  latitude_deg , longitude_deg FROM airport"
    sql += " WHERE ident ='" + code + "'"
#    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        return result[0]
    else:
        print("Sorry we could not found it!")

# Main program
connection = mysql.connector.connect(
        host ='127.0.0.1',
        port = 3306,
        database='flight_game',
        user='Nook',
        password='nook1996',
        autocommit = True
         )

time = 0
location = []
while time < 2:
    code = input("Enter the ICAO codes of two airports: ")
    result = get_location(code)
    if result:
        time += 1
        location.append(code)
        location.append(result[0])
        location.append(result[1])

#print(location)
location_1 = (location[1], location[2])
location_2 = (location[4], location[5])

print(f"Distance between {location[0]} and {location[3]} is {geopy.distance.geodesic(location_1, location_2).km} km.")



