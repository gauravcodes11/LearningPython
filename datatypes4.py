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