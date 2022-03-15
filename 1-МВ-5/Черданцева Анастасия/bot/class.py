class Colors:
    def __init__(self, name, r,g, b):
        self.name=name
        self.r=r
        self.g=g
        self.b=b

    def __str__(self):
        return f"{self.name} ({self.r}, {self.g}, {self.b})"

    def __eq__(self, other):
        if isinstance(other, Colors):
            return (self.r==other.r and
                    self.g==other.g and
                    self.b==other.b)
        return NotImplemented

red=Colors('red', 255,0,0)
green=Colors('green',0,255,0)
otherRed=Colors('other red', 255,0,0)

print(otherRed)
print(red)
print(green)

print(red==green)
print(red==otherRed)


class Figure:
    def __init__(self, color):
        self._color = color

    def color(self):
        return self._color

    def color(self, c):
        self._color=c

    def info(self):
        print("Figure")
        print("Color: " + self._color)

class Rectangle(Figure):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.__width=width
        self.__height=height

    def width(self):
        return self.__width

    def width(self, w):
        if w>0:
            self.__width=w
        else:
            raise ValueError

    def height(self):
        return self.__height

    def height(self, h):
        if h>0:
            self.__height=h
        else:
            raise ValueError

    def info(self):
        print("Rectangle")
        print("Color: " + self.color)
        print("Width: "+str(self.width))
        print("Height: " + str(self.height))
        print("Area: "+str(self.area()))

    def area(self):
        return self.__width*self.__height

fig=Figure("Orange")
print(fig.info())

rect=Rectangle(10,20,"Green")
rect.info()
