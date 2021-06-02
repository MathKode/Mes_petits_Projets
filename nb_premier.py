import random
nb_pr = [2]
for i in range(3,200):
    pr = 1
    for m in nb_pr:
        if i%m == 0 :
            pr = 0
    if pr == 1 :
        nb_pr.append(i)
print(nb_pr)
while True:
    print("---------------")
    n1 = nb_pr[random.randint(0,len(nb_pr)-1)]
    n2 = nb_pr[random.randint(0,len(nb_pr)-1)]
    nb = n1 * n2
    print(n1,n2,nb)
    nb1 = 0
    for i in range(0,nb):
        nb2 = 0
        nb1 += 1
        for i in range(0,nb):
            nb2 += 1
            if nb1*nb2 == nb :
                print(nb1,nb2)
^