
import random

#input
f=str(input())
j=f.split(" ")

#constants
x1=["a", "e", "o", "u"]


def owo(d):
    r=[]
    k1=[]  
    f1=""
    for h in d:
        r.append(list(h))
    for s1 in r:
        for w in s1:
            if w == "l" or w == "r":
                s1[s1.index(w)]="w"
            if w == "n" and s1.index(w) < len(s1)-1 and s1[s1.index(w)+1] in x1:
                s1[s1.index(w)]="ny"
        k1.append(s1)
    for zn in k1:
        q=""
        for g in zn:
            q=q+g
        f1=f1+q+" "
    return(f1)

print("\n")
print(owo(j))

#this function generates the stutter effect in OwOtext
k=j
v=x1
def st(x):
    for i in x:
        r=random.randint(1,5)
        if list(i)!= [] and list(i)[0] not in v and r == 1 and list(i)[0] != "\"":
            x[x.index(i)]=list(i)[0]+"-"+i
    s=""
    for i in x:
        s=s+i+" "
    return(s)


#print(st(k))


exp=["~","~~","OwO","OwO","OwO","owo","UwU","uwu","UwU","UwU",">w<","^w^","^~^",">///<", ":3", "desu","baka!"]

def insertEmote(x):
    for i in x:
        r=random.randint(0,3)
        z=list(i)
        z.reverse()
        if z != [] and z[0] in ["!",".","?"] and r <= 1:
            r2=random.choice(exp)
            x[x.index(i)]=i+" "+r2
    return(x)

print("\n")
print(st(insertEmote(owo(k).split(" "))))


