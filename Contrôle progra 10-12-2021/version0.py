#Importation du random et de colorama
import random
from colorama import init
init()
from colorama import Fore, Back, Style

#Variables 
listeMots = ["cinema", "desert", "girafe", "cactus", "tulipe", "etoile", "soleil", "violet", "voyage", "valise", "hivers"]
motAlea = random.choice (listeMots) #Un mot est choisi au harsard dans la liste

#Introduction au jeu
print ("Bienvenu dans le jeu MOTUS ! ")
print ("Vous allez devoir découvrir le mot caché, pour cela, vous aurez 8 essais.")
print ("Une lettre bien placée sera en rouge, une lettre présente dans le mot mais mal placée en jaune et une lettre qui n'est pas dans le mot sera en bleu")
print ("Bonne chance !")


#Affichage du mot pour la version de test
print ("Le mot caché est :", motAlea, "(invisible dans la version finale)")

for o in range (0,8) : #Le joueur à 8 tentatives
    
    motJoueur = input("Entrez un mot de 6 lettres : ")

    for i in range (0,6) :
        #Lettres bien placées (rouge)
        if motAlea[i] == motJoueur[i] :
            print (Back.RED+motJoueur[i], end=(''))
            #Lettres présentent mais mal placées (jaune)
            for j in range (0,6) :
                if motAlea[i] == motJoueur[j]:
                    print (Back.YELLOW+motJoueur[i], end=(''))
                    
                #Lettres absentes (bleu)
                    print (Back.BLUE+motJoueur[i], end=(''))
    print (Back.RESET + "")

    #Vctoire
    if motAlea == motJoueur :
        print ("Bravo ! Vous avez trouvé le mot !")
        print ("Relancez le programme si vous voulez jouer avec un nouveau mot.")
        exit()

#Défaite
print ("Dommage...Vous avez perdu")
print ("Retentez votre chance !")

