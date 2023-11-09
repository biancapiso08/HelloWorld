#Duck typing" este un concept în programare care se referă la abordarea în care tipul sau natura unui obiect este determinată mai mult de comportamentul său decât de tipul explicit. Ideea din spatele duck typing este că, "dacă arată ca o rață, sună ca o rață și se comportă ca o rață, atunci probabil este o rață

class Rata:
    def quack(self):
        print("Quack!")

    def walk(self):
        print("Walking like a duck")

class Gaina:
    def quack(self):
        print("Cluck!")
#   def cluck(self):
    #print("CLUCK!")
    def walk(self):
        print("Walking like a chicken")

def esterata(rața):
    rața.quack()
    rața.walk()

rața = Rata()
gaina = Gaina()

esterata(rața)  # Funcționează bine pentru obiectul de tip rață
esterata(gaina)  # Funcționează bine și pentru obiectul de tip găină, deoarece are metoda `quack()` și `walk()`
