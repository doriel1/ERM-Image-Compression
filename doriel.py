from numpy import random

fileName = open("centsGraph.txt",'w')
z=[]
for i in range(4):
    t=(random.random(),random.random(),random.random())
    z.append(t)
fileName.write(str(z[i]),"\n")