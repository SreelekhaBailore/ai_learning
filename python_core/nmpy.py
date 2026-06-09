import numpy as np
from numpy import genfromtxt


# 1D array
arr1  = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr1)

#2D array
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2)

arr1 = np.arange(10)
print(arr1)

print(arr2.size)

print(arr2.shape) # (rows, cols)

print(arr2.dtype)

print(arr2.ndim)

print(len(arr2)) # no of rows in 2D/3D/...

arr2 = np.array([[[0,1,2,4],[2,3,5,6]],[[4,5,7,8],[6,7,9,10]],[[8,9,11,12],[10,11,13,14]]])

print(arr2.ndim)

print(arr2.shape)

print(len(arr2))

arr2 = np.array([0,1,2,3,4,5,6,7,8,9], ndmin=5)
print(arr2)
print(arr2.shape)

arr2 = np.linspace(0,10,5) # 5 numbers between 0 and 10
print(arr2)

arr2 = np.linspace(0,10,5, endpoint=False) # 5 numbers between 0 and 10 excluding 10
print(arr2)

arr2 = np.ones((3,4)) # 3 rows and 4 cols of 1s
print(arr2)

arr2 = np.zeros((3,4)) # 3 rows and 4 cols of 0s
print(arr2)

arr2 = np.eye(2,3) # 2x3 identity matrix
print(arr2)

arr2 = np.diag([1,2,3,4]) # diagonal matrix with 1,2,3 on the diagonal
print(arr2)

print(np.diag(arr2)) # extract the diagonal elements of arr2

arr2 = np.full((3,4), 7) # 3 rows and 4 cols of 7s
print(arr2)

arr2 = np.random.rand(3,4) # 3 rows and 4 cols of random numbers between 0 and 1
print(arr2)

arr2 = np.random.randint(0,10,(3,4)) # 3 rows and 4 cols of random integers between 0 and 10
print(arr2)

print(arr2.dtype)

arr2 = np.arange(1,10,2)
print(arr2)

arr2[2:] = 10
print(arr2)
print(arr2.shape)

arr3 = np.arange(10,15)
print(arr3)
print(arr3.shape)

#assigning arr3 to arr2 from index 4 to end in reverse order
array1 = np.array([10,20,30,40])
array2 = np.zeros(8, dtype=int)
sta_index = 4
array2[sta_index:sta_index+len(array1)] = array1[::-1]
print(array2)


#sort
arr2 = np.array([3,1,4,2,5])
sorted_arr = np.sort(arr2)
print(sorted_arr)

#Inplace sort
arr2.sort()
print(arr2)

#Sort in DESC
arr = np.array([3,1,4,2,5])
sorted_arr_desc = np.sort(arr)[::-1]
print(sorted_arr_desc)

#Sort in  2D array
arr2 = np.array([[3,1,4],[2,5,6],[7,8,9]])
sorted_array = np.sort(arr2, axis=0)
print(sorted_array)

#Sort 2D array row Wise
sorted_array_row = np.sort(arr2, axis=1)
print(sorted_array_row)

#Sort 2D array DESC
sorted_array_desc = np.sort(arr2, axis=0)[::-1]
print(sorted_array_desc)

#Sorting with Indexes
arr2 = np.array([3,1,4,2,5])
sorted_indices = np.argsort(arr2)
print(sorted_indices)
print(arr2[sorted_indices]) # sorted array using the sorted indices

#Lex Sort
print("Lex Sort")
a = np.array([1, 2, 3, 1, 2, 2])
b = np.array([3,1, 2, 4, 5, 6])
print(np.sort(a))
sorted_indices = np.lexsort((b, a)) # sort by a first, then by b
print(sorted_indices)
print(a[sorted_indices]) # sorted array using the sorted indices
print(b[sorted_indices]) # sorted array using the sorted indices

#Reshaping
print("Reshaping")
arr2 = np.array([1,2,3,4,5,6])
reshaped_arr = arr2.reshape(2,3) # reshape to 2 rows and 3 cols
print(reshaped_arr)

#flatten
print(reshaped_arr.flatten()) # flatten the 2D array to 1D array
print(reshaped_arr.ravel()) # flatten the 2D array to 1D array

#Adding new axis
a = np.array([1,2,3])
col_vector = a[:,np.newaxis] # add new axis to make it a column vector
print(col_vector)

print(col_vector[np.newaxis,:]) # add new axis to make it a row vector


#reshaping to 3D array
print("Reshaping to 3D array")
arr2 = np.array([1,2,3,4,5,6])
reshaped_arr = arr2.reshape(2,3,1) # reshape to 2 rows and 3 cols
print(reshaped_arr)

#Reshaping a multi dimensional array
print("Reshaping a multi dimensional array")
arr2 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(arr2)
print(arr2.shape)
reshaped_arr = arr2.reshape(4,2) # reshape to 4 rows and 2 cols
print(reshaped_arr)

#transpose
print("Transpose")
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2)
print(arr2.T) # transpose of the array


#Get first 5 elements of an array
print("Get first 5 elements of an array")
arr2 = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr2[:5]) # get first 5 elements of the array

#Get last 5 elements of an array
print("Get last 5 elements of an array")
print(arr2[-5:]) # get last 5 elements of the array

#get first 5 lements of a list
print("Get first 5 elements of a list")
my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list[:5]) # get first 5 elements of the list

#Get last 5 elements of a list
print("Get last 5 elements of a list")
print(my_list[-5:]) # get last 5 elements of the list



#Dataset Manipulation
print("Dataset Manipulation")
dataset = genfromtxt('D:\python_ws\python_core\student-dataset.csv', delimiter=',', skip_header=1)
print(dataset)

names =dataset['name'] # extract the first column (names)
print(names)
