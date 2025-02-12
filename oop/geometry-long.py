import math


class Point2D:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Point2D({self.x}, {self.y})"
    
    def __eq__(self, other):  # equality: p1 == p2
        return other is not None and all(hasattr(a, other) for a in ['x', 'y']) and self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))

    def __abs__(self): # magnitude: abs(p)
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __neg__(self): # negation: -p
        return Point2D(-self.x, -self.y)
    
    def __add__(self, other) -> 'Point2D': # addition: p1 + p2
        if not isinstance(other, Point2D):
            other = Point2D(other, other) # if other is a scalar, convert it to a point of equal coordinates
        return Point2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other) -> 'Point2D': # subtraction: p1 - p2
        return self + (-other) # implemented via addition and negation
    
    def __mul__(self, other): # multiplication: p1 * s
        if isinstance(other, Point2D):
            return self.x * other.x + self.y * other.y # dot product
        return Point2D(self.x * other, self.y * other) # scalar product
    
    def __truediv__(self, other: float) -> 'Point2D':
        return self * (1 / other) # implemented via multiplication

    def distance(self, other: 'Point2D') -> float:
        return abs(self - other) # implemented via subtraction and magnitude
    
    def angle(self, other: 'Point2D') -> float:
        diff = other - self
        return math.atan2(diff.y, diff.x)

    @staticmethod
    def centroid(points: list['Point2D']) -> 'Point2D':
        return sum(points, Point2D(0, 0)) / len(points)

    @classmethod
    def sort_anti_clockwise(cls, points: list['Point2D']) -> list['Point2D']:
        centroid = cls.centroid(points)
        def angle_wrt_center(p):
            return (p - centroid).angle(Point2D(1, 0))
        points = list(points)
        points.sort(key=angle_wrt_center)
        return points
        

class Shape:
    def surface(self) -> float:
        raise NotImplementedError()

    def perimeter(self) -> float:
        raise NotImplementedError()
    

class Circle(Shape):
    def __init__(self, center: Point2D, radius: float):
        self.center = center
        self.radius = float(radius)
        
    def surface(self) -> float:
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
    
    def __repr__(self):
        return f"Circle(center={self.center}, radius={self.radius})"
    
    def __eq__(self, other):
        return isinstance(other, Circle) and self.center == other.center and self.radius == other.radius

    def __hash__(self):
        return hash((self.center, self.radius))
    

class Polygon(Shape):
    def __init__(self, points: list):
        self.vertices = tuple(point if isinstance(point, Point2D) else Point2D(*point) for point in points)
        if len(self.vertices) < 3:
            raise ValueError("A polygon must have at least 3 vertices")
    
    def __repr__(self):
        return f"Polygon(vertices=[{', '.join(str(p) for p in self.vertices)}])"
    
    def __eq__(self, other):
        return isinstance(other, Polygon) and self.vertices == other.vertices
    
    def __hash__(self):
        return hash(self.vertices)
    

class Triangle(Polygon):
    def __init__(self, fst: Point2D, snd: Point2D, trd: Point2D):
        super().__init__(Point2D.sort_anti_clockwise([fst, snd, trd]))

    @property
    def a(self):
        fst, snd = self.vertices[:2]
        return fst.distance(snd)
    
    @property
    def b(self):
        snd, trd = self.vertices[1:]
        return snd.distance(trd)
    
    @property
    def c(self):
        fst, trd = self.vertices[::2]
        return fst.distance(trd)
        
    def __repr__(self):
        return super().__repr__().replace("Polygon", "Triangle")
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def surface(self):
        # cf. https://en.wikipedia.org/wiki/Heron%27s_formula
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


class Rectangle(Polygon):
    def __init__(self, a: Point2D, b: Point2D):
        bl = Point2D(min(a.x, b.x), min(a.y, b.y))
        tr = Point2D(max(a.x, b.x), max(a.y, b.y))
        super().__init__([bl, Point2D(tr.x, bl.y), tr, Point2D(bl.x, tr.y)])

    @property
    def bottom_left(self):
        return self.vertices[0]
    
    @property
    def bottom_right(self):
        return self.vertices[1]
    
    @property
    def top_right(self):
        return self.vertices[2]
    
    @property
    def top_left(self):
        return self.vertices[3]
    
    @property
    def width(self):
        return self.top_right.x - self.bottom_left.x
    
    @property
    def height(self):
        return self.top_right.y - self.bottom_left.y
    
    def __repr__(self):
        return f"Rectangle(bottom_left={self.bottom_left}, top_right={self.top_right})"
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def surface(self):
        return self.width * self.height
    

class Square(Rectangle):
    def __init__(self, corner: Point2D, side: float):
        super().__init__(corner, corner + side)
    
    def __repr__(self):
        return f"Square(bottom_left={self.bottom_left}, top_right={self.top_right})"

    @property
    def side(self):
        return self.width
        
        
if __name__ == "__main__":
    triangle = [Point2D(1, -1), Point2D(-1, -1), Point2D(0, 1)]
    print(Point2D.centroid(triangle))               # (0.0, -0.3333333333333333)
    print(Point2D.sort_anti_clockwise(triangle))    # [Point2D(0.0, 1.0), Point2D(-1.0, -1.0), Point2D(1.0, -1.0)]
    
    rectangle = [Point2D(-2, 1), Point2D(2, 1)]
    rectangle = rectangle + [-p for p in rectangle]
    print(Point2D.centroid(rectangle))              # (0.0, 0.0)
    print(Point2D.sort_anti_clockwise(rectangle))   # [Point2D(2.0, 1.0), Point2D(-2.0, 1.0), Point2D(-2.0, -1.0), Point2D(2.0, -1.0)]
    
    circle = Circle(Point2D(1, 1), 2)
    print(circle, circle.surface(), circle.perimeter()) # Circle(center=(1.0, 1.0), radius=2.0) 12.566370614359172 12.566370614359172
    
    triangle = Triangle(Point2D(1, -1), Point2D(-1, -1), Point2D(0, 1))
    print(triangle, triangle.surface(), triangle.perimeter()) # Triangle(vertices=[(0.0, 1.0), (-1.0, -1.0), (1.0, -1.0)]) 2.0 6.47213595499958
    
    rectangle = Rectangle(Point2D(2, -1), Point2D(-2, 1))
    print(rectangle, rectangle.surface(), rectangle.perimeter()) # Rectangle(bottom_left=(-2.0, -1.0), top_right=(2.0, 1.0)) 8.0 12.0
    
    square = Square(Point2D(-1, -1), 2)
    print(square, square.surface(), square.perimeter()) # Square(bottom_left=(-1.0, -1.0), top_right=(1.0, 1.0)) 4.0 8.0
