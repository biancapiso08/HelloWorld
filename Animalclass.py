class Aminal :
    alive = True
    def sleep(self):
        print("This aminal are sleeping")
    def eat(self):
        print("This animal are eating")

class Rabbit(Aminal):
    def run(self):
        print("THis animal are running")
class Cow(Aminal):
    pass
class Fish(Aminal):
    def swim(self):
        print("This animal are swiming")

rabbit = Rabbit()
cow = Cow()
fish = Fish()

#print(rabbit.alive)
#fish.sleep()
#cow.eat()

rabbit.run()
fish.swim()
cow.sleep()