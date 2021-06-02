from MD5_algorithm import start
import time
debut = time.perf_counter()
print(debut)
c = list("azertyuiopqsdfghjklmwxcvbn")
b = [-1]
while True:
    b[0] = int(b[0]) + 1;t = 0
    for i in b :
        if int(i) == len(c):
            if len(b)==(t+1):b.append(-1)
            else:j = int(b[(t+1)])+1;b[(t+1)]=j
            b[t] = 0
        t += 1
    f = ""
    for i in b:f+=c[int(i)]
    print(f,len(f),end="\r")
    if f=="azuirt":break
fin = time.perf_counter()
print(fin)

