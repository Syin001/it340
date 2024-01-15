from tkinter import Tk, Label, StringVar, Button, Radiobutton, Canvas
from random import randint
from .question import *
import time


def createwindows():
    #   fenetre et toile de fond sur laquelle sont dessines les cases
    largeur = 1535
    hauteur = 800
    fenetre = Tk()
    fenetre.geometry( str(largeur)+"x"+str(hauteur) )
    fond = Canvas( fenetre , width=largeur , height=hauteur ,bg="white" )
    fenetre.wm_state(newstate="normal")
    fenetre.title('Jeu du BAC')
    fond.place( x=0 , y=0 )  
    return fond, fenetre

def generateBoard():
    global cases
    cases = []
    cases.append( fond.create_rectangle(30, 750, 100, 800, fill = 'white') )         # 0

    cases.append( fond.create_rectangle(40, 700, 90, 750, fill = 'yellow') )
    cases.append( fond.create_rectangle(40, 650, 90, 700, fill = 'red') )
    cases.append( fond.create_rectangle(40, 600, 90, 650, fill = 'green') )
    cases.append( fond.create_rectangle(40, 550, 90, 600, fill = 'purple') )
    cases.append( fond.create_rectangle(40, 500, 90, 550, fill = 'orange') )         # 5
    cases.append( fond.create_rectangle(40, 450, 90, 500, fill = 'red') )
    cases.append( fond.create_rectangle(40, 400, 90, 450, fill = 'blue') )
    cases.append( fond.create_rectangle(40, 350, 90, 400, fill = 'green') )
    cases.append( fond.create_rectangle(40, 300, 90, 350, fill = 'yellow') )
    cases.append( fond.create_rectangle(40, 250, 90, 300, fill = 'orange') )         # 10
    cases.append( fond.create_rectangle(40, 200, 90, 250, fill = 'purple') )
    cases.append( fond.create_rectangle(40, 150, 90, 200, fill = 'black') )
    cases.append( fond.create_rectangle(40, 100, 90, 150, fill = 'yellow') )
    cases.append( fond.create_rectangle(40, 50, 90, 100, fill = 'red') )
    cases.append( fond.create_rectangle(40, 0, 90, 50, fill = 'blue') )              # 15
    cases.append( fond.create_rectangle(90, 0, 140, 50, fill = 'yellow') )
    cases.append( fond.create_rectangle(140, 0, 190, 50, fill = 'black') )
    cases.append( fond.create_rectangle(190, 0, 240, 50, fill = 'green') )
    cases.append( fond.create_rectangle(240, 0, 290, 50, fill = 'purple') )
    cases.append( fond.create_rectangle(290, 0, 340, 50, fill = 'orange') )          # 20
    cases.append( fond.create_rectangle(290, 50, 340, 100, fill = 'red') )
    cases.append( fond.create_rectangle(290, 100, 340, 150, fill = 'black') )
    cases.append( fond.create_rectangle(290, 150, 340, 200, fill = 'green') )
    cases.append( fond.create_rectangle(290, 200, 340, 250, fill = 'blue') )
    cases.append( fond.create_rectangle(240, 200, 290, 250, fill = 'red') )          # 25
    cases.append( fond.create_rectangle(190, 200, 240, 250, fill = 'yellow') )
    cases.append( fond.create_rectangle(140, 200, 190, 250, fill = 'white') )
    cases.append( fond.create_rectangle(140, 250, 190, 300, fill = 'purple') )
    cases.append( fond.create_rectangle(140, 300, 190, 350, fill = 'black') )
    cases.append( fond.create_rectangle(140, 350, 190, 400, fill = 'orange') )       # 30
    cases.append( fond.create_rectangle(140, 400, 190, 450, fill = 'green') )
    cases.append( fond.create_rectangle(190, 400, 240, 450, fill = 'black') )
    cases.append( fond.create_rectangle(240, 400, 290, 450, fill = 'blue') )
    cases.append( fond.create_rectangle(290, 400, 340, 450, fill = 'red') )
    cases.append( fond.create_rectangle(290, 450, 340, 500, fill = 'yellow') )       # 35
    cases.append( fond.create_rectangle(290, 500, 340, 550, fill = 'purple') )
    cases.append( fond.create_rectangle(290, 550, 340, 600, fill = 'green') )
    cases.append( fond.create_rectangle(290, 600, 340, 650, fill = 'orange') )
    cases.append( fond.create_rectangle(240, 600, 290, 650, fill = 'red') )
    cases.append( fond.create_rectangle(190, 600, 240, 650, fill = 'blue') )         # 40
    cases.append( fond.create_rectangle(140, 600, 190, 650, fill = 'black') )
    cases.append( fond.create_rectangle(140, 650, 190, 700, fill = 'yellow') )
    cases.append( fond.create_rectangle(140, 700, 190, 750, fill = 'red') )
    cases.append( fond.create_rectangle(140, 750, 190, 800, fill = 'orange') )
    cases.append( fond.create_rectangle(190, 750, 240, 800, fill = 'purple') )       # 45
    cases.append( fond.create_rectangle(240, 750, 290, 800, fill = 'green') )
    cases.append( fond.create_rectangle(290, 750, 340, 800, fill = 'red') )
    cases.append( fond.create_rectangle(340, 750, 390, 800, fill = 'blue') )
    cases.append( fond.create_rectangle(390, 750, 440, 800, fill = 'yellow') )
    cases.append( fond.create_rectangle(440, 750, 490, 800, fill = 'orange') )        #50
    cases.append( fond.create_rectangle(490, 750, 540, 800, fill = 'purple') )
    cases.append( fond.create_rectangle(490, 700, 540, 750, fill = 'red') )
    cases.append( fond.create_rectangle(490, 650, 540, 700, fill = 'black') )
    cases.append( fond.create_rectangle(490, 600, 540, 650, fill = 'blue') )
    cases.append( fond.create_rectangle(490, 550, 540, 600, fill = 'green') )        # 55
    cases.append( fond.create_rectangle(490, 500, 540, 550, fill = 'purple') )
    cases.append( fond.create_rectangle(490, 450, 540, 500, fill = 'black') )        # debut de la boucle
    cases.append( fond.create_rectangle(440, 450, 490, 500, fill = 'blue') )
    cases.append( fond.create_rectangle(390, 450, 440, 500, fill = 'white') )
    cases.append( fond.create_rectangle(390, 400, 440, 450, fill = 'yellow') )       # 60
    cases.append( fond.create_rectangle(390, 350, 440, 400, fill = 'red') )
    cases.append( fond.create_rectangle(390, 300, 440, 350, fill = 'orange') )
    cases.append( fond.create_rectangle(390, 250, 440, 300, fill = 'black') )
    cases.append( fond.create_rectangle(390, 200, 440, 250, fill = 'green') )
    cases.append( fond.create_rectangle(440, 200, 490, 250, fill = 'red') )          # 65
    cases.append( fond.create_rectangle(490, 200, 540, 250, fill = 'yellow') )
    cases.append( fond.create_rectangle(540, 200, 590, 250, fill = 'blue') )
    cases.append( fond.create_rectangle(590, 200, 640, 250, fill = 'yellow') )
    cases.append( fond.create_rectangle(640, 200, 690, 250, fill = 'purple') )
    cases.append( fond.create_rectangle(640, 250, 690, 300, fill = 'red') )          # 70
    cases.append( fond.create_rectangle(640, 300, 690, 350, fill = 'orange') )
    cases.append( fond.create_rectangle(640, 350, 690, 400, fill = 'green') )
    cases.append( fond.create_rectangle(640, 400, 690, 450, fill = 'black') )
    cases.append( fond.create_rectangle(640, 450, 690, 500, fill = 'yellow') )
    cases.append( fond.create_rectangle(590, 450, 640, 500, fill = 'blue') )         # 75
    cases.append( fond.create_rectangle(540, 450, 590, 500, fill = 'purple') )       # fin de la boucle
    cases.append( fond.create_rectangle(540, 150, 590, 200, fill = 'black') )
    cases.append( fond.create_rectangle(540, 100, 590, 150, fill = 'green') )
    cases.append( fond.create_rectangle(540, 50, 590, 100, fill = 'orange') )
    cases.append( fond.create_rectangle(540, 0, 590, 50, fill = 'red') )             # 80
    cases.append( fond.create_rectangle(590, 0, 640, 50, fill = 'purple') )
    cases.append( fond.create_rectangle(640, 0, 690, 50, fill = 'yellow') )
    cases.append( fond.create_rectangle(690, 0, 740, 50, fill = 'red') )
    cases.append( fond.create_rectangle(740, 0, 790, 50, fill = 'orange') )
    cases.append( fond.create_rectangle(790, 0, 840, 50, fill = 'black') )           # 85
    cases.append( fond.create_rectangle(840, 0, 890, 50, fill = 'red') )
    cases.append( fond.create_rectangle(840, 50, 890, 100, fill = 'purple') )
    cases.append( fond.create_rectangle(840, 100, 890, 150, fill = 'blue') )         # debut de la boucle
    cases.append( fond.create_rectangle(790, 100, 840, 150, fill = 'yellow') )
    cases.append( fond.create_rectangle(740, 100, 790, 150, fill = 'purple') )       # 90
    cases.append( fond.create_rectangle(740, 150, 790, 200, fill = 'red') )
    cases.append( fond.create_rectangle(740, 200, 790, 250, fill = 'orange') )
    cases.append( fond.create_rectangle(740, 250, 790, 300, fill = 'green') )
    cases.append( fond.create_rectangle(790, 250, 840, 300, fill = 'blue') )
    cases.append( fond.create_rectangle(840, 250, 890, 300, fill = 'yellow') )       # 95
    cases.append( fond.create_rectangle(890, 250, 940, 300, fill = 'blue') )
    cases.append( fond.create_rectangle(940, 250, 990, 300, fill = 'purple') )
    cases.append( fond.create_rectangle(940, 200, 990, 250, fill = 'black') )
    cases.append( fond.create_rectangle(940, 150, 990, 200, fill = 'green') )
    cases.append( fond.create_rectangle(940, 100, 990, 150, fill = 'orange') )       # 100
    cases.append( fond.create_rectangle(890, 100, 940, 150, fill = 'red') )          # fin de boucle
    cases.append( fond.create_rectangle(840, 300, 890, 350, fill = 'white') )
    cases.append( fond.create_rectangle(840, 350, 890, 400, fill = 'blue') )
    cases.append( fond.create_rectangle(840, 400, 890, 450, fill = 'red') )
    cases.append( fond.create_rectangle(840, 450, 890, 500, fill = 'blue') )         # 105
    cases.append( fond.create_rectangle(840, 500, 890, 550, fill = 'yellow') )
    cases.append( fond.create_rectangle(840, 550, 890, 600, fill = 'purple') )
    cases.append( fond.create_rectangle(840, 600, 890, 650, fill = 'red') )
    cases.append( fond.create_rectangle(840, 650, 890, 700, fill = 'orange') )
    cases.append( fond.create_rectangle(840, 700, 890, 750, fill = 'green') )        # 110
    cases.append( fond.create_rectangle(840, 750, 890, 800, fill = 'blue') )
    cases.append( fond.create_rectangle(890, 750, 940, 800, fill = 'yellow') )
    cases.append( fond.create_rectangle(940, 750, 990, 800, fill = 'black') )
    cases.append( fond.create_rectangle(990, 750, 1040, 800, fill = 'purple') )
    cases.append( fond.create_rectangle(1040, 750, 1090, 800, fill = 'blue') )       # 115
    cases.append( fond.create_rectangle(1090, 750, 1140, 800, fill = 'green') )
    cases.append( fond.create_rectangle(1140, 750, 1190, 800, fill = 'orange') )
    cases.append( fond.create_rectangle(1140, 700, 1190, 750, fill = 'white') )
    #   cases par matière
    cases.append( fond.create_rectangle(1040, 550, 1190, 700, fill = 'orangered') )
    cases.append( fond.create_rectangle(1040, 400, 1190, 550, fill = 'deepskyblue') )# 120
    cases.append( fond.create_rectangle(1040, 250, 1190, 400, fill = 'chocolate') )
    cases.append( fond.create_rectangle(1040, 100, 1190, 250, fill = 'gold') )
    #   prison
    cases.append( fond.create_rectangle(650, 570, 750, 770, fill = 'navy') )
    #   cases légendes
    cases.append( fond.create_rectangle(1200, 400, 1250, 450, fill = 'red'))
    cases.append( fond.create_rectangle(1200, 450, 1250, 500, fill = 'purple'))
    cases.append( fond.create_rectangle(1200, 500, 1250, 550, fill = 'blue'))
    cases.append( fond.create_rectangle(1200, 550, 1250, 600, fill = 'yellow'))
    cases.append( fond.create_rectangle(1200, 600, 1250, 650, fill = 'green'))
    cases.append( fond.create_rectangle(1200, 650, 1250, 700, fill = 'black'))
    cases.append( fond.create_rectangle(1200, 700, 1250, 750, fill = 'orange'))

    #   legendes des couleurs
    texteRouge = fond.create_text(1285, 420,font = 250, text="Maths")
    texteViolet = fond.create_text(1295, 470,font = 250, text="CultureG")
    texteBleu = fond.create_text(1315, 520,font = 250, text="Philo/Français")
    texteJaune = fond.create_text(1325, 570,font = 250, text="Physique/Chimie")
    texteVert = fond.create_text(1305, 620,font = 250, text="SVT/Anglais")
    texteNoire = fond.create_text(1315, 670,font = 250, text="Manga/Anime")
    texteOrange = fond.create_text(1310, 720,font = 250, text="Histoire/Géo")

    #   ligne de separation
    fond.create_line(1195, 0, 1195, 800)

    #   texte dans les cases particulieres
    texteBac = fond.create_text(1110, 175,font = 250, text="Le Bac")
    texteS = fond.create_text(1110, 620,font = 250, text="S")
    texteL = fond.create_text(1110, 480,font = 250, text="L",)
    texteES = fond.create_text(1110, 325,font = 250, text="ES")
    textePrison = fond.create_text(700, 680, font = 250, fill = "red", text="PRISON")

