"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""


class Phone:
    brand: str
    model: str
    issue_year: int

    def __init__(self, brand: str, model: str, issue_year: int):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def receive_call(name: str):
        print(f'Звонит {name}')

    def get_info(self) -> tuple:
        phone_info = (self.brand, self.model, self.issue_year)
        return phone_info

    def __str__(self) -> str:
        return f"Бренд: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.issue_year}"


new_phone = Phone('Samsung', 'Galaxy S22', 2022)

Phone.receive_call('Alex --> I want a new phone Samsung')
print(new_phone)
print('phone_info -->', new_phone.get_info())
