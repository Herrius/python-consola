import csv
import pandas as pd

def openFile(dataset):
    with open(dataset) as file:
        text=file.readlines()
        print(text)

def readCsv(dataset):
    temperatures=[]
    with open(dataset) as file:
        data=csv.reader(file)
        for row in data:
            temperatures.append(row[1])
    print(temperatures)

def main():
    data=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
    print(data.head())

    fur_color=data["Primary Fur Color"]
    fur_color=data.groupby(["Primary Fur Color"]).size()
    print(fur_color[0])

    data_dict={
         "Fur Color":["Gray","Cinnamon","Black"],
         "Count":[fur_color[1],fur_color[0],fur_color[2]]
    }
    df=pd.DataFrame(data_dict)
    df.to_csv("count_favorite_color.csv")

main()