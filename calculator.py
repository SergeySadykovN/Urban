# math for arabic
def calculate_arabic(user_int_1, user_sign, user_int_2):

        if user_sign == '+':
            solved = float(user_int_1) + float(user_int_2)
            print(solved)
        elif user_sign == '-':
            solved = float(user_int_1) - float(user_int_2)
            print(solved)
        elif user_sign == '*':
            solved = float(user_int_1) * float(user_int_2)
            print(solved)
        elif user_sign == '/':
            solved = float(user_int_1) / float(user_int_2)
            print(solved)


calculate_arabic(user_int_1=input('Input first int '),
                 user_sign=input('Input math sign '),
                 user_int_2=input('Input second int '))

# data Roman
# roman_dict = {
#     "I": 1,
#     "II": 2,
#     "III": 3,
#     "IV": 4,
#     "V": 5,
#     "VI": 6,
#     "VII": 7,
#     "VIII": 8,
#     "IX": 9,
#     "X": 10,
#     "XX": 20,
#     "XXX": 30,
#     "XL": 40,
#     "L": 50,
#     "LX": 60,
#     "LXX": 70,
#     "LXXX": 80,
#     "XC": 90,
#     "C": 100,
# }
#
# user_input = input('Enter a number: ')
#
# for key, value in roman_dict.items():
#     if user_input == key:
#         print(value)
#         break
