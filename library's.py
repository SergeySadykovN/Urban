from colorama import init, Fore, Back
from faker import Faker
from PIL import Image, ImageDraw, ImageFont,  ImageFilter
import requests
import json


# Пример работы Faker генерирует случайные персональные данные от ФИО до адреса
# cololrama помогает стилизовать вывод
faker = Faker("Ru")
name_list = []
count = 3
index = 0

while index < count:
    name_list.append((faker.first_name(), faker.last_name(), faker.phone_number()))
    index += 1

print(f'{Fore.WHITE}{Back.BLACK}{name_list}')


# Пример работы  библиотеки pillow

"""пример работы pillow
открываем картинку, добавляем текст на картинку, применяем фильтр"""
im = Image.open('download.jpg')
im = im.filter(ImageFilter.GaussianBlur)
draw = ImageDraw.Draw(im)
font = ImageFont.truetype('arial.ttf', 12)
draw.text((20,20), 'Создать массив '
                   '\nчисел с помощью библиотеки numpy, '
                   '\nвыполнить математические '
                   '\nоперации с массивом '
                   '\nи вывести результаты', (255,255,255), font=font)

im.show()
im.save('output.png')

'''пример работы requsts
вывел на консоль список моих репозиториев на гитхаб'''
url = 'https://api.github.com/users/SergeySadykovN/repos'
headers = {'Authorization': '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'}
response = requests.get(url, headers=headers)
repos = json.loads(response.content)

for repo in repos:
    print(repo['name'])
