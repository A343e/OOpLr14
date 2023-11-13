import math

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)


# Пример использования полиморфных методов
point2d_a = Point2D(1, 2)
point2d_b = Point2D(4, 6)

point3d_a = Point3D(1, 2, 3)
point3d_b = Point3D(4, 6, 8)

# Вызываем полиморфные методы для нахождения расстояния
distance_2d = point2d_a.distance_to(point2d_b)
distance_3d = point3d_a.distance_to(point3d_b)

print(f"Расстояние между 2D точками: {distance_2d}")
print(f"Расстояние между 3D точками: {distance_3d}")