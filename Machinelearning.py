import numpy as np
import math
import random
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale

data = pd.read_csv(".\\appendix.csv")
Course_subject = data["Course Subject"]
i = 1.0
quantified_interest = {}
for ele in Course_subject:
    ele = ele.replace("and ", '')
    ele = ele.replace(", ", ",")
    ele = ele.replace(" ", "")
    interests = ele.split(",")
    for x in range(0, len(interests)):
        if interests[x] not in quantified_interest.keys():
            quantified_interest.update({interests[x]: i})
            i = i + 1
        else:
            total = 0.0
            for y in range(0, len(interests)):
                total = total + quantified_interest[interests[y]]
                average = total / len(interests)
            for y in range(0, len(interests)):
                quantified_interest[interests[y]] = quantified_interest[interests[y]] + (
                            average - quantified_interest[interests[y]]) / 200
            break

quantified_level = {"Freshman" : 15.0, "Sophomore" : 16.0,"Junior" : 17.0,"Senior" : 18.0, "6th Grade" : 6.0,"7th Grade" : 7.0,"8th Grade" : 8.0,"9th Grade" : 9.0,"10th Grade" : 10.0,"11th Grade" : 11.0,"12th Grade" : 12.0,"Masters 1st year" : 23.0,"Masters 2nd year" : 24.0,"PHD" : 26.0,}
data = pd.read_csv(".\\csv - Sheet1.csv")
from sklearn.utils import shuffle
l = []
for level in data["Level"]:
    l.append(quantified_level[level])
data.insert(1,"Year",l)
del data['Level']
i =[]
for ele in data["Interest"]:
    ele = ele.replace(", ",",")
    ele = ele.replace (" ","")
    interests = ele.split(",")
    average = 0.0
    for interest in interests:
        average += quantified_interest[interest]
    average = average / len(interests)
    i.append(average)
del data['Interest']
data.insert(1,"Interest",i)
len(data)
data = shuffle(data)
data = data[:20]
print(data)

n =4
inertia = 100000.0
while inertia > 0.3:
    model = KMeans(n_clusters=n)
    model = model.fit(scale(data))
    inertia = model.inertia_/len(data)
    n+=1
print(n-1)

newcolors =[]
colors = ['red','green','blue','magenta','black','#c47519','#00FF00','#c9bc29','#a0d6f3']
random.shuffle(colors)
for ele in model.labels_:
    newcolors.append(colors[ele])
print(model.cluster_centers_)
print(model.inertia_)
plt.figure(figsize=(20, 10))
plt.scatter(data["Interest"], data["Year"], c=newcolors, s = 80)
plt.savefig('Cluster.png')
plt.show()
