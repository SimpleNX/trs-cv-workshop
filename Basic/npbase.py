import numpy as np
#Array
#numpy array is a grid of values, all of same type with +ve indexes.
#Dimensions = Rank of the array
#Shape = Size of the array along each dimension
'''a = np.array([1,2,3])#Rank 1 Array
b = np.array([[1,2,3],[4,5,6]])#Rank 2 Array
#Using lists in the arrays.
a[2] = 25
print(a)
print(b)
print(type(b))
print(b.shape)
#Numpy functions, zeros(null matrix), ones(all elements 1),full(const array) with assigned value, eye(I) take input for shape of the array.
c = np.zeros((2,2))
d = np.ones((2,2,2))
e = np.full((2,2,2,2),7)
f = np.eye(3)
print(c)
print(d)
print(e)
print(f)

s = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(s)
s1 = s[1:3, 1:4]#Slicing of array, (y-start:y-end, x-start:x-end) if end is not specified it traverses the whole array.
print (s1)'''

#Integer Array Inedxing
#Boolean Array Indexing
'''a = np.array([[1,2],[3,4],[5,6]])
bool_idx = (a>2)#Find the elements of a which are greater than 2
                #returns a numpy array with the corresponding boolean values
print(bool_idx)

#Usage of the boolean matrix
#Use it to construct a rank 1 array / List
print(a[bool_idx])
print(a[a>2])'''
#Slice Question
b = np.ones((5,5), dtype=np.int64)
b[1:4,1:4] = np.zeros((3,3))
b[2:3,2:3]=np.full((1,1),9)
#print(b)
'''c = np.array([1.1,1.3], dtype=np.int64)'''

#Slice Q2
a = np.zeros((5,5), dtype = np.int64)
print (a)
c=1
for i in range(0,5,1):
    for j in range(0,5,1):
        a[i][j]=c
        c+=1

'''print(a)
print(np.add(a,b))'''
#np.multiply(position multiplication),divide,sqrt
#Dot Product
print(a.dot(b))
print(np.dot(a,b))#Matrix Multiplication as defined in Algebra
print(a@b)