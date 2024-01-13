class Building:
    '''Создайте новый класс Building с атрибутом total
    Создайте инициализатор для класса Building, который будет
    увеличивать атрибут количества созданных объектов класса Building total
    В цикле создайте 40 объектов класса Building и выведите их на экран командой print'''
    total = 0

    def __init__(self):
        Building.total += 1

    def __str__(self):
        return str(f'new building of the city, total buildings: {Building.total}')


city = []

for i in range(40):
    building = Building()
    city.append(building)
    print(Building.__str__(''))