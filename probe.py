# # def find_name(list_name):
# #     user_input = input('Enter name: ')
# #     for name in list_name:
# #         if name == user_input:
# #             print(f' is in list!')
# #             break
# #         else:
# #             print(input('Try another: '))
#
#
# def find_name(name_list, name):
#     for name in list_name:
#         if name == name:
#             return ('Ok!')
#     return 'Name not found'
#
#
# list_name = ['Serg', 'Anna', 'Igor', 'Lena']
# name = input('Enter your name: ')
# result = find_name(*list_name, name)
# print(result)
#
# # find_name(list_name)
import os
import time

# path = '/Users/9110226522g/Desktop'
# for dirs, files, filenames in os.walk(path):
#     for file in filenames:
#         filepath = os.path.join(dirs, file)
#         filetime = os.path.getatime(file)
#         time = time.strftime('%d-%m-%Y %H:%M', time.localtime(filetime))
#         filesize = os.path.getsize(file)
#
#         print(f'File: {file}, path: {filepath}, size: {filesize}, time: {time}')
path = r'/Users/9110226522g/Desktop'
filename = '/Users/9110226522g/Desktop/Снимок экрана 2023-12-17 в 18.27.12.png'
for file in os.listdir(path):
    file_path = os.path.join(path, filename)
    file_time = os.path.getatime(filename)
    time_normal = time.strftime('%d-%m-%Y %H:%M', time.localtime(file_time))

    file_parent = os.path.dirname(filename)
    print(filename,time_normal)

print('%'*40)]
print(filename)
