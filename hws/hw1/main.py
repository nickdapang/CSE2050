from weather_analysis import *

# main.py

def weather_analyze(file_path):
    dict = {}
    dict1 = {}
    dict2 = {}
    dict3 = {}
    list = read_weather_data(file_path)
    
    avg_temp = calculate_average_temperature(list)

    dict['average_temperature'] = avg_temp

    total_rainfall = calculate_total_rainfall(list)

    dict['total_rainfall'] = total_rainfall

    high_temp = find_highest_temperature(list)

    dict1['date'] = high_temp[0]
    dict1['temperature'] = high_temp[1]


    dict['highest_temperature'] = (dict1)

    low_temp = find_lowest_temperature(list)
     
    dict2['date'] = low_temp[0]
    dict2['temperature'] = low_temp[1]

    dict['lowest_temperature'] = (dict2)

    most_rainfall = find_day_with_most_rainfall(list)

    dict3['date'] = most_rainfall[0]
    dict3['rainfall'] = most_rainfall[1]
    dict['most_rainfall'] = (dict3)

    return dict


if __name__ == "__main__":
    
    results = weather_analyze("/Users/nick/Documents/GitHub/CSE2050/hws/hw1/weather_data.txt") #or the path to the file
    print(results)