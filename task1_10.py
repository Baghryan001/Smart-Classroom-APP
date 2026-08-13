# while True:
#   exam_1 = input("Enter the value of exam 1: ")
#   try:
#       exam_1 = int(exam_1)
#       break
#   except ValueError as e:
#       print(f'Error: {e}')
#
#
# while True:
#   exam_2 = input("Enter the value of exam 1: ")
#   try:
#       exam_2 = int(exam_2)
#       break
#   except ValueError as e:
#       print(f'Error: {e}')
#
#
# average_score = (exam_1 + exam_2)/2
#
#
# print(average_score)


# while True:
#     score = input("Enter the score: ")
#     try:
#         score = int(score)
#         break
#     except ValueError as e:
#         print('Error')
#
#
# if score >= 90:
#     print("Excellent")
# elif score >= 70:
#     print('Good')
# elif score >=50:
#     print('Pass')
# else:
#     print('Fail')


# x = 20
#
# while x >= 2:
#     if x % 2 == 0:
#         print(x)
#     x = x - 1



# data = [1,2,3,4,5,6,7]
#
# print(data[:4])
# print(data[-3:])
# print(data[1::2])


# location = (40.1234, 12.29029292)
# print(location[0])
# print(location[1])
#
# numbers = [1,2,1,2,2,1,3,4,3,5,5,4,56,7,8]
#
# numbers_unique = set(numbers)
# print(numbers_unique)


# data = {"name": 'Aram',
#         'scores': [80,90,100],
#         'city': 'New York'}
#
# average_score = (data['scores'][0] + data['scores'][1] +  data['scores'][2]) / 3
#
# print(data['name'])
# print(data['city'])
# print(average_score)



# def count_long_words(words,min_len):
#     count = 0
#     for word in words:
#         if len(word) >= min_len:
#             count += 1
#
#     return count
#
#
#
# print(count_long_words(['apple','cherry','age','apps'],5))


# votes = ['Ani','Aram','Ani','Anahit','Aram','Ani','Mariam']
#
# data_votes = {}
#
# for name in votes:
#     if name in data_votes:
#         data_votes[name] += 1
#     else:
#         data_votes[name] = 1
#
#
# max_value = 0
# winner = None
# for key,value in data_votes.items():
#     if max_value < value:
#         max_value = value
#         winner = key
#
# print(winner)


#
# import numpy as np
#
# def analyze_matrix(values):
#     if not isinstance(values,list) or len(values) != 12:
#         raise ValueError("The values mast be list ant the length mast be 12!!!")
#
#     matrix = np.array(values).reshape(3,4)
#     print(matrix)
#     print(matrix[1])
#     print(matrix[:,-2:])
#     print(matrix[[0,0,2,2],[0,3,0,3]])
#     row_mean = np.mean(matrix, axis = 1)
#     print(row_mean)
#     new_matrix = np.where(matrix < 50, 0, matrix)
#     print(new_matrix)
#
#
# data = [12,56,23,78,90,34,50,45,100,98,12,22]
#
# try:
#     analyze_matrix(data)
# except ValueError as e:
#     print(f'Error: {e}')




# import cv2
#
# def process_poster(image_path):
#     img = cv2.imread(image_path)
#     if img is None:
#         raise FileNotFoundError('Error:')
#     print('Img shape: ', img.shape)
#     img_resized = cv2.resize(img, (600,400))
#     img_gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
#     img_crop = img_resized[150:450,100:300]
#     img_not_red = img_resized.copy()
#     img_not_red[:,:,2] = 0
#     cv2.imwrite('poster_gray.jpg', img_gray)
#     cv2.imwrite('poster_crop.jpg', img_crop)
#     cv2.imwrite('poster_marked.jpg', img_not_red)
#
#     print(img_crop.shape)
#     cv2.imshow('poster_gray.jpg', img_gray)
#     cv2.imshow('poster_crop.jpg', img_crop)
#     cv2.imshow('poster_marked.jpg', img_not_red)
#     cv2.waitKey(0)
#     cv2.destroyWindow()
#
#
# try:
#     process_poster("red_picture.jpg")
# except FileNotFoundError:
#     print("Error....")
# except ValueError as e:
#     print(f'Error: {e}')



import pandas as pd

# data = [15, 22, 8, 40, 12, 33, 5, 18]
#
# data_series = pd.Series(data)
# print(data_series[data_series>15])

#
# data = [10, None, 30, None, 50]
# data_ser = pd.Series(data)
# average_data = data_ser.mean()
# data_ser = data_ser.fillna(average_data)
# print(data_ser)



# data = {
#     'Name': ['Anna','Bella','Artur','Anahit'],
#     'Age': [29,32,18,33],
#     'City': ['Yerevan','New York','Yerevan','Atenq']
# }
#
# df = pd.DataFrame(data)
# print(data_fr[['Name','City']])
# data_fr['Is_adult'] = data_fr['Age'] >=30
# print(data_fr)
# new_df = data_fr[(data_fr["City"] == 'Yerevan') & (data_fr['Age'] < 30)]
# print(new_df)


# data = {
#     "Category": ['Electronics', 'Clothing', 'Electronics', 'Clothing', 'Electronics'],
#      "Price"  : [300, 50, 500, 70, 150]
# }
#
# df = pd.DataFrame(data)
# #print(df)
# el_mean = df[(df['Category'] == 'Electronics')]['Price'].sum()
# print(el_mean)

