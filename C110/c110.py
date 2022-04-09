import plotly.figure_factory as pf
import plotly.graph_objects as go
import statistics as st
import random as r
import pandas as p
import csv 
df = p.read_csv("data2.csv")
data = df["temp"].tolist()
mean = st.mean(data)
sd = st.stdev(data)
print(mean)
print(sd)
figure = pf.create_distplot([data],["temp"],show_hist=False)
figure.add_trace(go.Scatter(x = [mean,mean], y = [0,1], mode = "lines"))
figure.show()
dataset = []
for i in range(0,100):
    random_index = r.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)
ds_mean = st.mean(dataset)
ds_sd = st.stdev(dataset)
print(ds_mean)
print(ds_sd) 

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,100):
        random_index = r.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean
def show_figure(mean_list):
    df = mean_list
    figure = pf.create_distplot([df],["temp"],show_hist=False)
    figure.show()
def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_mean=random_set_of_mean(100)
        mean_list.append(set_of_mean)
    show_figure(mean_list)
setup()