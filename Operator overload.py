class Building:
    '''Создайте новый класс Buiding
    Создайте инициализатор для класса Buiding, который будет задавать
    целочисленный атрибут этажности self.numberOfFloors и строковый атрибут self.buildingType
    Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения'''
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = int(numberOfFloors)
        self.buildingType = str(buildingType)

    def __eq__(self, other):
        return self.numberOfFloors == other


firstBuilding = Building(10, 'simple building')
secondBuilding = Building(100, 'skyscraper')
thirdBuilding = Building(10, 'simple building')
fourthBuilding = Building(10, 'not simple building')

#  обращение к методу класса  через __eq__
if Building.__eq__(firstBuilding, thirdBuilding):
    print('identical')
else:
    print('not identical!')

# прямое сравнение экземпляров
if firstBuilding == secondBuilding:
    print('equal')
else:
    print('not equal!')
