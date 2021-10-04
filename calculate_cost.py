from os import listdir
from os.path import isfile, join
import os
import sys
import matplotlib.pyplot as plt


def countLinesInPath(path,directory):
    count=0
    for line in open(join(directory,path), encoding="utf8"):
        count+=1
    return count
def countLines(paths,directory):
    count=0
    for path in paths:
        count=count+countLinesInPath(path,directory)
    return count
def getPaths(directory):
    return [f for f in listdir(directory) if isfile(join(directory, f))]
def countIn(directory):
    return countLines(getPaths(directory),directory)


project_list = os.listdir("Projects")

path_list=[]
loc={}
l=[]
for p in project_list:
    path=os.path.join("Projects",p)
    path_list.append(path)
    loc[p]=countIn(path)
    l.append(countIn(path))

e=[]
eD=[]
for item in l:
    temp1=1.4*(item**0.93)
    temp2=4.6*(item**0.26)
    e.append(temp1)
    eD.append(temp2)
f=[]
g=[]
for item in l:
    temp1=5.2*(item**0.91)
    temp2=4.1*(item**0.36)
    f.append(temp1)
    g.append(temp2)

kloc = [i for i in range(0,100)]
m=[]
n=[]
o=[]
plt.plot(project_list,l,'ks',project_list,e,'g^',project_list,eD,'b^',project_list,f,'go',project_list,g,'bo')
plt.xlabel('Projects')
plt.show()


a=2.4
b=1.05
for kl in kloc:
    e = a*((kl)**b)
    m.append(e)

a=3
b=1.12    

for kl in kloc:
    e = a*((kl)**b)
    n.append(e)

a=3.6
b=1.20    

for kl in kloc:
    e = a*((kl)**b)
    o.append(e)

plt.plot(kloc,m,kloc,n,kloc,o)
plt.xlabel('KLOC')
plt.ylabel('Effort')
plt.show()