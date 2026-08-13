import numpy as np
from future.builtins.new_min_max import new_min_max
from numpy import dtypes
from numpy.f2py.symbolic import as_eq
from numpy.ma.core import masked_where
from numpy.ma.extras import average
from numpy.random.mtrand import random_sample
from setuptools.namespaces import flatten

# array_1 = np.array(1)
# array_2 = np.array([1,2,3,4])
# array_3 = np.array([[1,2,3,4],[1,2,3,4]])
# array_4 = np.zeros((3,4), dtype = int)
# array_5 = np.ones((2,2), dtype = int)
# array_6 = np.arange(0,20,2)
# print(array_6)
#


# a = np.arange(15).reshape(3, 5)
# # Print: shape, ndim, size, dtype, itemsize.
# print(a)
# print(a.shape)
# print(a.ndim)
# print(a.size)
# print(a.dtype)
# print(a.itemsize)

# m = np.array([[10, 20, 30],
#               [40, 50, 60],
#               [70, 80, 90]])
# # Print the first row, the last row, the second column, and the element at [1, 2].
# print(m[0])
# print(m[-1])
# print(m[:,-2])
# print(m[1][2])


# m = np.array([[10, 20, 30],
#               [40, 50, 60],
#              [70, 80, 90]])
# # - the first two rows
# # - the last two columns
# # - the center 2x2 submatrix
# # - the matrix in reversed row order.
#
# #print(m[:2])
# #print(m[:,-2:])
# #print(m[1:,1:])
# #print(m[1:, :2])
# print(m[:,::-1])
#
# a = np.array([12, 45, 7, 89, 34, 100, 3])
# # Print only the values that are:
# # - greater than 30
# # - smaller than 50
# # - even.
# result = a[(a>30) & (a<50) & (a%2 == 0)]
# print(result)


# scores = np.array([45, 62, 88, 30, 100, 55])
# #Use np.where to build a new array where score >= 50 becomes 'PASS' and score < 50 becomes 'FAIL'.
# result = np.where(scores>=50, 'Pass', 'Fail' )
# print(result)



# scores = np.array([[80, 75, 90],
#                    [55, 60, 70],
#                    [100, 95, 85]])
#
# # - the mean of the whole matrix
# # - row-wise means
# # - column-wise means.
#
# resalt_1 = scores.mean()
# print(resalt_1)
# resalt_2 = scores.mean(axis=1)
# print(resalt_2)
# resalt_3 = scores.mean(axis=0)
# print(resalt_3)


# a = np.array([5, 2, 9, 2, 7, 9, 1, 5])
# #Print the unique values, the index of the maximum value, and the index of the minimum value.
#
# max_a = a.argmax()
# min_a = a.argmin()
# unique_a = np.unique(a)
# print(unique_a)
# print(min_a)
# print(max_a)

# m = np.arange(1, 17).reshape(4, 4)
# # Use fancy indexing to get:
# # - all corner elements
# # - the main diagonal elements
# # - the elements at rows [0, 2] and columns [1, 3].
# corners = m[[0,0,3,3],[0,3,0,3]]
# #print(m,end = " ")
# #print(corners)
# diagonal = m[[0,1,2,3],[0,1,2,3]]
# #print(diagonal)
# rows = np.array([1,3])
# cols = np.array([0, 2])
# gird = m[np.ix_(rows,cols)]




# a = np.array([[1, 2, 3], [4, 5, 6]])
# row = np.array([10, 20, 30])
# #Compute a + row and explain in a short comment why broadcasting works here.
#
# print(a+row)

# a = np.array([[1, 2, 3],
#               [4, 5, 6]])
# col = np.array([[100],
#                 [200]])
# #Compute a + col and explain the shape logic in a short comment.
# print(a+col)


# data = np.arange(24)
#
# try:
#     data_1 = data.reshape(3, 10)
#     print(data_1)
# except ValueError as e:
#     print(f'It is invalid value {e}')




# a = np.arange(12).reshape(3, 4)
# #Print the original array, the transposed array, the original shape, and the transposed shape.
# print(a)
# print(a.T)
# print(a.shape)
# print(a.T.shape)


