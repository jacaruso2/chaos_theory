import numpy as np
import matplotlib.pyplot as plt
import sys
from mpl_toolkits.mplot3d import Axes3D

rs = np.linspace(1,4,1000)


#print(rs)

stabilization_record = []

def core_function(rate):
    r = rate
    array = [.4]
    for i in range(1,1000):
        x_at_n = array[-1]
        next_x = r * x_at_n * (1-x_at_n)
        array.append(round(next_x,5))
    stabilization = list(set(array[-300:]))
    stabilization_record.append(tuple(stabilization))

for value in rs:
    core_function(value)

def core_function_plot(rate):
    r = rate
    array = [.4]
    for i in range(1,1000):
        x_at_n = array[-1]
        next_x = r * x_at_n * (1-x_at_n)
        array.append(next_x)
    stabilization = list(set(array[-15:]))
    x = np.arange(1,1001)
    y = np.array(array)
    plt.xlabel("Iteration")
    plt.ylabel("Population Percent of Total")
    plt.plot(x,y, color ="green")
    plt.show() 

#print(core_function_plot(1.003003))

#print(stablization_record)


xs = [i for i in rs]
ys = stabilization_record

pxs = []
pys = []
value_counts_x = []
value_counts = []

for i, element in enumerate(xs):
    value_counts_x.append(element)
    value_counts.append(len(ys[i]))
    for value in ys[i]:
        pxs.append(element)
        pys.append(value)
    

def phase_diagram(r):
    values_array = [.4]
    for i in range(1,1000):
        x_at_n = values_array[-1]
        next_x = r * x_at_n * (1-x_at_n)
        values_array.append(round(next_x,5))
    stabilized = values_array[-300:]
    y = [stabilized[index+1] for index, value in enumerate(stabilized[:-1])]
    z = [stabilized[index+2] for index, value in enumerate(stabilized[:-2])]

    return stabilized, stabilized[:-2], y[:-1], z

s,x,y,z = phase_diagram(4)

#print(len(x), len(y), len(z))

#Show logistic map:

plt.plot(pxs, pys, ',' , markersize = 100)
plt.title('Logistic Map')
plt.xlabel('Growth Rate')
plt.ylabel('Population Oscillation Values')
plt.show()

#Show number of values converged at for each value r:   

#plt.plot(value_counts_x, value_counts)
#plt.title('Complexity per value R')
#plt.xlabel('Growth Rate')
#plt.ylabel('Population Oscillation Values')
#plt.show()

#Time series plot of data for phase diagram:

#plt.plot(s)
#plt.show()

#Phase diagram:

#fig = plt.figure() 
#ax = plt.axes(projection ='3d') 
#ax.plot3D(x, y, z, '.', 'pink') 
#plt.show()

















