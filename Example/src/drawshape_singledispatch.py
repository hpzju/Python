from functools import singledispatch


class Shape:

    def __init__(self):
        pass


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x},{self.y})'


class Rectangle(Shape):

    def __init__(self, w, h, center=Point(0, 0)):
        self.width = w
        self.height = h
        self.center = center

    def __repr__(self):
        return f'Rectangle({self.width},{self.height}, center={self.center})'


class Triangle(Shape):

    def __init__(self, pa, pb, pc, center=Point(0, 0)):
        self.a = pa
        self.b = pb
        self.c = pc
        self.center = center

    def __repr__(self):
        return f'Triangle({self.a},{self.b}, {self.c}, center={self.center})'


class Circle(Shape):

    def __init__(self, radius, center=Point(0,0)):
        self.center = center
        self.radius = radius

    def __repr__(self):
        return f'Circle({self.radius}, center={self.center})'


@singledispatch
def draw(shape):
    print(f"Draw generic {type(shape).__name__}")


@draw.register(Circle)
def _(shape):
    print(f"Draw Circle: {shape}")


@draw.register(Rectangle)
def _(shape):
    print(f"Draw Rectangle: {shape}")


@draw.register(Triangle)
def _(shape):
    print(f"Draw Triangle: {shape}")


if __name__ == '__main__':
    shapes = (Shape(), Point(1,2), Rectangle(2,10), Triangle(3, 4, 5), Circle(4))
    for item in shapes:
        draw(item)
