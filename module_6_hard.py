# Дополнительное практическое задание по модулю: "Наследование классов."
# Задание "Они все так похожи":
import math
class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.__color = color # список цветов в формате RGB
        self.__sides = sides  # Список сторон целые числа
        self.filled = False   #закрашенный, bool
    def get_color(self):
        return self.__color
    def __is_valid_color(self, r, g, b): # корректность переданных значений
        for c in [r, g, b]:
            if isinstance(c, int) and 0 <= c <= 255:
                return True
            return False
    def set_color(self, r, g, b): # изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
    def __is_valid_sides(self, *sides): # если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим
        if len(sides) == self.sides_count:
            for side in sides:
                if isinstance(side, int) and side > 0:
                    return True
                return False
    def get_sides(self):
        return self.__sides
    def __len__(self):
        return sum(self.__sides) # должен возвращать периметр фигуры
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2*math.pi) # рассчитать исходя из длины окружности (одной единственной стороны)
    def get_square(self):
        return math.pi * (self.__radius ** 2)

class  Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
    def get_square(self):
        sides = self.get_sides()
        p = sum(sides) / 2
        return math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])) # площадь треугольника по формуле Герона


class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *sides ):
        super().__init__(color, *sides)
        self.__sides = [sides[0]] * self.sides_count # переопределение __sides
        print(self.__sides)
    def get_volume(self):
        v = self.get_sides()[0] ** 3
        return v # возвращает объём куба




circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())