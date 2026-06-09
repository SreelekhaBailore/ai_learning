import numpy as np
import random

"""Using a NumPy function, how would you create a one-dimensional NumPy array of the numbers from 10 to 100, counting by 10?"""
array = np.arange(10, 101, 10)
print(array)

"""How could you create the same NumPy array using a Python range and a list?"""
array = np.array([i for i in range(10,101,10)])
print(array)

"""What happens if you pass no arguments to the np.array()?"""
# array = np.array()
# print(array)

"""How might you create a NumPy array of the capital letters, A-Z?"""
array =np.array([chr(i) for i in range(ord('A'), ord('Z')+1)])
print(array)


"""How would you create a ten-element NumPy array object of all zeros?"""
array = np.zeros(10)
array.dtype = int
print(array)

print(array.dtype)

"""What function would return the same number of elements, but of all ones?"""
array =np.ones(10)
print(array)

"""How could you create a ten-element array of random integers between 1 and 5 (inclusive)?"""
array = np.random.randint(1,6,10)
print(array)

"""How can you create a normal distribution of 10 numbers, centered on 5?"""
array = np.random.normal(5,1,10)
print(array)

"""What code would create an array of 10 random numbers between 10 and 20?"""
array = np.random.uniform(10, 20, 10) # np.random.rand(10) -- if its between 0 and 1
print(array)

"""Consider the code: np.ones((3,5)). Does this A) create an array of three arrays containing five elements each or B) create an array of five arrays containing three elements each?"""
matrix = np.ones((3,5))
print(matrix)

"""Consider an array named “myarray” that is displayed as in the block below. What value does the code myarray[1,2] return? A) 10 B) 7."""
myarray = np.array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
print(myarray[1,2])

"""An array of three arrays of four elements each like this has twelve elements, of course. How could you create a new array consisting of two arrays of six elements each?"""
array = np.array([[1,2,3,4],
                  [5,6,7,9],
                  [9,10,11,12]])
new_array = array.reshape(2,6)
print(new_array)

"""Given new_array from the last exercise, and the code x = new_array, you run the code:"""
x = new_array
x[0,0] = 42
print (x[0,0])
print(new_array[0,0])

"""How could you create a two-dimensional, 3 x 4 array (three arrays of four elements each) with random numbers from 1 to 10?"""
array = np.random.randint(1,11,(3,4))
print(array)

"""create an array of 64 bit integer zeros for a 3 x 4 array"""
array = np.zeros(dtype=np.int64, shape=(3,4))
print(array)

"""What would the value of x_array.shape be?"""
z_list = [z for z in range(0,5)]
y_list = [z_list for y in range(0,4)]
x_list = [y_list for x in range(0,3)]

x_array = np.array(x_list)
print(x_array.shape)

print(x_array.ndim)

"""change the shape of array"""
array = np.array([[0, 1, 2],
                  [3, 4, 5]])
new_array = array.T
print(new_array)

"""Write a statement that prints the first row. (It will be a five-element array)."""
array = np.array([[ 1,  2,  3,  4,  5],
                  [ 6,  7,  8,  9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20]])
print(array[0])

