import os
if "nb_premier.txt" not in os.listdir():
    file = open("nb_premier.txt","w")
    file.close()
    nb_pr = [["2"]]
else :
    file = open("nb_premier.txt","r")
    c1 = file.read().split('\n')
    c = []
    for i in c1:
        c.append(i.split(':'))
    file.close()
    if c == [[""]] :
        nb_pr = [["2"]]
    else :
        nb_pr = c
print(nb_pr)
if nb_pr[-1] == ['']:
    del nb_pr[-1]
for i in range(int(nb_pr[-1][-1])+1,100000000000000000000):
    pr = 1
    for m in nb_pr:
        for j in m :
            if i%int(j) == 0 :
                pr = 0
    if pr == 1 :
        print(i,end='\r')
        if len(nb_pr[-1])%100 == 0 :
            nb_pr.append([str(i)])
        else :
            k = nb_pr[-1]
            k.append(str(i))
            nb_pr[-1] = k
        file = open("nb_premier.txt","w")
        for n in nb_pr:
            file.write(":".join(n))
            file.write('\n')
        file.close()
print(nb_pr)