class Car:
    color = None
class Motocicleta():
    color=None
def change_color(car, color):

    car.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()
motocicleta = Motocicleta()
change_color(car_1,"red")
change_color(car_2,"albastru")
change_color(car_3,"portocaliu")
change_color(motocicleta,"maro")
print(car_1.color)
print(car_2.color)
print(car_3.color)
print(motocicleta.color)