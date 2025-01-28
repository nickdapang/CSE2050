import os

def read_weather_data(file_path: str):
  
    with open(file_path, 'r') as file:
        data =  file.readlines()
    list= []
    for i in data:
        list.append(tuple(i.split(',')))
    return list

def calculate_average_temperature(weather_data):
    result = 0.0
    j = 0
    for i in weather_data:
        result += (float)(i[1])
        j += 1
    average= result / j
    return average

def calculate_total_rainfall(weather_data):
    total = 0
    for i in weather_data:
        total += (float)(i[2])
    return total

def find_highest_temperature(weather_data):
    highest_temp = -99999
    
    for i in weather_data:
        if int(i[1]) > highest_temp:
            highest_temp = int(i[1])
            highest_date = i[0]
    return highest_temp, highest_date


def find_lowest_temperature(weather_data):
    lowest_temp = 9999999999
    for i in weather_data:
        if int(i[1]) < lowest_temp:
            lowest_temp = int(i[1])
            lowest_date = str(i[0])
    return lowest_temp, lowest_date

def find_day_with_most_rainfall(weather_data):
    highest_rainfall = 0
    for i in weather_data:
        if float(i[2]) > highest_rainfall:
            highest_rainfall = float(i[2])
            highrainfall_date = str(i[0])
    return highest_rainfall, highrainfall_date