# a = np.array([[1, 2], [3, 4]])
# # Create flat1 = a.flatten() and flat2 = a.ravel(). Change the first element in both results and observe whether the
# # original array changes. Then write a short note explaining the difference.
# flat_1 = a.flatten()
# flat_2 = a.ravel()
# print(flat_2)
# print(flat_1)


# a = np.array([[1, 2],
#               [3, 4]])
# b = np.array([[5, 6],
#               [7, 8]])
# # Produce:
# # - vertical concatenate
# # - horizontal concatenate
# # - vstack
# # - hstack
# # - stack(axis=0).
# a_b = np.concatenate((a,b), axis=0)
# a_b_1 = np.concatenate((a,b), axis=1)
# print(a_b)
# print(a_b_1)
# a_b_2 = np.vstack((a,b))
# print(a_b_2)
# a_b_3 = np.hstack((a,b))
# print(a_b_3)

# a = np.arange(16).reshape(4, 4)
# #Split it into 2 parts row-wise and 2 parts column-wise.
# print(a)
# try:
#    a_1 = np.split(a,3,axis = 1)
#    print(a_1)
# except ValueError as e:
#     print(f'It is invalid value {e}')
# # a_2 = np.split(a,2,axis = 0)
# # print(a_2)
#


# scores = np.array([[91, 44, 75, 60],
#                    [30, 88, 95, 40],
#                    [70, 70, 70, 70]])
#
# # - print row-wise averages
# # - replace all FAIL scores (< 50) with 0 using np.where
# # - find the best student index
# # - find the highest score in the whole matrix.
# average = np.average(scores,axis = 1)
# Fail_scores = np.where(scores<50,0,scores)
# best_student = np.argmax(average)
# highest_score = scores.max()
# print(highest_score)


# def mean_array(arr):
#     assert len(arr) > 0
#
#     return np.mean(arr)
#
# data = np.array([])
# try:
#   print(mean_array(data))
# except AssertionError as e:
#     print(f'It is invalid value {e}')
#
# def scores_array(array):
#
#     if np.any((array<0) | (array>100)) :
#         raise ValueError
#     else:
#         return np.average(array,axis = 1)
#
# data = np.array([[1,2,3,4],
#                  [5,7,8,9],
#                  [10,11,12,13]])
# try:
#   print(scores_array(data))
# except ValueError   as e:
#     print(f'It is a invalid value {e}')



# user_input = input("Enter numbers: ")
# splittt = user_input.split(',')
# try :
#     numbers = np.array(splittt, dtype = int)
#     print(numbers)
# except ValueError as e:
#     print(f'it is a invalid value {e}')



# a = np.array([[1, 2],
#               [3, 4]])
# b = np.array([[5, 6],
#               [7, 8]])
#
# print(a@b)
# print(b@a)



# m = np.array([[2, 1],
#               [5, 3]])
# print(np.linalg.det(m))

# m = np.array([[4, 7,3],
#               [2, 6,2]])
# try:
#    print(np.linalg.inv(m))
# except ValueError as e:
#     print(f"It is not sqare matrix {e}")

# a = np.array([[3, 1],
#               [1, 2],
#               [1,2]])
# b = np.array([9, 8])
# try:
#   print(np.linalg.solve(a,b))
# except : try:
#     print("It is impossible")


# def func(arr1,arr2):
#     try:
#        return arr1+arr2
#     except ValueError:
#         raise ValueError("It is impossible")
#
#
# a = np.array([1,2,3])
# b = np.array([2,2,2,2])
# try:
#    print(func(a,b))
# except ValueError as e:
#     print(f"it is impossible {e}")
#
#

# v = np.array([3, 4])
# # Compute the norm using numpy.linalg.norm. Then explain why the result has that value.
# print(np.linalg.norm(v))













# matrices = [np.array([[1, 2],
#                       [3, 4]]),
#             np.array([[1, 2],
#                       [2, 4]]),
#             np.array([[2,0],
#                       [0, 2]])]
#
#
# for matrice in matrices:
#     print("Determinant: ", np.linalg.det(matrice))
#
#     try:
#         inv_m = np.linalg.inv(matrice)
#         print(inv_m)
#     except np.linalg.LinAlgError as e:
#         print(f'{e}')




