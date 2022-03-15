class Colors:
    def __init__(self, name, r, g, b):
        self.name = name
        self.r = r
        self.g = g
        self.b = b


    def __str__(self):
        return f"{self.name} ({self.r},{self.g},{self.b})"

    def __eq__(self, other):
        if isinstance(other, Colors):
            return (self.r == other.r and
                    self.g == other.g and
                    self.b == other.b)
        return NotImplemented


red = Colors('красный', 255, 0, 0)
green = Colors('зелёный', 0, 255, 0)
otherRed = Colors('другой красный', 255, 0, 0)

print(otherRed)
print(red)
print(green)

print(red == green)
print(red == otherRed)

class Rect:
    def __init__(self,name, color, x, y):
        self.name = name
        self.color = color
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.name} ({self.color}, x = {self.x}, y = {self.y})"

    def __eq__(self, other):
        if isinstance(other, Rect):
            return (self.x == other.x and
                    self.y == other.y or
                    self.x == other.y and
                    self.y == other.x)
        return NotImplemented

rect_one = Rect("прямоугольник1", "красный", 50, 10)
rect_two = Rect("прямоугольник2", "синий", 20, 10)

print(rect_one)
print(rect_two == rect_one)





