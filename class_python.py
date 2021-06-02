import random
class Pain_choco:
    def __init__(self,heures_restantes,id):
        self.hr = int(heures_restantes)
        self.id = id
    def Time_fly(self):
        self.hr -= 1

ls_choco = []
for i in range(0,3):
    ls_choco.append(Pain_choco(random.randint(2,5),i))
print(ls_choco)
for choco in ls_choco:
    print(choco.id,":",choco.hr)
for heure in range(0,6):
    index = 0
    for choco in ls_choco:
        choco.Time_fly()
        if choco.hr == 0:
            del ls_choco[index]
        index += 1
        print(choco.id,":",choco.hr)
print(ls_choco)