# You must:
# 1. assert that the matrix is 2D
# 2. raise ValueError if any score is below 0 or above 100
# 3. compute row-wise averages
# 4. replace all values below 50 with 0 using np.where
# 5. find the best student index
# 6. compute each exam average with axis=0
# 7. count how many unique scores exist
# 8. print a final summary report.

#
# results = np.array([[91, 44, 75, 60],
#                     [30, 88, 95, 40],
#                     [77, 66, 59, 100],
#                     [55,55, 55, 55]])
#
# assert results.ndim == 2, "Matrix mast be 2D"
#
# if np.any(results<0) or np.any(results>100):
#     raise ValueError("Score mast be between 0 and 100")
#
# row_averages = np.mean(results, axis=1)
#
# modified_results = np.where(results<50, 0, results)
#
# best_student = np.argmax(row_averages)
#
# exam_average = np.mean(results,axis=0)
# unique_score = len(np.unique(results))
#
# print(row_averages)
# print(modified_results)
# print(best_student)
# print(exam_average)
# print(unique_score)




# def analyze_matrix(values):
#     if len(values) !=12:
#         raise ValueError("Values mast be 12")
#
#     matrix = np.array(values).reshape(3,4)
#     print(matrix)
#     print(matrix[1])
#     print(matrix[:,2:])
#     print(matrix[[0,0,2,2],[0,3,0,3]])
#     row_mean = np.mean(matrix,axis=1)
#     print(row_mean)
#     new_matrix = np.where(matrix<50, 0, matrix)
#     print(new_matrix)
#
#
#
# data = [48, 67, 72, 90, 55, 81, 39, 100, 24, 58, 77,22]
#
#
# try:
#     analyze_matrix(data)
# except ValueError as e:
#     print(f'{e}')



# grades_data = [45, 88, 92, 60, 75, 52, 95, 38, 81, 70, 84, 90, 58, 62, 79]


# def analyze_grades(data_list):
#     if not  isinstance(data_list,list) or len(data_list) !=15:
#         raise ValueError("Mast be 15 and list")
#
#     matrix = np.array(data_list).reshape(5,3)
#     print(matrix)
#     print(matrix[2])
#     print(matrix[3:,:2])
#     print(matrix[[0,0,4,4],[2,0,2,0]])
#     row_mean = np.mean(matrix, axis = 1)
#     print(row_mean)
#     column_max = np.argmax(matrix,axis = 0)
#     best_student = np.argmax(row_mean)
#     new_matrix = np.where(matrix<60, 0 , matrix)
#     print(new_matrix)
#
# grades_data = [45, 88, 92, 60, 75, 52, 95, 38, 81, 70, 84, 90, 58, 62, 79]
#
# analyze_grades(grades_data)




#data = [120, 85, 140, 200, 95, 110, 160, 130, 180, 70, 190, 210, 80, 105, 115, 175]


# def analyze_sales(sales_data):
#
#     if not isinstance(sales_data,list) or len(sales_data) != 16:
#         raise ValueError("Mast be list and the length mast be 16: ")
#
#     array = np.array(sales_data)
#
#     if np.any(array < 0):
#         raise ValueError("Sales data > 0")
#
#     matrix = array.reshape(4,4)
#     print("-"*20)
#     print(matrix)
#     print("-"*20)
#     print(matrix[:2,2:])
#     print("-" * 20)
#     print(matrix[[0,0,3,3],[0,3,0,3]])
#     row_sum = np.sum(matrix,axis=1)
#     print("-" * 20)
#     print(row_sum)
#     column_mean = np.mean(matrix,axis = 0)
#     print("-" * 20)
#     print(column_mean)
#     worst_shope = np.argmin(row_sum)
#     print("-" * 20)
#     print(worst_shope)
#     new_matrix = np.where(matrix<100, 100, matrix)
#     print("-" * 20)
#     print(new_matrix)
#     count_over_150 = np.sum(matrix>150)
#     print("*"*20)
#     print(count_over_150)
#
#
#
# data = "linux"
#
# try:
#     analyze_sales(data)
# except ValueError as e:
#     print(f'{e}')




