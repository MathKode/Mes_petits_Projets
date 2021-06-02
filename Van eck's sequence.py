from matplotlib import pyplot
import numpy as np
a1 = 0
n = 20
ls = []
nb = a1
tour_final = 0
if a1 < 201 and n < 1000001 :
    while True and tour_final < n :
        ls.append(str(nb)) #On ajoute
        a = list.copy(ls)
        del a[-1]
        if str(nb) not in a :
            nb = 0
        else :
            t = -2
            i = True
            while i :
                if str(ls[t]) == str(nb) :
                    i = False
                    nb = t*-1-1
                t-=1
        tour_final += 1
        print(tour_final)
    y = np.array(ls)
    n=[]
    for i in range(len(ls)) :
      n.append(i)
    x = np.array(n)
    pyplot.plot(x, y)
    pyplot.show()