def temps():
    heure.set(time.strftime('%H:%M:%S'))                                        # fonction indiquant l'heure
    fenetre.after(1000,temps)

def lancer1():
    ''' lance un de a six faces '''
    global position
    global couleur
    if position < 118 :
        de1 = randint(1,6)
        position = position + de1
        labelDiceResultat.config( text= str(de1)+" au lancé de dé" )
        if position>119 :
            position = 119
            poserQuestionFiliere()
        couleur = fond.itemcget( cases[position] , 'fill' )
        coordonneeCase = fond.coords( cases[position] )                                #   coordonnees de la case n
        x1Case = int(coordonneeCase[0])                                         #   abscisse (en haut a gauche) de la case n
        y1Case = int(coordonneeCase[1])                                         #   ordonnee (en haut a gauche) de la case n
        fond.coords( player , x1Case+5 , y1Case+5 , x1Case+25 , y1Case+25 )
        if couleur=='white' :
            prisoner()
        else :
            poserQuestion()

def poserQuestion() :
    ''' pose une question   '''
    #   choix aleatoire d'une question
    global numeroCouleur
    global numeroQuestion
    numeroCouleur = couleurs.index( couleur )                                   #   numero de cette couleur du joueur1
    nbQuestionCetteCouleur = len( question[numeroCouleur])                      #   nombre de questions pour cette couleur
    numeroQuestion = randint( 0 , nbQuestionCetteCouleur-1 )                    #   choix aleatoire d'un numero de question
    #   modification des textes
    labelQuestion.config( text = question[numeroCouleur][numeroQuestion][0] )      #   question posée
    bouton1.config( text =  question[numeroCouleur][numeroQuestion][1] )        #   réponse A proposée
    bouton2.config( text =  question[numeroCouleur][numeroQuestion][2] )        #   réponse B proposée
    bouton3.config( text =  question[numeroCouleur][numeroQuestion][3] )        #   réponse C proposée

