import pandas as pd
import csv
import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go


df = pd.read_csv(r"mediumData.csv")
time = df["reading_time"]
pop_mean = statistics.mean(time)
print(pop_mean)

def random_sample(num):
    dataSet=[]
    for i in range(0,num):
        index = random.randint(0,len(time))
        value = time[index]
        dataSet.append(value)
        mean = statistics.mean(dataSet)
        print(mean)

def showFig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],["temp"],show_hist=False)
    fig.show()

def setUp():
    mean_list = []
    for i in range (0,100):
        set_of_mean = random_sample(30)
        mean_list.append(set_of_mean)   
        showFig(mean_list)
