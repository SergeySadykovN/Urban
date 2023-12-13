from colorama import init, Style, Fore, Back
from faker import Faker

faker = Faker("Ru")
name_list = []
count = 3
index = 0

while index < count:
    name_list.append((faker.first_name(), faker.last_name(), faker.phone_number()))
    index += 1
print(Fore.GREEN + "\n" + Style.BRIGHT + "Name list is: " + str(name_list))