##  fonction ajoutee
def poserQuestionFiliere() :
    ''' pose une question dans chaque filiere '''
    global numeroCouleur
    global numeroQuestion
    if position==119 :
        fond.coords( player , 1060 , 570 , 1080 , 590 )                        #   deplacement du pion
        numeroCouleur = couleurs.index( "orangered" )                            #   couleur de la case S
    elif position==120 :
        fond.coords( player , 1060 , 420 , 1080 , 440 )                        #   deplacement du pion
        numeroCouleur = couleurs.index( "deepskyblue" )                          #   couleur de la case L
    elif position==121 :
        fond.coords( player , 1060 , 270 , 1080 , 290 )                        #   deplacement du pion
        numeroCouleur = couleurs.index( "chocolate" )                            #   couleur de la case ES
    elif position==122 :
        fond.coords( player , 1060 , 120 , 1080 , 140 )                        #   deplacement du pion
        heureFin = time.strftime('%H:%M:%S')
        print( "heure de fin de partie :" , heureFin )
        if points>10 :
            texteFinal = "Bravo, vous avez eu votre baccalauréat !"
        else :
            texteFinal = "Dommage vous êtes recalé, vous devez repasser le baccalauréat"
        labelQuestion.config( text = texteFinal )                                  #   message de fin
        bouton1.destroy()
        bouton2.destroy()
        bouton3  .destroy()
        boutonValider.destroy()
        score.destroy()
    if position<122 :
        nbQuestionCetteCouleur = len( question[numeroCouleur])                  #   nombre de questions pour cette couleur
        numeroQuestion = randint( 0 , nbQuestionCetteCouleur-1 )                #   choix aleatoire d'un numero de question
        labelQuestion.config( text = question[numeroCouleur][numeroQuestion][0] )
        bouton1.config( text =  question[numeroCouleur][numeroQuestion][1] )
        bouton2.config( text =  question[numeroCouleur][numeroQuestion][2] )
        bouton3.config( text =  question[numeroCouleur][numeroQuestion][3] )

