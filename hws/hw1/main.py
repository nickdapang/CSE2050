from weather_analysis import *

# main.py

def weather_analyze(file_path):
    dict = {}

    list = read_weather_data(file_path)
    
    avg_temp = calculate_average_temperature(list)

    dict['average_temperature'] = avg_temp

    return dict


if __name__ == "__main__":
    
    results = weather_analyze("/Users/nick/Documents/GitHub/CSE2050/hws/hw1/weather_data.txt") #or the path to the file
    print(results)