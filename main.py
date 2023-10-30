
#firt_name ="Bro"
#last_name="Code"
#full_name=firt_name+last_name

#print("Hello  "+full_name)

#age= 21
#age+=1
#print(age)
#print(type(age))
#print("My age is"+ str(age))

#height=250.5
#print(str(height))
#print(type(height))

#name=input("What is your name:  " )
#print("Hello" + name)

#age=int(input("How old are you?  "))
#age= age+1
#print("I am"+str(age))

#import math

#pi=3.14
#x=1
#y=2
#z=3

#print(round(pi))
#print(math.floor(pi))
#print(math.log10(pi))
#print(math.exp2(pi))
#print(pow(pi,-3))
#print(math.sqrt(pi))
#print(max(pi,x,y,z))

#name="Pisoschi Bianca"
#first_name= name[::4]
#reversed_name=name[::-1]
#print(reversed_name)

#website= "http://google.com"
#slice=slice(7,-4)
#print(website[slice(7,-4)])


#age=int(input("How old are you?:  "))

#if age==100:
#    print("You are a century old!")
#elif age>=18:
 #   print("You are an adult.")
#elif age<0:
 #   print("You have`n been born yet")

#else:
 #   print("You are a child!")

#temp=int(input("Ce temperatura este afara?: "))

#if temp >= 0 and temp <= 30:
 #   print("The temp is good today")
  #  print("So outside!")
#elif not(temp<0 or temp>30) :
 #   print("Is nor good today.STay home!")


#While loop =bucla care se executa atata timp cat se indeplineste conditia

#while 1==1:
 #  print("Hel! I`m stuck a loop!")

#name= None
#while not name:
#    name=input("Enter your name")
#    print("Hello"+name)




#for loop= este o bucla limitat

#for i in range(10):
#   print(i)
#for i in "Bro Code":
 #   print(i)
#for i in range(50,101,2):
 #   print(i)

#TEMPORIZATOR DE NUMARATOARE INVERSA

#import time
#for seconds in range(60,0,-1):
#     print(seconds)
#     time.sleep(1)
#print("Happy New Year")


#nested loops= a avea o bucla in interiorul altei bucle
#rows=int(input("How many rows?:"))
#columns=int(input("How many colums?:"))
#symbol=input("Hoe many simbols?:")
#for i in range(rows):
#    for j in range(columns):
#       print(symbol, end="")
#    print()

#Controlul buclei:
# break= utilizat pt a termina bucla in intregime
#continue = trece peste urmatoarea iteratie a buclei
#pass= actioneaza ca substituient

#while True:
   # name=input("Enter your name: ")
   # if name != "":
   #     break


#phone_number= "123-456-7890"
#for i in phone_number:
#    if i == "-":
#        continue
#   print(i, end=" ")


#for i in range(0,20+1):
#     if i == 13:
#         pass
#     else:
#        print(i)


#list = utilizeaza mai multe valori intr o variabila
#food=["pizza","hamburger","hotdog","spaghetti"]
#food[0]="sushi"
#food.append("Choco")
#food.remove("hotdog")
#food.sort()
#food.insert(1, "paste")
#print(food)

#2D list= o lista cu liste
#drinks=["coffe","juice","tea"]
#dinner=["pizza","hamburger","hotdog"]
#dessert=["cake","pankchakes"]
#food=[drinks,dessert,dinner]
#print(food[2][1])

#tuple= colectii ordonate si neschimbabile
#student=("Bianca","24","female")
#print(student.count("Bianca"))
#print(student.index("female"))
#for x in student:
 #   print(x)
#if "24" in student:
 #   print("24 is Here!")

 #set= colectie neordonata, neindexata, nu permite aceleasi valori
#ustensile={"furculita","cutit","lingura","lingura","lingura"}
#dishes={"bol","farfurie","castron","furculita"}
#ustensile.add("lingurita")
#ustensile.remove("cutit")
#ustensile.clear() #curata setul
#ustensile.update(dishes) #schimba setul ustensile cu dishes
#dishes.update(ustensile) #invers
#dinner_table=ustensile.union(dishes) #creaza un nou set cu cele 2
#for x in dinner_table:
 #    print(x)
