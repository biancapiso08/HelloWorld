#super() = functie cu ajutorul careia putem accesa metode din clasa parinte

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

class Squared(Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)
    def area(self):
        return self.length+self.width

class Cube(Rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height

squared = Squared(2,3)
cube = Cube(4,5,3)

print(squared.area(), end="   ")
print( cube.volume())