##  fin de la fonction

def validation():
    ''' valide le choix et permet de continuer a poser des questions    '''
    global nbValidations
    global points
    global position
    if position<119 :
        nbValidations = nbValidations+1                                         #   le nombre de clics sur le bouton valider est incremente
        if (nbValidations%2==1) :                                               #   si le nombre de clics est impair
            if (choix.get() == question[numeroCouleur][numeroQuestion][4]) :    #   si le choix correspond a la bonne reponse
                etiquetteSelection.config( text="VRAI" )
                points = points + 1                                             #   on gagne un point a chaque bonne reponse
            else :                                                              #   si le choix ne correspond pas a la bonne reponse
                etiquetteSelection.config( text="FAUX, la bonne réponse était " + question[numeroCouleur][numeroQuestion][4] )
            score.config(text = 'score : '+ str(points))
            boutonValider.config( text="Lancer" )
        else :
            lancer1()
            etiquetteSelection.config( text="Choisissez une réponse" )
            boutonValider.config( text="Valider" )
    ##  nouvelle partie de la fonction
    else :                                                                      #   validation avec les dernières cases
        if (choix.get() == question[numeroCouleur][numeroQuestion][4]) :        #   si le choix correspond a la bonne reponse
            etiquetteSelection.config( text="VRAI" )
            position = position + 1                                                         #   on passe a la case suivante
        else :                                                                  #   si le choix ne correspond pas a la bonne reponse
            etiquetteSelection.config( text="FAUX, essayez à nouveau" )
            points = points - 1                                                 #   on perd un point a chaque mauvaise reponse
        score.config(text = 'score : '+ str(points))
        poserQuestionFiliere()
    ##  fin de la nouvelle partie

