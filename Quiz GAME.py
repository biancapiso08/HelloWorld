#Jocul presupune să răspunzi la întrebări alegând din opțiunile A, B, C și D și să obții un scor în funcție de câte răspunsuri corecte ai dat.
def new_game():
    guesses = [] #Lista care stocheaza raspunsurile utilizatorului
    correct_guesses = 0 #Variabila care urmareste cate raspunsuri corecte a dat utilizatorul
    questions_num = 1 #Tine evidenta numarului de intrebari

    for key in questions: #Parcurgem bucla for pentru fiecare intrebare din dictionarul questions
        print("-------------------")
        print(key) #Afisam intrebarea
        for i in options[questions_num-1]: #Parcurgem bucla for pentru raspunsul din dictionarul options
            print(i) #Printam raspunsurile
        guess = input("Enter (A,B,C,D): ") #Utilizatorul este nvitat sa aleaga una din variante
        guess = guess.upper() #Transformam raspunsul il litere mari
        guesses.append(guess) # Adaugam raspunsul il lista guesses pt a-l urmari

        correct_guesses += check_answer(questions.get(key),guess) #Cu aceasta functie verificam daca raspunsul este corect și se adaugă 1 la correct_guesses dacă răspunsul este corect.
        questions_num += 1 #questions_num se incrementează pentru a trece la următoarea întrebare

    display_score(correct_guesses,guesses) #După ce s-au răspuns la toate întrebările, se apelează funcția display_score pentru a afișa scorul final.

def check_answer(answer, guess): #Funcția check_answer primește răspunsul corect și răspunsul utilizatorului și verifică dacă sunt la fel.
    if answer == guess:
        print("Correct")
        return 1 # Dacă sunt egale, se afișează "Correct" și funcția returnează 1
    else:
        print("Wrong")
        return 0 #altfel se afișează "Wrong" și funcția returnează 0.


def display_score(correct_guesses,guesses): #Funcția display_score afișează întrebările și răspunsurile corecte, apoi afișează răspunsurile utilizatorului și calculează scorul.
    print("------------------")
    print("Result")
    print("------------------")
    print("Answers:", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
        print()

    print("Guesses",end=" ")
    for i in guesses:
        print(i, end=" ")
        print()

    score=int((correct_guesses/len(questions))*100) # Scorul este calculat ca procentajul de răspunsuri corecte din numărul total de întrebări și se afișează la sfârșit.
    print("Your score is:" +str(score)+"%")

def play_again(): #Funcția play_again este definită, dar momentană nu face nimic.
    pass



questions = {
    "Cine a creat limbajul python?":"A",
    "In ce an a fost creat?":"B",
    "Ce grup de comedie sprijina?":"C",
    "ESte Pamantul rotund?":"A"}  #questions conține întrebările și răspunsurile corecte



options = [["A.Rossum","D.Musk", "B.Gates","C.Zuckerburg"],
         ["A.1989","B.1991","C.2000","D.1299"],
           ["A. Lonely Island","B.SSmosh", "C.Monthi","D.SNL"],
         ["A.True","B.False","C.something","D.mda,poate"]] #options conține opțiunile pentru fiecare întrebare.


new_game() # se apelează funcția new_game() pentru a începe jocu