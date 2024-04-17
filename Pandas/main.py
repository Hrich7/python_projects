import pandas as pd

"""
data = pd.read_csv('./CSV_And_Pandas/weather_data.csv')
average_temp = sum(data['temp'])/len(data['temp'])
print(f"Average temperature : {round(average_temp, 2 )}")

print(f"Average temperature : {round(data['temp'].mean(), 2 )}")
print(f"Maximum temperature : {data['temp'].max() }")

print(f"Day with max temperature : \n{data[data.temp == data.temp.max()]}")
print("\n\n")

monday = data[data.day == "Monday"]
print(f"Day temperature : \n  {(monday.temp * 1.8) + 32} F")

"""
data = pd.read_csv('./Pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240416.csv')

red_squirels = data[data["Primary Fur Color"] == "Cinnamon"]