def selection() :
    selection = "Vous avez choisi la réponse " + choix.get()
    etiquetteSelection.config( text=selection )                                        #   modifie le texte de l'etiquette
    labelDiceResultat.config( text="" )                                             #   efface le resultat du de


def lancerPrison():                                                             # Lance un dé en prison
    global dicePrison
    dicePrison = randint(1,6)
    labelPrison.config( text = str(dicePrison) )
    prisoner()

def prisoner() :                                                              # fonction Prison
    global position, dicePrison
    coordonneeCase = fond.coords( cases[123] )
    x1Case = int(coordonneeCase[0])
    y1Case = int(coordonneeCase[1])
    fond.coords( player , x1Case+5 , y1Case+5 , x1Case+25 , y1Case+25 )
    couleur1 = fond.itemcget( cases[123] , 'fill' )
    boutonValider.place_forget()
    boutonPrison.place(x = 680, y = 710)
    labelPrison.place(x = 700, y = 740)
    if dicePrison==6 :
        position = position-1
        coordonneeCase = fond.coords( cases[position-1] )
        x1Case = int(coordonneeCase[0])
        y1Case = int(coordonneeCase[1])
        fond.coords( player , x1Case+5 , y1Case+5 , x1Case+25 , y1Case+25 )
        boutonPrison.place_forget()
        boutonValider.place(x = 1320, y = 300)