#print(ustensile.difference(dishes)) #setul cu ce are dishes si nu are ustensile
#print(ustensile.intersection(dishes))

 #dictionary=colectie neordonata, schimbatoare de perechi, valori cheie unice
#capitals={'USA':'Washington DC',
 #         'India':'New Dehli',
  #        'China':'Beijing',
   #       'Russia':'Moscova'
    #      }

#print(capitals['Russia'])
#print(capitals.get('Germany')) #Verificam daca exista o cheie in dictionar
#print(capitals.keys()) #afisam cheile
#print(capitals.values()) #afisam valoarea cheilor
#print(capitals.items()) #afisam intregul dictionar
#for key,value in capitals.items():
#    print(key,value)
#capitals.update({'Germany':'Berlin'})
#capitals.update({'Russia':'Kiev'})
#capitals.pop('China')
#apitals.clear()
#for key,value in capitals.items():
#   print(key,value)


#index operator [] = ofera acces la un element al unei secvente
#name="pisoschi Bianca."
#if(name[0].islower()): #aici verificam daca prima litera din secventa este mica
 #   name=name.capitalize() #aceasta functie face prima litera MARE restul mici
#first_name=name[0:8] #avem o variabila noua si un index care selecteaza PISOSCHI
#last_name=name[9:]
#last_character=name[-1]
#print(first_name.upper(), last_name.lower())#upper face scrisul mare
#print(last_character)

#function= un bloc de cod este executat doar atunci cand il apelam
#def hello(first_name,last_name,age,adjectiv): #declaram functia si ii dam parametrii
#    print("hello " +first_name+" "+last_name) #aici ii spunem functiei ce sa faca si ii damm parametrii
#    print("you are "+str(age)+" years old")
#    print("You are "+ adjectiv+" person")
#    print("Have a nice day!")
#hello("Pisoschi","Bianca","24", "pretty") #apelam functia si dam o valoare parametrilor

#return statement= aceasta functie este folosita in cadrul functiilor pentru a trimite valorile sau obiectele inapoi apelantului
#def multiply(number1,number2):
   # result=number1*number2
   # return result
   #SAU putem scrie pe o singura linie
#   return number1*number2
#x=multiply(2,3) #stocam valoarea intr-o variabila
#print(x)

#nested function calls= apeluri de functii in interiorul altor apele de functii.....
                    #unele din aceste functii returneaza o valoare iar noi putem folosi imediat valoarea respectiva in alta functie
#num=input("enter a wholw position number: ") #cerem utilizatorului sa introduca un numar si stochez in variabila num
#num=float(num) #convertim la float
#num=abs(num) #gasesc valoarea absoluta
#num=round(num) #rotunjesc
#print(num)
#SAU
#print(round(abs(float(input("enter a wholw position number: ")))))

#scope=domeniul in care o functie este recunoscuta
    #o variabila poate fi creata in scop local(in interiorul unei functii) sau global in exterior

#nume="pisoschi" #variabila globala
#def display_name():
 #    nume="Bianca" #variabila locala
  #   print(nume)
#display_name()
#print(nume)

# *args= parametru care impacheteaza toate argumentele intr-un tuplu
        #e necesar ca o functie sa accepte o cantitate variabila de argumente

#def suma(*arg): #* ne ajuta sa dam cate numere vrem
#    sum=0
#   arg=list(arg) #facem arg ca o lista
#    arg[5]=0    #schimbam valoarea unui indice
#    for i in arg:
#        sum+=i
#    return(sum)
#print(suma(1,2,3,4,5,6))

# **kwargs = parametru care impacheteaza toate argumentele in dictionar

#def hello(**kwargs):
#    print("Hello", end=" ") #end face ca printarea sa fie pe acelasi rand
#    for key,value in kwargs.items(): #dictionarul are 2 parametrii key si value
#        print(value)
#hello(tittle='Mrs.', first_name='Pisoschi', last_name='Bianca')

