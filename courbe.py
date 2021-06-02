from matplotlib import pyplot
import numpy as np
file = open('nb_premier.txt','r')
c1 = file.read().split('\n')
y2 = []
for i in c1:
    for j in i.split(':'):
        y2.append(j)
y = []
for h in range(0,int(len(y2)/2)):
    y.append(y2[h])
x = []
for i in range(0,len(y)):
    x.append(i)
print(len(x),len(y))
x = np.array(x)
y = np.array(y)
pyplot.plot(x, y)
pyplot.show()