
class Colors:
    def __init__(self, name, r, g, b):
        self.name = name
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return f"{self.name} ({self.r}, {self.g}, {self.b})"

    def __eq__(self, other):
        if isinstance(other, Colors):
            return (self.r == other.r and
                    self.g == other.g and
                    self.b == other.b)
        return NotImplemented

red = Colors('красный', 255, 0, 0)
green = Colors('зеленый', 0, 255, 0)
otherRed = Colors('другой красный', 255, 0, 0)

print(otherRed)
print(red)
print(green)

print(red == green)
print(red == otherRed)



class Figure:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.color

    @color.setter
    def color(self, c):
        self.__color = c

    def info(self):
        print('Figure')
        print('Color: + self.__color')

class Rectangle(Figure):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if w > 0:
            self.__width = w
        else:
            raise ValueError

    @property
    def height(self):
        return self.__height

    def height(self, h):
        if h > 0:
            self.__height = h
        else:
            raise ValueError

    def info(self):
        print('Rectangle')
        print('Color:' + self.color)
        print('Width:' + str(self.width))
        print('Height:' + str(self.he))
        print('Area:' + str(self.area()))

    def area(self):
        return self.__width * self.__height

fig = Figure('orange')
print(fig.info())

rect = Rectangle(10, 20, 'green')
print(fig.info())


class Computers:

    color = "black"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__isTurned = False

    def __str__(self):
        return f"Computer '{self.name}': {self.age} years, turned {self.isTurned}"

    @property
    def isTurned(self):
        return self.__isTurned

    @isTurned.setter
    def isTurned(self, i):
        if (i == 'on'):
            self.__isTurned = 'off'
        else:
            self.__isTurned = 'on'

    def powerOn(self):
        self.isTurned = not self.isTurned
        # Как-то вкл комп

    def getStatus(self):
        return self.__isTurned


comp1 = Computers('с-462-26', 6)
print(comp1)
comp1.isTurned = True
print(comp1.isTurned)
print(comp1.name)
