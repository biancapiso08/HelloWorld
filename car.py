class Car:
    weels = 4
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This car" + self.make + "is driving")

    def stop(self):
        print("This car" +self.make + "is stopped.")



Car_1 = Car("Chevy", "Corvette", "2023", "black")
Car_2 = Car("Ford", "Focus", "2021", "blue")
print(Car_1.make)
print(Car_1.model)
print(Car_1.year)
print(Car_1.color)

Car_1.drive()
Car_2.stop()
print(Car_1.weels)
print(Car_2.weels)