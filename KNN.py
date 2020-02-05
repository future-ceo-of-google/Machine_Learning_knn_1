import numpy as np
#test comment
import matplotlib.pyplot as plt
s=np.random.uniform(100,200,150)
t=np.random.uniform(150,250,150)
s=list(s)
t=list(t)
plt.plot(s,'o',color='silver')
plt.plot(t,'o',color='gold')
dic={}
dic['A']=s
dic['B']=t
td=int(input('Enter the test data:'))
plt.plot(td,'*',color='aquamarine')
distance=[]
for key in dic:
    for i in range(120):
        s=key
        t=str(abs(dic[key][i]-td))
        t+=s
        distance.append(t)       
distance.sort()
print('It belongs to the class:',distance[0][len(distance[0])-1])
