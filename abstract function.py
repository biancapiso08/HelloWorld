from abc import ABC, abstractmethod

class  Vehicul(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Masina(Vehicul):
    def go(self):
        print("Tu conduci masina")
    def stop(self):
        print("Aceasta maisna este oprita.")
class Motocicleta(Vehicul):
     def go(self):
         print("Tu conduci o motocicleta.")

     def stop(self):
         print("Aceasta motocicleta este oprita.")

#vehicul= Vehicul()
masina = Masina()
motocicleta = Motocicleta()

masina.go()
masina.stop()
motocicleta.go()
motocicleta.stop()