def initplayer():
    global player, position, couleur
    x, y = 50, 770
    player = fond.create_oval(x, y, x+20, y+20, fill = 'gold')
    position = 0                                                                      #   numero de la case du joueur1
    couleur = 'white'

def initialize_gui():
    global fond, fenetre, labelDiceResultat, score, points, labelHeure, labelQuestion, etiquetteSelection, choix, boutonValider, boutonPrison, bouton1, bouton2, bouton3, labelPrison, question, couleurs, heure, nbValidations, numeroCouleur, numeroQuestion, dicePrison
    fond, fenetre = createwindows()
    generateBoard()
    initplayer()

    #   affiche le résultat du dé
    labelDiceResultat = Label(fenetre , text = "" , fg = 'black' , bg = 'white')
    labelDiceResultat.place( x=1400 , y=300 )

    #   score du joueur
    score = Label(fenetre, text = "", fg = 'black', bg = 'white')
    score.place( x = 1205, y = 350)

    heure = StringVar()                                                         #   variable de controle de type chaine de caracteres
    labelHeure = Label(fenetre, textvariable=heure)
    labelHeure.place( x=950 , y=10 )                                               #   pour faire apparaitre l'heure dans la fenetre
    temps()

    points = 0                                                                  #  nombre de points
    couleurs = [ "red", "green", "blue", "purple", "black", "yellow", "orange", "orangered", "deepskyblue", "chocolate", "navy" ]
    question = [ questionRouge, questionVerte, questionBleue, questionViolette, questionNoire, questionJaune, questionOrange, questionS, questionL, questionES, Prison ]
    numeroCouleur = -1                                                          #   initialisation arbitraire
    numeroQuestion = -1                                                         #   initialisation arbitraire

    #   composants de la fenetre
    labelQuestion = Label(fenetre, text = "question" )
    labelQuestion.place(x = 1205, y = 10)

    choix = StringVar()                                                         #   variable de controle de type chaine de caracteres
    bouton1 = Radiobutton(fenetre, text = "reponse A", variable = choix, value = 'A', command = selection)
    bouton1.place(x = 1290, y = 100)
    bouton2 = Radiobutton(fenetre, text = "reponse B", variable = choix, value = 'B', command = selection)
    bouton2.place(x = 1290, y = 150)
    bouton3 = Radiobutton(fenetre, text = "reponse C", variable = choix, value = 'C', command = selection)
    bouton3.place(x = 1290, y = 200)
    etiquetteSelection = Label( fenetre, text="Faites votre choix" )                   #   etiquette indiquant la selection
    etiquetteSelection.place(x = 1270, y = 250)

    nbValidations = -1                                                          #   initialisation à -1 car on clique d'abord sur 'commencer' avant de lancer le premier dé
    boutonValider = Button(fenetre, text = "Commencer", command = validation)
    boutonValider.place(x = 1320, y = 300)

    boutonPrison = Button(fenetre, text = "Lancer", command = lancerPrison)
    labelPrison = Label(fenetre, text = "", fg = 'red', bg = 'white')
    dicePrison = 0

def main():
    heureDebut = time.strftime('%H:%M:%S')
    print("heure de debut de partie :", heureDebut)

    initialize_gui()

    temps()
    fenetre.mainloop()

