# Открываем файл с латинскими и русскими символами и выводим в консоль (mode='r')
import io
import operator
import os
from itertools import count

poetry = 'poetry.txt'
file = open(poetry, mode='r', encoding='utf8')
content = file.read()
file.close()
# print(content)

# Создаем пустой файл и записываем латинские и русские символы (mode='w')
# file_name = 'out.txt'
# file = open(file_name, mode='w', encoding='utf8')
# content1 = 'Hello World!, Привет, мир! '
# file.write(content1)
# file.close()
#
# # Открываем файл, читаем и добавляем в конец символы (mode='a')
# file = open(poetry, mode='a', encoding='utf8')
# file_content = '\nPeace for everyone! '
# file.write(file_content)
# file.close()
#
# # Режим чтения и записи одновременно (mode='r+')
# file = open(poetry, mode='r+', encoding='utf8')
# content2 = file.read()
# file.write('\nNo  war!')
# file.close()

# Позиционный вывод
# file = open(poetry, mode='r', encoding='utf8')
#
# # new_position = file.seek(0, os.SEEK_CUR)
# file_content1 = file.read(37)#до какого номера символа считываем
# print(file_content1)
# print(file.tell()) #показывает на каком пот счету символе остановились
#
# file_content1 = file.read()
# print(file_content1)
# print(file.tell())


# with open(poetry, mode='r', encoding='utf8') as file:
#     file_content3 = file.read()
#     print(file_content3)

file_name = 'Poem about Winter.txt'
with open(file_name, mode='w', encoding='utf8') as file:
    content_add = ('Разукрасилась зима: На уборе бахрома \n'
                   'Из прозрачных льдинок, Звездочек-снежинок. \n'
                   'Вся в алмазах, жемчугах, В разноцветных огоньках, \n'
                   'Льет вокруг сиянье, Шепчет заклинанье: \n'
                   '— Лягте, мягкие снега, На леса и на луга  \n'
                   'Тропы застелите, Ветви опушите! На окошках, \n'
                   'Дед Мороз, Разбросай хрустальных роз \n'
                   'Легкие виденья, Хитрые сплетенья. \n'
                   'Ты, метелица, чуди, Хороводы заводи, \n'
                   'Взвейся вихрем белым В поле поседелом! \n'
                   'Спи, земля моя, усни, Сны волшебные храни: \n'
                   'Жди, в парчу одета, Нового рассвета!')
    file.write(content_add)

print(file.encoding, file.name, file.mode)

with open(file_name, mode='r', encoding='utf8') as file:
    file_content = file.read(20)
    symbol_count = {}
    for char in file_content:
        if char in symbol_count:
            symbol_count[char] += 1
        else:
            symbol_count[char] = 1

    print(symbol_count)

    new_position = file.seek(0, os.SEEK_SET)
    file_content = file.read(20)

with open(file_name, mode='r', encoding='utf8') as file:
    line = True
    while line:
        line = file.readline()
        if 'Дед' in line:
            print("word in line:", line)
            break
    else:
        print("not in file")

