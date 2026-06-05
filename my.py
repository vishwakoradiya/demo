import numpy as np


# print("Hello")


# arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# print(arr[1])
# print(type(arr))

# arr_1d = np.array([1, 2, 3, 4, 5])  # 1D array
# arr_2d = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array

# print("1D Array:")
# print(arr_1d)
# print("2D Array:")
# print(arr_2d)

# Arithmetic operations
# addition = arr_1d + 2  # Add 2 to each element
# multiplication = arr_2d * 2  # Multiply each element by 2

# print("\nArray After Addition:")
# print(addition)
# print("Array After Multiplication:")
# print(multiplication)

# Accessing elements
# print("\nElement at index 2 in 1D Array:")

# print(arr_1d[2])  # Access third element of 1D array
# print("Element at row 1 column 2 in 2D Array:")
# print(arr_2d[1, 2])  # Access element from second row, third column


# Slicing
# print("\nSliced Array from 1D Array:")
# print(arr_1d[1:4])  # Slice from index 1 to 3


# Reshaping arrays
# reshaped_array = np.reshape(arr_2d, (3,2))
# print("\nReshaped 2D Array (3x2):")
# print(reshaped_array)


# Statistical functions
# mean_value = np.mean(arr_1d)
# max_value = np.max(arr_2d)
# std_dev = np.std(arr_1d)

# print("\nStatistics:")
# print("Mean of 1D Array:", mean_value)
# print("Maximum in 2D Array:", max_value)
# print("Standard Deviation of 1D Array:", std_dev)


# Creating specialized arrays
# zeros_array = np.zeros((2, 3))  # 2x3 array of zeros
# ones_array = np.ones((3, 2))  # 3x2 array of ones
# identity_matrix = np.eye(4)  # 3x3 identity matrix

# print("\nSpecial Arrays:")
# print("Zeros Array:")
# print(zeros_array)
# print("Ones Array:")
# print(ones_array)
# print("Identity Matrix:")
# print(identity_matrix)


# original = np.array([10, 20, 30])
# copy_array = original.copy()

# copy_array[0] = 99  # Modify the copy
# print("Original Array:", original)  # Unchanged
# print("Copy Array:", copy_array)    # Modified


# original = np.array([10, 20, 30])
# view_array = original.view()

# view_array[0] = 99  # Modify the view
# print("Original Array:", original)  # Affected
# print("View Array:", view_array)    # Modified

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr.shape)  #shape

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# result = np.concatenate((arr1, arr2))
# print(result) 

#The concatenate() function joins arrays along an existing axis.
# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 9]])
# result = np.concatenate((arr1, arr2), axis=1)
# print(result)

# arr = np.array([10,20,30,40,50])
# print(arr)
# print(arr[2])
# print(type(arr))

# arr1 = np.array([11,12,13])
# arr2 = np.array([[14,15,16],[17,18,19]])
# print('1d array:')
# print(arr1)
# print('2d array:')
# print(arr2)

# addition = arr1 + 2
# print(addition)
# multiplication = arr2 * 1
# print(multiplication)








myarr = np.array([[31,32,33],[34,35,36]])
mean_value = np.mean(myarr)
max_value = np.max(myarr)
print(max_value)
print(mean_value)

# print(myarr)

# addition = myarr + 2
# print(addition)


# 5 * (1<=1) 
# print(5 * (1<=1))


