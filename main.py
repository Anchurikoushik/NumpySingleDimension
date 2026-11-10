import numpy as n
lst=[1,2,3,4,6,4,63,5,3,53,5,3,5]
arr=n.array(lst)
print(type(arr))
print(arr)

k=arr.shape
print(k)
k=arr.sum()
print(k)
k=arr.any()
print(k)
k=arr.max()
print(k)
k=arr.argmax()
print(k)
