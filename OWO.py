#i want to fucking yeet myself off a cliff
import random

#input
发=str(input())
就=发.split(" ")

#constants
熙=["a", "e", "o", "u"]

#this gay ass function turns text into OwOtext
#the variables are in chinese cause 你他妈的黑鬼,这是我的冰淇淋!
def owo(都):
    任=[]
    库=[]  
    负=""
    for 很 in 都:
        任.append(list(很))
    for 撒 in 任:
        for 哇 in 撒:
            if 哇 == "l" or 哇 == "r":
                撒[撒.index(哇)]="w"
            if 哇 == "n" and 撒.index(哇) < len(撒)-1 and 撒[撒.index(哇)+1] in 熙:
               撒[撒.index(哇)]="ny"
        库.append(撒)
    for 赞 in 库:
        群=""
        for 杠 in 赞:
            群=群+杠
        负=负+群+" "
    return(负)

print("\n")
print(owo(就))

#this function generates the stutter effect in OwOtext
k=就
v=熙
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

#now it's time to notice some bulges
exp=["~","~~","OwO","OwO","OwO","owo","UwU","uwu","UwU","UwU",">w<","^w^","^~^",">///<", ":3", "desu","baka!"]

def insertRandomShit(x):
    for i in x:
        r=random.randint(0,3)
        z=list(i)
        z.reverse()
        if z != [] and z[0] in ["!",".","?"] and r <= 1:
            r2=random.choice(exp)
            x[x.index(i)]=i+" "+r2
    return(x)

print("\n")
print(st(insertRandomShit(owo(k).split(" "))))


