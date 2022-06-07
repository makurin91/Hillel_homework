"""
Создать класс Vehicle который будет описывать аттрибуты свойственные ему.
Создать класс Bus который будет наследоваться от класса Vehicle
Создать класс Car который будет наследоваться от класса Vehicle

Вашей задачей, при формировании классов, будет достижение следующих целей
1)Общие методы и аттрибуты для Bus и Car имеет смысл определять в классе
Vehicle
2)Используйте модификаторы доступа для ваших аттрибутов
3)Используйте @property для отдельных аттрибутов(например для проверки типа)
"""


class Vehicle:
    def __init__(self, model_name, model_carcass, fuel_tank_volume, model_color):
        self.model_name = model_name
        self.model_carcass = model_carcass
        self.fuel_tank_volume = fuel_tank_volume
        self.__model_color = model_color
        self._vehicle_condition = None

    @property
    def condition(self):
        return f"{self.model_name} condition is: {self._vehicle_condition}"

    @condition.setter
    def condition(self, val):
        self._vehicle_condition = val


class Car(Vehicle):
    def __init__(self, model_name, model_carcass, fuel_tank_volume, model_color, sale):
        super().__init__(model_name, model_carcass, fuel_tank_volume, model_color)
        self.sale = sale

    @property
    def for_sale(self):
        return f"The car is up for sale: {self.sale}"


class Bus(Vehicle):
    def __init__(self, model_name, model_carcass, fuel_tank_volume, model_color, fuel_type):
        super().__init__(model_name, model_carcass, fuel_tank_volume, model_color)
        self.fuel_type = fuel_type

    def check_type_fuel(self):
        if self.fuel_type == 'petrol':
            return "not economical transport"
        elif self.fuel_type == 'gas':
            return "economical transport"
        return "Something went wrong"


car1 = Car('bmw', 'hatchback', 60, 'black', True)
car1.condition = 'new'
print(car1.condition)
print(car1.for_sale)

car2 = Car('mercedes', 'coupe', 85, 'white', False)
car2.condition = 'used'
print(car2.condition)


bus = Bus('toyota', 'van', 100, 'green', 'petrol')
bus.condition = 'used'
print(bus.condition)
print(bus.check_type_fuel())