# def analyze_temperatures(temp_list):
#
#     if not isinstance(temp_list,list) or len(temp_list) !=20:
#         raise ValueError("The temp_list mast be list and the length mast be 20:")
#
#     array = np.array(temp_list)
#
#     if np.any(array < -50) or np.any(array > 50):
#         raise ValueError("The numbers must be between -50 and 50:")
#
#     matrix = array.reshape(5,4)
#     print("*"*20)
#     print(matrix)
#     print("*" * 20)
#     print(matrix[2:,:2])
#     print("*" * 20)
#     print(matrix[[0,0,4,4],[0,3,0,3]])
#     row_mean = np.mean(matrix, axis=1)
#     print("*" * 20)
#     print(row_mean)
#     max_temp = np.max(matrix,axis = 0)
#     print("*" * 20)
#     print(max_temp)
#     cold_city = np.argmin(row_mean)
#     print("*" * 20)
#     print(cold_city)
#     new_matrix = np.where(matrix < 0, 0, matrix)
#     print("*" * 20)
#     print(new_matrix)
#     count_20 = np.sum(matrix > 20)
#     print("*" * 20)
#     print(count_20)
#
#
# data = temperatures = [
#     15, 15, 15, 15,
#     -5,  2,  8, 12,
#     25, 28, 30, 27,
#     10, 14, 16, 21,
#      3, -2,  5,  9
# ]
#
# try :
#     analyze_temperatures(data)
# except ValueError as e:
#     print(f'{e}')













# • Print the second row.
# • Print the third column.
# • Print only the scores that are greater than or equal to 70.
# • Use fancy indexing to extract only the corner elements.
# • Build a PASS / FAIL matrix with np.where, where score >= 50 becomes PASS and score < 50
# becomes FAIL.
# • Compute the average score for each student.
# • Find the index of the best student.

# scores = np.array([
#     [80, 45, 91, 60],
#     [55, 77, 39, 88],
#     [100, 62, 73, 40],
# ])
#
# print(scores[1])
# print(scores[:, 2])
# matrix = scores[scores >= 70]
# print(matrix)
# print(scores[[0, 0, 2, 2], [0, 3, 0, 3]])
# new_matrix = np.where(scores >= 50, 'Pass', 'Fail')
# print(new_matrix)
# average_score = np.average(scores, axis=1)
# print(average_score)
# best_student = np.argmax(average_score)
# print(best_student)





# • Reshape it into a (2, 3, 4) array.
# • Transpose the reshaped array so that the order of axes changes.
# • Flatten the array back to one dimension.
# • Write a short explanation of what each operation changes: reshape, transpose, and flatten.

# data = np.arange(24)
# array = data.reshape(2,3,4)
# # print(array)
# # print(array.T)
# print(array.flatten())











# • Create a vertical join of the two matrices.
# • Create a horizontal join of the two matrices.
# • Stack them into a 3D array.
# • Split the horizontally joined result back into two separate parts.
# • Print each result clearly: vertical join, horizontal join, 3D stack, left split, right split.


# a = np.array([[1, 2],
#               [3, 4]])
# b = np.array([[5, 6],
#               [7, 8]])
#
# # a_b = np.concatenate((a,b), axis = 0)
# # print(a_b)
# # a_b1 = np.concatenate((a,b), axis = 1)
# # # print(a_b1)
# # a_b3D = np.stack((a,b))
# # print(a_b3D)




# • Calculate the average score of each student using axis=1.
# • Find the index of the top student.
# • Use np.where to replace all scores below 50 with 0.
# • Find all unique scores.
# • Count how many unique scores there are.


# class_scores = np.array([
# [91, 44, 75, 60],# class_scores = np.array([
# [91, 44, 75, 60],
# [30, 88, 95, 40],
# [77, 66, 59, 100],
# ])
#
# average_score = np.mean(class_scores,axis = 1)
# # print(average_score)
# top_student = np.argmax(average_score)
# # print(top_student)
# new_scores = np.where(class_scores<50, 0, class_scores)
# # print(new_scores)
# unique_score = np.unique(class_scores)
# # print(unique_score)
# print(len(unique_score))
#

# [30, 88, 95, 40],
# [77, 66, 59, 100],
# ])
#
# average_score = np.mean(class_scores,axis = 1)
# # print(average_score)
# top_student = np.argmax(average_score)
# # print(top_student)
# new_scores = np.where(class_scores<50, 0, class_scores)
# # print(new_scores)
# unique_score = np.unique(class_scores)
# # print(unique_score)
# print(len(unique_score))







