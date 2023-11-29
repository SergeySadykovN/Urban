
# вписать имя и фамилию , определить  мужчина или женщина
name_1 = input('input name and fullname ')

print (name_1)

if name_1.isnumeric():
    print ('is not name')
elif name_1.isalpha():
    print('Thanks')
else:
    print('error')

    #проверка