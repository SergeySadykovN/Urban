user_int_1 = input('Input first int ')
user_sign = input('Input math sign ')
user_int_2 = input('Input second int ')


#math for arabic
if user_sign == '+':
    slvd = float(user_int_1) + float(user_int_2)
    print(slvd)
elif user_sign == '-':
    slvd = float(user_int_1) - float(user_int_2)
    print(slvd)
elif user_sign == '*':
    slvd = float(user_int_1) * float(user_int_2)
    print(slvd)
elif user_sign == '/':
    slvd = float(user_int_1) / float(user_int_2)
    print(slvd)

