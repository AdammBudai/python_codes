'''
The task is to create a program that, given a database of weather information over a particular period in different cities,
displays the required detail information. The input database is stored in a file whose name is passed to the program as the first parameter. 
Requests to display information are passed on standard input in the form of simple commands.

Database
The database will be saved in a JSON file. 
The file will have the correct format, the dates will not contain errors, the individual dates are sorted in the ascending order for each city. 
You can use the standard JSON library to load it. The file format is as follows:


'''








#!/usr/bin/env python3
import json
import sys

data=json.load(open(sys.argv[1]))

def thp(function,city, date):

    temp_city = city.split(':')[1]
    temp_date = date.split(':')[1]

    if temp_date not in data[temp_city]:
        print('Invalid input')
        return

    temp_function = function
    if function == 'humidity':
        temp_function = 'relhum'
    elif function == 'pressure':
        temp_function = 'ap'

    value = data[temp_city][temp_date][temp_function]
    if function == 'humidity':
        value = (round(100*data[temp_city][temp_date][temp_function]))
    
    print(f'{city} {date} {function}:{value}')
    

def maxim(function,city,start_date,end_date):
    temp_function = function.split('max')[1]
    temp_function_2 = function.split('max')[1]
    
    if temp_function == 'humidity':
        temp_function = 'relhum'
    elif temp_function == 'pressure':
        temp_function = 'ap'

    stats = []
    keys = []
    temp_city = city.split(':')[1]
    temp_startdate = start_date.split(':')[1]
    temp_enddate = end_date.split(':')[1]

    if temp_startdate not in data[temp_city] or temp_enddate not in data[temp_city]:
        print('Invalid input')
        return
    
    for date,values in data[temp_city].items():
        if date >= temp_startdate and date <= temp_enddate:
            stats.append(values[temp_function])
            keys.append(date)
    stat = max(stats)
    if temp_function_2 == 'humidity':
        print(f'{city} date:{keys[stats.index(stat)]} {temp_function_2}:{round(stat*100)}')
    else:

        print(f'{city} date:{keys[stats.index(stat)]} {temp_function_2}:{stat}')



def topcity(function,date):
    temp_date = date.split(':')[1]

    cities = []
    for key, value in data.items():
        cities.append(key)

        if temp_date not in data[key]:
            print('Invalid input')
            return
        
    temperatures = []
    for i in cities:
        temperatures.append(data[i][temp_date]['temp'])

    if function == 'warmestcity':
        ind = temperatures.index(max(temperatures))
        city = cities[ind]
        print(f'city:{city} {date} temp:{max(temperatures)}')

    elif function == 'coldestcity':
        ind = temperatures.index(min(temperatures))
        city = cities[ind]
        print(f'city:{city} {date} temp:{min(temperatures)}')




def graph(typ,city, startdate, enddate):
    stats = []
    columns = []
    city = city.split(':')[1]
    temp_startdate = startdate.split(':')[1]
    temp_enddate = enddate.split(':')[1]
    typ = typ.split('h')[1]

    if temp_startdate not in data[city] or temp_enddate not in data[city]:
        print('Invalid input')
        return
    elif typ == 'humidity':
        print('Invalid input')
        return
    

    if typ == 'pressure':
        typ = 'ap'

    for date,hodnoty in data[city].items():
        if date >= temp_startdate and date <= temp_enddate:
            stats.append(hodnoty[typ])

    if len(stats) > 50:
        curr = 0
        M = len(stats)
        for i in range(M % 50):
            avg = 0
            for j in range((M // 50) + 1):
                avg += stats[curr]
                curr += 1
            columns.append(avg / ((M // 50) + 1))

        while len(columns) != 50:
            avg = 0
            for j in range(M // 50):
                avg += stats[curr]
                curr += 1
            columns.append(avg / (M // 50))
    else:
        columns = stats

    heights = []
    step = (max(columns) - min(columns)) / 19
    minTemp = min(columns)
    for value in columns:
        heights.append(round((value - minTemp) / step) + 1)

    for i in range(20, 0, -1):
        for height in heights:
            if height >= i:
                print("#", end="")
            else:
                print(" ", end="")
        print()



for line in sys.stdin:
    line = (line.strip().split())
    try:
        if(len(line)== 0):
            continue
        elif (line[0] =='temp' or line[0] ==  'humidity' or line[0] == 'pressure'):
            thp(line[0],line[1],line[2])
        
        elif line[0] == 'maxtemp' or  line[0] ==  'maxpressure' or line[0] == 'maxhumidity':
            maxim(line[0],line[1],line[2],line[3])
            
        elif line[0] == 'graphtemp' or line[0] == 'graphpressure':
            graph(line[0],line[1],line[2],line[3])
            
        elif (line[0] == 'coldestcity' or line[0] == 'warmestcity'):
            topcity(line[0],line[1])
        else:
            raise Exception

    except:
        print('Invalid input')