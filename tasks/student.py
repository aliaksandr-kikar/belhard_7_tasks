"""
Создать класс Student.

Определить атрибуты:

- surname - фамилия
- name - имя
- group - номер группы
- average_score - средний балл

Определить методы:

- инициализатор __init__
- Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
  студентов по среднему баллу

Создать список из 5 объектов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 5
"""


class Student:
    surname: str
    name: str
    group: int
    average_score: float

    def __init__(self, surname: str, name: str, group: int, average_score: float):
        self.surname = surname
        self.name = name
        self.group = group
        self.average_score = average_score

    def __eq__(self, other):
        return self.average_score == other.average_score

    def __ne__(self, other):
        return self.average_score != other.average_score

    def __lt__(self, other):
        return self.average_score < other.average_score

    def __gt__(self, other):
        return self.average_score > other.average_score

    def __le__(self, other):
        return self.average_score <= other.average_score

    def __ge__(self, other):
        return self.average_score >= other.average_score

    def __repr__(self):
        return f"{self.surname} {self.name}, гр.{self.group}, средний балл = {self.average_score}."


students = [
    Student('Кикар', 'Саша', 101213, 7.6),
    Student('Казак', 'Сергей', 101213, 4.8),
    Student('Гибок', 'Лена', 101218, 9.3),
    Student('Шнип', 'Дмитрий', 101218, 5.1),
    Student('Савчук', 'Ольга', 101211, 3.5)
]

print(sorted(students))

print(sorted(students, reverse=True))

good_students = [student for student in students if student.average_score > 5]
print(good_students)