# str.format() = metoda pt siruri de caractere prin care utilizatorul poate controla ce apare pe iesire
#Folosim {} ca substituient al valorii..iar apoi punem .format(argumente) sau putem pune indexul intre acolade gen {0},{1}
#number = 1000
#print("The number pi is {:.3f}".format(number)) #:.3f adica printeaza 3 cifre dupa virdula
#print("The number is {:,}".format(number)) #pune virgula
#print("The number is {:b}".format(number)) #afiseaza nr ca binar
#print("The numbert is {:o}".format(number)) #afiseaza in octal
#print("The number is {:X}".format(number)) #afiseaza in hexazecimal
#print("The number is {:E}".format(number))#afiseaza in notatie stiintifica


import random

#x = random.randint(1,6) #Dam o valoare random intre 1 si 6
#y=random.random() #random intre 0 si 1
#list=['mere','pere','nuci']
#cards = [1,2,3,4,5,6,7,8,9,"J","K","Q","A"]
#random.shuffle(cards) #Amesteca valorile din lista
#print(cards)
#print(random.choice(list)) #returnam un element random din lista

# exception= eveniment detectat in timpul executiei care intrerupe fluxul normal al uinui program
#try:
#    numarator=int(input("Enter a number ti divide: "))
#    numitor=int(input("Enter a numbet to divide by: "))
#    result=numarator/numitor

#except ZeroDivisionError as e:
#    print(e)
#    print("NU POTI IMPARTI NUMARATORUL LA ZEROOO"
#    )
#except Exception:
#    print("Something went wrong!!") #ACeasta excetie face ca programul sa ruleze si sa nu fie intrerupt
#except ValueError:
#    print("Introdu doar numere!!")
#else:
#   print(result)
#finally:
#    print("This will always execute")

#DETERCTIE DE FISIERE
#import os
#path="C:\\Users\\Bianca\\Desktop\\pht.txt" #Calea catre fisier

#if os.path.exists(path): #Verificam daca aceasta cale exista
 #   print("That loction exist!")
#    if os.path.isfile(path): #verificam daca reda un fisier calea nostra
#        print("This is a file")
#    elif os.path.isdir(path): #Verificam daca este un director
#        print("This is a dir")
#else:
#    print("This location doesn`t exist!")


#CITIREFISIER
#try:
#    with open('test.txt') as file:  #cu aceasta deschidem fisierul
#        print(file.read())
#except FileNotFoundError:
#    print(file.close())

#SCRIEREINFISIER
#text="YPPPPPPPPPPPPPP\n"
#with open('test.txt', 'w') as file: #@aici daca punem w stergem si scriem...daca punem a scriem pe langa ce este
 #   file.write(text)

#try:
#    with open("date_personale.txt") as file:
#      print(file.read())
#except FileNotFoundError:
#    print("File not exist!")
#else: file.close()
#text=("Detalii")
#with open("date_personale.txt","a") as file:
#    file.write(text)

#COPYFILE
# copyfile()= copiaza continutul fisierului
# copy() = copyfile+ permisiuni+ destinatia poate fi un director
# copy2() = cop() + copy metadata

#import shutil
#shutil.copy2('test.txt','copy.txt',  )  #src,dst


#MOVEAFILE

import os
source = "Pa.txt"
destination="C:\\Users\\Bianca\\Desktop\\pa.txt"

#try:
#    if os.path.exists(destination):
#        print("File Exist.")
#    else:
#        os.replace(source,destination)
#        print(source+"FIle moved")
#except FileNotFoundError as e:
#    print(e)
#   print(source+"not found")

#DELETE A FILE
#import os
#import shutil

#path = 'folder'
#try:
   # os.remove(path) #STERGEM FISIER
   # os.rmdir(path)  #STERGEM FOLDER GOL
   #  shutil.rmtree(path) #STERGEM FOLDER PLIN
#except FileNotFoundError:
#    print("That file not found!")
#except PermissionError:
#    print("You are not acces!")
#except OSError:
#    print("NOT PERMISSION")
#else:
#    print("File deleted")

# MODULE = fisier care contine cod python. POate contine functii, clase, etc/
#import messages as msg
#msg.hello()
#msg.bye()
#SAU
#from messages import hello,bye
#hello()
#bye()
#help("modules")

##OOP
from car import Car

Car_1 = Car("Chevy","Corvette","2023","black")
Car_2 = Car("Ford","Focus","2021","blue")
print(Car_1.make)
print(Car_1.model)
print(Car_1.year)
print(Car_1.color)

Car_1.drive()
Car_2.stop()