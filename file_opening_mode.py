# Открываем файл с латинскими и русскими символами и выводим в консоль (mode='r')
poetry = 'poetry.txt'
file = open(poetry, mode='r', encoding='utf8')
content = file.read()
file.close()
print(content)

# Создаем пустой файл и записываем латинские и русские символы (mode='w')
file_name = 'out.txt'
file = open(file_name, mode='w', encoding='utf8')
content1 = 'Hello World!, Привет, мир! '
file.write(content1)
file.close()

# Открываем файл, читаем и добавляем в конец символы (mode='a')
file = open(poetry, mode='a', encoding='utf8')
file_content = '\nPeace for everyone! '
file.write(file_content)
file.close()

# Режим чтения и записи одновременно (mode='r+')
file = open(poetry, mode='r+', encoding='utf8')
content2 = file.read()
file.write('\nNo  war!')
file.close()

