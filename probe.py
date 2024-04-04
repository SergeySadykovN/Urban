# # # def find_name(list_name):
# # #     user_input = input('Enter name: ')
# # #     for name in list_name:
# # #         if name == user_input:
# # #             print(f' is in list!')
# # #             break
# # #         else:
# # #             print(input('Try another: '))
# #
# #
# # def find_name(name_list, name):
# #     for name in list_name:
# #         if name == name:
# #             return ('Ok!')
# #     return 'Name not found'
# #
# #
# # list_name = ['Serg', 'Anna', 'Igor', 'Lena']
# # name = input('Enter your name: ')
# # result = find_name(*list_name, name)
# # print(result)
# #
# # # find_name(list_name)
# import os
# import time
#
#
# # path = '/Users/9110226522g/Desktop'
# # for dirs, files, filenames in os.walk(path):
# #     for file in filenames:
# #         filepath = os.path.join(dirs, file)
# #         filetime = os.path.getatime(file)
# #         time = time.strftime('%d-%m-%Y %H:%M', time.localtime(filetime))
# #         filesize = os.path.getsize(file)
# #
# #         print(f'File: {file}, path: {filepath}, size: {filesize}, time: {time}')
# # path = r'/Users/9110226522g/Desktop'
# # filename = '/Users/9110226522g/Desktop/Снимок экрана 2023-12-17 в 18.27.12.png'
# # for file in os.listdir(path):
# #     file_path = os.path.join(path, filename)
# #     file_time = os.path.getatime(filename)
# #     time_normal = time.strftime('%d-%m-%Y %H:%M', time.localtime(file_time))
# #
# #     file_parent = os.path.dirname(filename)
# #     print(filename,time_normal)
# #
# # print('%'*40)]
# # print(filename)
#
# def square(n):
#     return n * n
#
#
# numbers_list = [2, 7, 5, 7, 11, 13, 13, 19, 22, 29]
# squares_numb = map(square, numbers_list)
#
# for number in squares_numb:
#     print(f'The square of {number} is {list(squares_numb)}')
#
# squared_list = [square(number) for number in numbers_list]
# print(list(squared_list))
# class InvalidDataException(Exception):
#     pass
#
#
# class ProcessingException(Exception):
#     pass
#
#
# def generate_exc(arg):
#     if arg < 0:
#         raise InvalidDataException('arg is a negative value')
#     elif arg == 0:
#         raise ProcessingException('arg is a zero value')
#     else:
#         print('Sorry, but not generate exception today :(')
#
#
# def process_data(arg):
#     try:
#         generate_exc(arg)
#     except InvalidDataException as e:
#         print(f'invalid data exception {e}')
#         raise
#     except ProcessingException as e:
#         print(f'processing exception {e}')
#         raise
#
#
# try:
#     process_data(-1)
# except InvalidDataException:
#     print('invalid data exception')
#
# try:
#     process_data(0)
# except ProcessingException:
#     print('processing exeption')
#
# try:
#     process_data(3)
# except Exception:
#     print('not handled')

from datetime import time, datetime


# print(time.gmtime(0))
month = datetime.now()
find = month.month
hour = int(time[:-2])
print(hour)


seasons = {
            'Winter': (11, 0, 1),
            'Spring': (2, 3, 4),
            'Summer': (5, 6, 7),
            'Autumn': (8, 9, 10)
        }
for i, j in seasons.items():
    if j.count(find):
        print(i)


