import math
from typing import Sized


class Point2D:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Point2D({self.x}, {self.y})"
    
    def __eq__(self, other):
        return other is not None and all(hasattr(a, other) for a in ['x', 'y']) and self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def distance(self, other: 'Point2D') -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    
    def angle(self, other: 'Point2D') -> float:
        return math.atan2(other.y - self.y, other.x - self.x)
    
    def __add__(self, other: 'Point2D') -> 'Point2D':
        if not isinstance(other, Point2D):
            other = Point2D(other, other)
        return Point2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: 'Point2D') -> 'Point2D':
        if not isinstance(other, Point2D):
            other = Point2D(other, other)
        return Point2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other: float) -> 'Point2D':
        return Point2D(self.x * other, self.y * other)
    
    def __truediv__(self, other: float) -> 'Point2D':
        return Point2D(self.x / other, self.y / other)
    
    @staticmethod
    def ensure_points(points: Sized) -> list:
        return [point if isinstance(point, Point2D) else Point2D(*point) for point in points]
    
    @classmethod
    def center(cls, points: Sized) -> 'Point2D':
        points = cls.ensure_points(points)
        return sum(points, Point2D(0, 0)) / len(points)
    
    @classmethod
    def anti_clockwise(cls, points: Sized) -> bool:
        points = cls.ensure_points(points)
        center = Point2D.center(points)
        def angle_with_center(p):
            return (p - center).angle(Point2D(0, 1))
        points = list(points)
        points.sort(key=angle_with_center)
        return points


class Shape:
    def surface(self) -> float:
        raise NotImplementedError()

    def perimeter(self) -> float:
        raise NotImplementedError()
    

class Circle(Shape):
    def __init__(self, center: Point2D, radius: float):
        self.center = Point2D.ensure_points([center])[0]
        self.radius = float(radius)
        
    def surface(self) -> float:
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
    
    def __repr__(self):
        return f"Circle(center={self.center}, radious{self.radius})"
    
    def __eq__(self, other):
        return isinstance(other, Circle) and self.center == other.center and self.radius == other.radius

    def __hash__(self):
        return hash((self.center, self.radius))
    

class Polygon(Shape):
    def __init__(self, points: list):
        self.__points = [point if isinstance(point, Point2D) else Point2D(*point) for point in points]
        if len(self.__points) < 3:
            raise ValueError("A polygon must have at least 3 points")
        
    @property
    def points(self):
        return list(self.__points) # defensive copy
    
    def __len__(self):
        return len(self.__points)
    
    def __getitem__(self, index):
        return self.__points[index]
    
    def __iter__(self):
        return iter(self.__points)
    
    def perimeter(self) -> float:
        result = self.__points[-1].distance(self.__points[0])
        for i in range(1, len(self.__points)):
            result += self.__points[i - 1].distance(self.__points[i])
        return result
    
    def surface(self) -> float:
        # cf. https://en.wikipedia.org/wiki/Shoelace_formula
        result = 0
        for i in range(len(self.__points)):
            current = self.__points[i]
            next = self.__points[(i + 1) % len(self.__points)]
            result += abs(current.y + next.y) * abs(current.x - next.x)
        return 0.5 * result
    
    def __repr__(self):
        return f"Polygon([{', '.join(str(p) for p in self.__points)}])"
    
    def __eq__(self, other):
        return isinstance(other, Polygon) and self.__points == other.__points
    
    def __hash__(self):
        return hash(tuple(self.__points))
    

class Triangle(Polygon):
    def __init__(self, a: Point2D, b: Point2D, c: Point2D):
        super().__init__(Point2D.anti_clockwise([a, b, c]))

    @property
    def a(self):
        return self[0]
    
    @property
    def b(self):
        return self[1]
    
    @property
    def c(self):
        return self[2]
        
    def __repr__(self):
        return f"Triangle(a={self[0]}, b={self[1]}, c={self[2]})"


class Rectangle(Polygon):
    def __init__(self, a: Point2D, b: Point2D):
        a, b = Point2D.ensure_points([a, b])
        bl = Point2D(min(a.x, b.x), min(a.y, b.y))
        tr = Point2D(max(a.x, b.x), max(a.y, b.y))
        super().__init__([bl, Point2D(tr.x, bl.y), tr, Point2D(bl.x, tr.y)])

    @property
    def bottom_left(self):
        return self[0]
    
    @property
    def bottom_right(self):
        return self[1]
    
    @property
    def top_right(self):
        return self[2]
    
    @property
    def top_left(self):
        return self[3]
    
    @property
    def width(self):
        return self.top_right.x - self.bottom_left.x
    
    @property
    def height(self):
        return self.top_right.y - self.bottom_left.y
    
    @property
    def center(self):
        return (self.bottom_left + self.top_right) / 2
    
    def __repr__(self):
        return f"Rectangle(bottom_left={self.bottom_left}, top_right={self.top_right})"
    

class Square(Rectangle):
    def __init__(self, a: Point2D, l: float):
        a = Point2D.ensure_points([a])[0]
        super().__init__(a, a + l)
    
    def __repr__(self):
        return f"Square(bottom_left={self.bottom_left}, top_right={self.top_right})"

    @property
    def side(self):
        return self.width
