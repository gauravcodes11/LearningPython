#frozenset
s=(1,4,2,4,5,9)
fs=frozenset(s)
print(fs)

#ARRAYS

#NumPy arrays
import numpy as np
a=np.array([1,2,3,4])
print(a)
print(a*2)
#multi-dimensional NumPy array
res=np.array([[1,2],[3,4]])
print(res*2)

#Python array
import array as arr
b=arr.array('i',[1,2,3,4,5])
print(b)
print(b[0])
for i in range(0,5):
    print(b[i])
#extend() method
b.extend([6,7,8,9,10])
print(b) 

#ListComprehension
a=[1,2,3,4,5]
res=[val**2 for val in a ]
print(res)
    #example 2-creating a list from a range
a=[i for i in range(9)]
print(a)
    #example 3-nested loops
a=[(x,y) for x in range(3) for y in range (3)] 
print(a)