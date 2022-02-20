def last_name(username,last_name):
    """
    Input : math krem
    Output : mathk, mathkr, mathkrem

    [2;4] -->   kr math
                kre math 
    """
    l=[-1,-1];tt=len(username);ls=[]
    for i in range((len(username)+1)*(len(last_name)+1)):
        l[0]=l[0]+1
        if l[0]==tt:
            l[0]=-1
            l[1]=l[1]+1
        if l[0]!=-1:
            u=username[0:(l[0]+1)]
        else:
            u=""
        
        if l[1]!=-1:
            k=last_name[0:(l[1]+1)]
        else:
            k=""
        
        ls.append(f"{u}{k}")
        if f"{k}{u}" not in ls:
            ls.append(f"{k}{u}")
    return ls

def __maj(username):
    """
        math, 
        Math, 
        mAth ...
    """
    nb=2**len(username)
    l=[]
    ls=[]
    for i in range(len(username)):
        l.append(0)
    for i in range(nb-1):
        n=0
        l[n]=l[n]+1
        for j in range(len(l)-1):
            if l[n]==2:
                l[n]=0
                l[n+1]=l[n+1]+1
            n+=1
        #print(l)
        name=""
        n=0
        for lettre in username:
            if l[n]==0:
                name+=lettre.lower()
            else:
                name+=lettre.upper()
            n+=1
        ls.append(name)
    return ls

def maj(ls_name):
    ls=[]
    for name in ls_name:
        l=__maj(name)
        for i in l:
            ls.append(i)
    return ls

def number(ls_name,start,end):
    """
    Input : ["math","Math"...] 1900 1901
    Output : ["math1900","math1901"...]
    """
    ls=[];tt=end-start+1
    for name in ls_name:
        date=start
        for i in range(tt):
            ls.append(f"{name}{date}")
            ls.append(f"{date}{name}")
            date+=1
    return ls

def symbol(ls_name,symbol=list("&\"#'{([-|è`_\ç^ à@)] =}+$^ù%!:;,?./§*¨€")):
    """
    Input : ["Math"...] ["$" "%"]
    Output : ["$Math", "%Math" ... "Math%"]
    """
    #Début
    ls=[]
    for name in ls_name:
        for s in symbol:
            ls.append(f"{s}{name}")
            ls.append(f"{name}{s}")
    return ls

def chiffre(ls_name,symbol=list("1234567890")):
    """
    Input : ["Math"...] ["1" "2"]
    Output : ["1Math", "2Math" ... "Math2"]
    """
    #Début
    ls=[]
    for name in ls_name:
        for s in symbol:
            ls.append(f"{s}{name}")
            ls.append(f"{name}{s}")
    return ls

def keep_text(mp):
    """
    Input : 123MathK123
    Output : [1,0,0,0,1], 2, 3
    1->Maj  0->min
    """
    ls=[];maj=list("AZERTYUIOPQSDFGHJKLMWXCVBN");_min=list("AZERTYUIOPQSDFGHJKLMWXCVBN".lower())
    nb1=0;nb0=0
    for lettre in mp:
        if lettre in maj:
            ls.append(1)
            nb1+=1
        elif lettre in _min:
            ls.append(0)
            nb0-=-1
    return ls

def score(ls):
    tt=[];last=ls[0];t=0
    for i in ls:
        if i != last:
            tt.append(t)
            last=i
            t=0
        t+=1
    tt.append(t)
    result=1
    t=0
    for nb in tt:
        if t==0:
            t=1
            result=result*nb
        else:
            t=0
            result=float(result/nb)
    result=float(result/len(tt))
    return result

#print(score([0,0,1,1,1,0,0,0]))

def tri(mp_ls):
    """
    Input : ["Mp1","Mp2"...]
    Output : first[] mid[] end[]
    """
    first=[];mid=[];end=[]
    for mp in mp_ls:
        print(mp,end='\r')
        ls, nb1, nb0=keep_text(mp)
        #[1,0,0,0...,0] first
        #[0,0,0,0...,1] first
        #[0,0,0,0...,0] first
        #[1,1,1,1...,1] first
        if ls[0]==1 and nb1==1:
            first.append(mp)
        elif ls[-1]==1 and nb1==1:
            first.append(mp)
        elif nb1==0:
            first.append(mp)
        elif nb0==0:
            first.append(mp)
        else :
            tt=-1;last=-1
            for i in ls:
                if i!=last:
                    last=i
                    tt+=1
            if tt==2:
                mid.append(mp)
            elif ls[0]==1 and ls[0]==0 and ls[0]==0 and ls[0]==0 :
                mid.append(mp)
            elif ls[0]==1 and ls[0]==1 and ls[0]==0 and ls[0]==0 :
                mid.append(mp)
            elif ls[0]==1 and ls[0]==1 and ls[0]==1 and ls[0]==0 :
                mid.append(mp)
            elif ls[0]==1 and ls[0]==1 and ls[0]==1 and ls[0]==1 :
                mid.append(mp)
            else:
                end.append(mp)




"""
plausibilite(["HdkZhdAZkjD","AhdghsK155"])
exit(0)
"""

name=str(input("Username: ")).lower()
last=str(input("LastName: ")).lower()
start=int(input("Date-start: "))
end=int(input("Date-End: "))
sy=str(input("Symbole (11 for use default list): "))
if sy=="11":
    sy=list("&\"#'{([-|è`_\ç^ à@)] =}+$^ù%!:;,?./§*¨€")
else:
    sy=list(sy)

nb=str(input("Number (11 for default): "))
if nb=="11":
    nb=list("1234567890")
else:
    nb=list(nb)

filename=name+".txt"
file=open(filename, "w")

print("Generate Username-LastName list")
ls=last_name(name,last)
file.write("\n".join(ls))
print("Generate Upper-Lower List")
ls2=maj(ls)
file.write("\n".join(ls2))
print("Generate Number (date) List")
ls3=number(ls2,start,end)
file.write("\n".join(ls3))
print("Generate Symbol List")
ls4=symbol(ls3,sy)
file.write("\n".join(ls4))
print("Generate Number Before-After List")
ls5=chiffre(ls4,nb)
file.write("\n".join(ls5))
file.close()
print("Done !!!\nThe password list is save at",filename)