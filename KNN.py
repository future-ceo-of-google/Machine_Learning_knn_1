import numpy as np
import matplotlib.pyplot as plt
s=np.random.uniform(100,200,150)
t=np.random.uniform(150,250,150)
s=list(s)#storing dynamically generated data
t=list(t)
plt.plot(s,'o',color='#ffff00')#labelling the data in the graph
plt.plot(t,'o',color='silver')
dic={}
dic['A']=s#mapping the data with labels
dic['B']=t
distance=[]
td=int(input('Enter the test data:'))#test for a single input 
plt.plot(td,'o',color='aqua')
for key in dic:
    for i in range(120):
        t=str(abs(dic[key][i]-td))+key
        distance.append(t)
distance.sort()
k=int(input('Enter the key value:')) #value for the k-nearsest neighbour
s=t=0
for i in range(k):
    if distance[i][len(distance[i])-1]=='A':
      s+=1
    else:
      t+=1
if s>t:
    print("Data belongs to class A")
else:
    print("Data belongs to class B")
