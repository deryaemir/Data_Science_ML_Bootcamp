###############################################
# DATA ANALYSIS WITH PYTHON
###############################################
# - NumPy
# - Pandas
# - Data Visualization: Matplotlib & Seaborn
# - Advanced Functional Exploratory Data Analysis
#############################################
# NUMPY
#############################################
# Neden NumPy? (Why Numpy?)
# NumPy Array'i Oluşturmak (Creating Numpy Arrays)
# NumPy Array Özellikleri (Attibutes of Numpy Arrays)
# Yeniden Şekillendirme (Reshaping)
# Index Seçimi (Index Selection)
# Slicing
# Fancy Index
# Numpy'da Koşullu İşlemler (Conditions on Numpy)
# Matematiksel İşlemler (Mathematical Operations)

#############################################
# Neden NumPy?
#############################################
# When storing data in NumPy, the data is kept in a fixed type.
# This provides the ability to perform operations much faster compared to lists.
# Difference from lists:
# 1. Efficient data storage.
# 2. Ability to perform high-level (vectorized) operations.
# Why NumPy?
# 1. Speed (thanks to storing data in a fixed type).
# 2. Ability to perform high-level operations.

import numpy as np
# Multiplication using normal Python lists
# (element-wise multiplication with a loop)
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]
ab = []
for i in range(0, len(a)):
    ab.append(a[i] * b[i])

# Multiplication using NumPy arrays
# (vectorized operation, no loop needed, much faster)
a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
a * b
#############################################
# Creating Numpy Arrays
#############################################
# Just like Python has its own data structures,NumPy also has special data structures.
# The NumPy array is one of these data structures.
# We can create a NumPy array from a Python list.

import numpy as np
# Create a NumPy array from a Python list
np.array([1, 2, 3, 4, 5])
# Check the type of the object (it's a numpy.ndarray)
type(np.array([1, 2, 3, 4, 5]))
# Create an array of 10 zeros (dtype=int → integer values)
np.zeros(10, dtype=int)
# Create an array of 10 random integers between 0 and 10
np.random.randint(0, 10, size=10)
# Create a 3x4 matrix with random values from a normal distribution
# mean = 10, standard deviation = 4
np.random.normal(10, 4, (3, 4))

#############################################
# Attibutes of Numpy Arrays
#############################################
import numpy as np

# ndim  : number of dimensions
# shape : shape of the array
# size  : total number of elements
# dtype : data type of the array elements

# Create a 1D array with 5 random integers between 0–9
a = np.random.randint(10, size=5)
a.ndim   # -> 1   (1D array)
a.shape  # -> (5,)  (1 dimension, 5 elements)
a.size   # -> 5   (total number of elements)
a.dtype  # -> int32 or int64 (depends on the system)

#############################################
# Reshaping
#############################################
import numpy as np

np.random.randint(1, 10, size=9)
# Reshape the 1D array of size 9 into a 3x3 matrix
np.random.randint(1, 10, size=9).reshape(3, 3)

# Another example: first create the array, then reshape it
ar = np.random.randint(1, 10, size=9)
ar.reshape(3, 3)  # valid because 3 * 3 = 9 elements
# NOTE: Reshape works only if the total number of elements matches.
# For example, size=10 has 10 elements, but reshape(3, 3) requires 9 elements.
# This mismatch will raise a ValueError.

#############################################
# Index Selection
#############################################
import numpy as np
a = np.random.randint(10, size=10)
a[0]      # first element
a[0:5]    # first 5 elements (index 0 to 4)
a[0] = 999   # assign new value to the first element

# Create a 2D array (3x5 matrix) with random integers between 0–9
m = np.random.randint(10, size=(3, 5))

m[0, 0]   # element at row 0, column 0
m[1, 1]   # element at row 1, column 1
m[2, 3]   # element at row 2, column 3

m[2, 3] = 999   # assign new value to element at row 2, column 3
m[2, 3] = 2.9   # assign 2.9 → automatically converted to int (2) because dtype=int

m[:, 0]   # all rows, column 0 (first column)
m[1, :]   # row 1, all columns (second row)
m[0:2, 0:3]  # rows 0–1, columns 0–2 (a sub-matrix)


#############################################
# Fancy Index
#############################################
import numpy as np

# Create an array from 0 to 30 with step size 3
v = np.arange(0, 30, 3)   # -> [ 0  3  6  9 12 15 18 21 24 27]

v[1]   # element at index 1 -> 3
v[4]   # element at index 4 -> 12

# Define a list of indexes
catch = [1, 2, 3]

# Fancy indexing: get elements at indexes 1, 2, and 3
v[catch]   # -> [3 6 9]

#############################################
# Conditions on Numpy
#############################################
import numpy as np
v = np.array([1, 2, 3, 4, 5])

# Classic way (with loop)
#######################
ab = []
for i in v:
    if i < 3:        # condition check
        ab.append(i) # add elements less than 3
# Result: [1, 2]

# With NumPy (vectorized conditions)
#######################
v < 3       # -> [ True  True False False False ]
v[v < 3]    # elements less than 3 -> [1 2]
v[v > 3]    # elements greater than 3 -> [4 5]
v[v != 3]   # elements not equal to 3 -> [1 2 4 5]
v[v == 3]   # elements equal to 3 -> [3]
v[v >= 3]   # elements greater than or equal to 3 -> [3 4 5]

#############################################
# Mathematical Operations
#############################################
import numpy as np
v = np.array([1, 2, 3, 4, 5])

v / 5        # divide each element by 5 -> [0.2 0.4 0.6 0.8 1. ]
v * 5 / 10   # multiply by 5 then divide by 10 -> [0.5 1.  1.5 2.  2.5]
v ** 2       # square each element -> [ 1  4  9 16 25]
v - 1        # subtract 1 from each element -> [0 1 2 3 4]

# NumPy mathematical functions
np.subtract(v, 1)   # subtract 1 -> [0 1 2 3 4]
np.add(v, 1)        # add 1 -> [2 3 4 5 6]
np.mean(v)          # average -> 3.0
np.sum(v)           # sum -> 15
np.min(v)           # minimum value -> 1
np.max(v)           # maximum value -> 5
np.var(v)           # variance -> 2.0
v = np.subtract(v, 1)  # update v by subtracting 1 from each element

# Solving a system of linear equations with NumPy
#######################

# Equations:
# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

a = np.array([[5, 1],   # coefficients matrix
              [1, 3]])
b = np.array([12, 10])  # results vector

np.linalg.solve(a, b)   # -> array([2.,  2.666...])
# Solution: x0 = 2, x1 = 8/3


