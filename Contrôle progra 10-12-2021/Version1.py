import random
from colorama import init
init()
from colorama import Fore, Back, Style

listeMots = ["cinema", "girafe","tulipe","violet", "voyage", "valise", "hivers"]

motAlea = random.choice (listeMots)

print ("Bienvenu dans le jeu -- MOTUS -- ")
print ("Vous allez devoir découvrir le mot caché, pour cela, vous aurez 8 essais.")
print ("Bonne chance !")

#Pour la version de test
print ("Le mot caché est :", motAlea, "(invisible dans la version finale)")

for o in range (0,8) :
    
    motJoueur = input("Entrez un mot de 6 lettres : ")

    for i in range (0,6) :
        if motAlea[i] == motJoueur[i] :
            print (Back.RED+motJoueur[i], end=(''))
        else :
            test=False #ajout de True et False
            for j in range (0,6) :
                if motAlea[i] == motJoueur[j]:
                    print (Back.YELLOW+motJoueur[i], end=('')) 
                    test = True
            if test==False :
                    print (Back.BLUE+motJoueur[i], end=(''))
    print (Back.RESET + "")

    if motAlea == motJoueur :
        print ("Bravo ! Vous avez trouvé le mot !")
        print ("Relancez le programme si vous voulez jouer avec un nouveau mot.")
        exit()

print ("Dommage...Vous avez perdu")
print ("Retentez votre chance !")
