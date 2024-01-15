# crée par la Triforce Informatique
from tkinter import*
from random import*
import time

#   fenetre et toile de fond sur laquelle sont dessines les cases
largeur = 1535
hauteur = 800
fenetre = Tk()
fenetre.geometry( str(largeur)+"x"+str(hauteur) )
fond = Canvas( fenetre , width=largeur , height=hauteur ,bg="white" )
fenetre.wm_state(newstate="normal")
fenetre.title('Jeu du BAC')
fond.place( x=0 , y=0 )                                                         #   place le canevas sur la fenetre

#   tous les dessins (rectangles et textes) sur la toile de fond (Canvas)

#   cases
case = [ ]
case.append( fond.create_rectangle(30, 750, 100, 800, fill = 'white') )         # 0

case.append( fond.create_rectangle(40, 700, 90, 750, fill = 'yellow') )
case.append( fond.create_rectangle(40, 650, 90, 700, fill = 'red') )
case.append( fond.create_rectangle(40, 600, 90, 650, fill = 'green') )
case.append( fond.create_rectangle(40, 550, 90, 600, fill = 'purple') )
case.append( fond.create_rectangle(40, 500, 90, 550, fill = 'orange') )         # 5
case.append( fond.create_rectangle(40, 450, 90, 500, fill = 'red') )
case.append( fond.create_rectangle(40, 400, 90, 450, fill = 'blue') )
case.append( fond.create_rectangle(40, 350, 90, 400, fill = 'green') )
case.append( fond.create_rectangle(40, 300, 90, 350, fill = 'yellow') )
case.append( fond.create_rectangle(40, 250, 90, 300, fill = 'orange') )         # 10
case.append( fond.create_rectangle(40, 200, 90, 250, fill = 'purple') )
case.append( fond.create_rectangle(40, 150, 90, 200, fill = 'black') )
case.append( fond.create_rectangle(40, 100, 90, 150, fill = 'yellow') )
case.append( fond.create_rectangle(40, 50, 90, 100, fill = 'red') )
case.append( fond.create_rectangle(40, 0, 90, 50, fill = 'blue') )              # 15
case.append( fond.create_rectangle(90, 0, 140, 50, fill = 'yellow') )
case.append( fond.create_rectangle(140, 0, 190, 50, fill = 'black') )
case.append( fond.create_rectangle(190, 0, 240, 50, fill = 'green') )
case.append( fond.create_rectangle(240, 0, 290, 50, fill = 'purple') )
case.append( fond.create_rectangle(290, 0, 340, 50, fill = 'orange') )          # 20
case.append( fond.create_rectangle(290, 50, 340, 100, fill = 'red') )
case.append( fond.create_rectangle(290, 100, 340, 150, fill = 'black') )
case.append( fond.create_rectangle(290, 150, 340, 200, fill = 'green') )
case.append( fond.create_rectangle(290, 200, 340, 250, fill = 'blue') )
case.append( fond.create_rectangle(240, 200, 290, 250, fill = 'red') )          # 25
case.append( fond.create_rectangle(190, 200, 240, 250, fill = 'yellow') )
case.append( fond.create_rectangle(140, 200, 190, 250, fill = 'white') )
case.append( fond.create_rectangle(140, 250, 190, 300, fill = 'purple') )
case.append( fond.create_rectangle(140, 300, 190, 350, fill = 'black') )
case.append( fond.create_rectangle(140, 350, 190, 400, fill = 'orange') )       # 30
case.append( fond.create_rectangle(140, 400, 190, 450, fill = 'green') )
case.append( fond.create_rectangle(190, 400, 240, 450, fill = 'black') )
case.append( fond.create_rectangle(240, 400, 290, 450, fill = 'blue') )
case.append( fond.create_rectangle(290, 400, 340, 450, fill = 'red') )
case.append( fond.create_rectangle(290, 450, 340, 500, fill = 'yellow') )       # 35
case.append( fond.create_rectangle(290, 500, 340, 550, fill = 'purple') )
case.append( fond.create_rectangle(290, 550, 340, 600, fill = 'green') )
case.append( fond.create_rectangle(290, 600, 340, 650, fill = 'orange') )
case.append( fond.create_rectangle(240, 600, 290, 650, fill = 'red') )
case.append( fond.create_rectangle(190, 600, 240, 650, fill = 'blue') )         # 40
case.append( fond.create_rectangle(140, 600, 190, 650, fill = 'black') )
case.append( fond.create_rectangle(140, 650, 190, 700, fill = 'yellow') )
case.append( fond.create_rectangle(140, 700, 190, 750, fill = 'red') )
case.append( fond.create_rectangle(140, 750, 190, 800, fill = 'orange') )
case.append( fond.create_rectangle(190, 750, 240, 800, fill = 'purple') )       # 45
case.append( fond.create_rectangle(240, 750, 290, 800, fill = 'green') )
case.append( fond.create_rectangle(290, 750, 340, 800, fill = 'red') )
case.append( fond.create_rectangle(340, 750, 390, 800, fill = 'blue') )
case.append( fond.create_rectangle(390, 750, 440, 800, fill = 'yellow') )
case.append( fond.create_rectangle(440, 750, 490, 800, fill = 'orange') )        #50
case.append( fond.create_rectangle(490, 750, 540, 800, fill = 'purple') )
case.append( fond.create_rectangle(490, 700, 540, 750, fill = 'red') )
case.append( fond.create_rectangle(490, 650, 540, 700, fill = 'black') )
case.append( fond.create_rectangle(490, 600, 540, 650, fill = 'blue') )
case.append( fond.create_rectangle(490, 550, 540, 600, fill = 'green') )        # 55
case.append( fond.create_rectangle(490, 500, 540, 550, fill = 'purple') )
case.append( fond.create_rectangle(490, 450, 540, 500, fill = 'black') )        # debut de la boucle
case.append( fond.create_rectangle(440, 450, 490, 500, fill = 'blue') )
case.append( fond.create_rectangle(390, 450, 440, 500, fill = 'white') )
case.append( fond.create_rectangle(390, 400, 440, 450, fill = 'yellow') )       # 60
case.append( fond.create_rectangle(390, 350, 440, 400, fill = 'red') )
case.append( fond.create_rectangle(390, 300, 440, 350, fill = 'orange') )
case.append( fond.create_rectangle(390, 250, 440, 300, fill = 'black') )
case.append( fond.create_rectangle(390, 200, 440, 250, fill = 'green') )
case.append( fond.create_rectangle(440, 200, 490, 250, fill = 'red') )          # 65
case.append( fond.create_rectangle(490, 200, 540, 250, fill = 'yellow') )
case.append( fond.create_rectangle(540, 200, 590, 250, fill = 'blue') )
case.append( fond.create_rectangle(590, 200, 640, 250, fill = 'yellow') )
case.append( fond.create_rectangle(640, 200, 690, 250, fill = 'purple') )
case.append( fond.create_rectangle(640, 250, 690, 300, fill = 'red') )          # 70
case.append( fond.create_rectangle(640, 300, 690, 350, fill = 'orange') )
case.append( fond.create_rectangle(640, 350, 690, 400, fill = 'green') )
case.append( fond.create_rectangle(640, 400, 690, 450, fill = 'black') )
case.append( fond.create_rectangle(640, 450, 690, 500, fill = 'yellow') )
case.append( fond.create_rectangle(590, 450, 640, 500, fill = 'blue') )         # 75
case.append( fond.create_rectangle(540, 450, 590, 500, fill = 'purple') )       # fin de la boucle
case.append( fond.create_rectangle(540, 150, 590, 200, fill = 'black') )
case.append( fond.create_rectangle(540, 100, 590, 150, fill = 'green') )
case.append( fond.create_rectangle(540, 50, 590, 100, fill = 'orange') )
case.append( fond.create_rectangle(540, 0, 590, 50, fill = 'red') )             # 80
case.append( fond.create_rectangle(590, 0, 640, 50, fill = 'purple') )
case.append( fond.create_rectangle(640, 0, 690, 50, fill = 'yellow') )
case.append( fond.create_rectangle(690, 0, 740, 50, fill = 'red') )
case.append( fond.create_rectangle(740, 0, 790, 50, fill = 'orange') )
case.append( fond.create_rectangle(790, 0, 840, 50, fill = 'black') )           # 85
case.append( fond.create_rectangle(840, 0, 890, 50, fill = 'red') )
case.append( fond.create_rectangle(840, 50, 890, 100, fill = 'purple') )
case.append( fond.create_rectangle(840, 100, 890, 150, fill = 'blue') )         # debut de la boucle
case.append( fond.create_rectangle(790, 100, 840, 150, fill = 'yellow') )
case.append( fond.create_rectangle(740, 100, 790, 150, fill = 'purple') )       # 90
case.append( fond.create_rectangle(740, 150, 790, 200, fill = 'red') )
case.append( fond.create_rectangle(740, 200, 790, 250, fill = 'orange') )
case.append( fond.create_rectangle(740, 250, 790, 300, fill = 'green') )
case.append( fond.create_rectangle(790, 250, 840, 300, fill = 'blue') )
case.append( fond.create_rectangle(840, 250, 890, 300, fill = 'yellow') )       # 95
case.append( fond.create_rectangle(890, 250, 940, 300, fill = 'blue') )
case.append( fond.create_rectangle(940, 250, 990, 300, fill = 'purple') )
case.append( fond.create_rectangle(940, 200, 990, 250, fill = 'black') )
case.append( fond.create_rectangle(940, 150, 990, 200, fill = 'green') )
case.append( fond.create_rectangle(940, 100, 990, 150, fill = 'orange') )       # 100
case.append( fond.create_rectangle(890, 100, 940, 150, fill = 'red') )          # fin de boucle
case.append( fond.create_rectangle(840, 300, 890, 350, fill = 'white') )
case.append( fond.create_rectangle(840, 350, 890, 400, fill = 'blue') )
case.append( fond.create_rectangle(840, 400, 890, 450, fill = 'red') )
case.append( fond.create_rectangle(840, 450, 890, 500, fill = 'blue') )         # 105
case.append( fond.create_rectangle(840, 500, 890, 550, fill = 'yellow') )
case.append( fond.create_rectangle(840, 550, 890, 600, fill = 'purple') )
case.append( fond.create_rectangle(840, 600, 890, 650, fill = 'red') )
case.append( fond.create_rectangle(840, 650, 890, 700, fill = 'orange') )
case.append( fond.create_rectangle(840, 700, 890, 750, fill = 'green') )        # 110
case.append( fond.create_rectangle(840, 750, 890, 800, fill = 'blue') )
case.append( fond.create_rectangle(890, 750, 940, 800, fill = 'yellow') )
case.append( fond.create_rectangle(940, 750, 990, 800, fill = 'black') )
case.append( fond.create_rectangle(990, 750, 1040, 800, fill = 'purple') )
case.append( fond.create_rectangle(1040, 750, 1090, 800, fill = 'blue') )       # 115
case.append( fond.create_rectangle(1090, 750, 1140, 800, fill = 'green') )
case.append( fond.create_rectangle(1140, 750, 1190, 800, fill = 'orange') )
case.append( fond.create_rectangle(1140, 700, 1190, 750, fill = 'white') )
#   cases par matière
case.append( fond.create_rectangle(1040, 550, 1190, 700, fill = 'orangered') )
case.append( fond.create_rectangle(1040, 400, 1190, 550, fill = 'deepskyblue') )# 120
case.append( fond.create_rectangle(1040, 250, 1190, 400, fill = 'chocolate') )
case.append( fond.create_rectangle(1040, 100, 1190, 250, fill = 'gold') )
#   prison
case.append( fond.create_rectangle(650, 570, 750, 770, fill = 'navy') )
#   cases légendes
case.append( fond.create_rectangle(1200, 400, 1250, 450, fill = 'red'))
case.append( fond.create_rectangle(1200, 450, 1250, 500, fill = 'purple'))
case.append( fond.create_rectangle(1200, 500, 1250, 550, fill = 'blue'))
case.append( fond.create_rectangle(1200, 550, 1250, 600, fill = 'yellow'))
case.append( fond.create_rectangle(1200, 600, 1250, 650, fill = 'green'))
case.append( fond.create_rectangle(1200, 650, 1250, 700, fill = 'black'))
case.append( fond.create_rectangle(1200, 700, 1250, 750, fill = 'orange'))

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

#   liste de questions par matière

# Physique et Chimie
questionJaune = [["Quel est le domaine visible de la lumière ?", "A : [400:800] m", "B : [400,800] nm", "C : [400,800] μm", "B"],
                 ["Quelle est la formule brut de l'acide sulfurique ?", "A : HNO3", "B : H2CO3", "C : H2SO4", "C" ],
                 ["Quelle est la loi de Beer-Lambert ?", "A : A = ε x l x C", "B : σ = k x C", "C : σ = λ x C", "A"],
                 ["Quelle est la vitesse de la lumière ?", "A : 3 000 000 cm/s ","B : 3 000 000 m/s" , "C =  300 000 km/s", "C",],
                 ["Quelle est la seconde loi de Newton ?", "A : F= m*a", "B : F= m*g", " C : F= m/a", "A"],
                 ["A quelle famille appartient les elements chimique de la deuxième colonne du tableau périodique des éléments ?","A : Halogènes", "B : Alcalino-terreux", "C : Gaz nobles", "B"],
                 ["Quelle est la température d'ébullition de l'eau ?", "A : 100 °C", "B : 95 °C", "C : 130 °C", "A"],
                 ["Qu'est ce qu'une espèce amphotère ?", "A : une espèce qui peut être acide \n et basique","B : une espèce qui est uniquement \n acide","C : une espèce qui est uniquement \n basique", "A"],
                 ["Quelle est la formule du pH ?", "A : pH= [H3O+]*log(10)", "B : pH= -log[H3O+]", "C : pH= -log[HO-]", "B"],
                 ["Quel philosophe a participé au progrés de la chimie ?", "A : Descartes", "B : Archimède", "C : Machiavel", "A"],
                 ["Un acide peut...?", "A : libérer un proton H+", "B : capter un proton H+", "C : faire fondre un os", "A"],
                 ["Les réactifs titrés et titrants sont introduits dans des proportions stoechiométrique", "A : au milieu", "B : à l'équivalence", "C : à l'équilibre", "B"],
                 ["Que signifie CAN ?", "Convertisseur Antologique Numérisé", "B : Convertisseur Arithmétique Numérique", "C : Convertisseur Analogique Numérique", "C"],
                 ["un octet...", "A : code 256 valeurs", "B : 8 valeurs", "C : 64 valeurs", "A"],
                 ["quel est l'unité SI de base du Joule (J)", "A : kg.m2.s−2", "B : B : kg.m.s-2", "C : kg.m2.s-1", "A"],
                 ["Quelle est la formule de l'acide chlorydrique", "A : Cl", "B : ACl", "C : HCl", "C"],
                 ["Quelle(s) précaution(s) prendre; à part la blouse; \n pour manipuler  un produit corrosif ?", "A : une hotte", "B : gants et lunettes", "C : un chiffon", "B"],
                 ["Lors d'un dosage par étalonnage, il faut d'abord...?", "A : faire le blanc", "B : calculer l'absorbance de la solution", "C : rajouter de l'eau distillée", "A"],
                 ["Un faisceau laser est une onde ...?", "A : polychromatique", "B : monochromatique", "C : chromatique", "B"],
                 ["Le son est plus rapide dans ?", "A : l'air", "B : l'eau", "C : la matiére", "B"],
                 ["Un son est perçu plus aigu lorsque l'on...?", "A : s'approche de l'émetteur", "B : s'éloigne de l'émetteur", "C : augmente le volume", "A"]]

# Philosophie et Français
questionBleue = [["Quel philosophe est pessimiste ?", "A : Schopenhauer", "B : Rousseau", "C : Eisenhower","A"],
                 ["Qui est l'auteur des ''Pensées'' ?", "A : Pascal", "B : Aristote", "C : Hegel", "A"],
                 ["Qu'est-ce que l'aliénation ?", "A : être déposséder de soi", "B : accoucher de ses pensées", "C : agir avec contrainte", "A"],
                 ["Qu'est-ce que la maïeutique ?", "A : une technique", "B : un art", "C : une mosaïque", "B"],
                 ["comment appelle-t-on un vers à 12 syllabes ?", "A : Alexandrin", "B : Octosyllabe", "C : Décasyllabe", "A"],
                 ["quelle figure de style associe directement \n un comparé à un comparant ?", "A : Comparaison", "B : Antithèse", "C : Métaphore", "C"],
                 ["Parmi ces auteurs lequel est un philosophe du contract ?","A : Pascal","B : Hobbes","C : Spinoza","B"],
                 ["Quel auteur dit <L'obéissance à la loi qu'on s'est \n prescrite est liberté> ?","A : Rousseau","B : Lévi-Strauss","C : Clastres ","A"],
                 ["Comment se nome la figure de style qui designe \n l'amplification d'un mot ?","A : l'éxagération","B : L'hyperbole","C : La disproportion","B"],
                 ["qu'est ce qui est inscrit sur le temple de Delphe ?", "A : Connait toi toi-même", "B : Aide ton prochain", "C : Sois humble", "A"],
                 ["Qu'est ce qui s'oppose au droit positif ?", "A : le droit négatif", "B : le droit naturel", "C : le droit humain", "B"],
                 ["Compléter : << L'Homme est un roseau...", "A : perdant", "B : faible", "C : pensant", "C"],
                 ["A quoi s'oppose la justice commutative ?", "A : la justice additive", "B : la jusice distributive", "C : la justice humaine", "B"],
                 ["Selon Kant le bonheur est...", "A : de la raison pure", "B : de l'imagination", "C : un désir", "B"],
                 ["Qui est le philosophe des petites perçeptions ?", "A : Kant", "B : Rousseau", "C : Leibniz", "C"],
                 ["Autrui est le médiateur indispensable...", "A : entre Moi et Moi-même", "B : Moi et ça", "C : Moi et surmoi", "A"],
                 ["Quelles sont les trois instances psychiques selon Freud", "A : Moi, surmoi et ça", "B : ich, Überich et falsch", "C : Moi, autrui et ça", "A"],
                 ["L'expérience de la honte est évoqué par...", "A : Freud", "B : René Girard", "C : Sartre", "C"],
                 ["A quoi correspond le dualisme Cartésien ?", "A : Corp et Esprit", "B : Bien et Mal", "C : Le doute et la Raison", "A"],
                 ["Quel philosophe pense pense qu'à l'état de nature \n l'Homme est un loup pour l'Homme ?", "A : Rousseau", "B : Hobbes", "C : Spinoza", "B"],
                 ["Quel philosophe définit l'Homme comme un \n animal politique ?", "A : Aristote", "B : Hobbes", "C : Rousseau", "A"],
                 ["Dans << Le Prince >>, Machiavel \n présente une philosophie...", "A : immorale", "B : intolérante", "C : amorale", "C"],
                 ["Pour Spinoza << La fin de l'Etat \n est donc en réalité...>>", "A : La domination", "B : Le pouvoir", "C : La liberté", "C"],
                 ["Qu'est ce que l'anarchie ?", "A : Le Chaos social", "B : Le refus de l'autorité politique", "C : le communisme", "B"],
                 ["Selon Weber l'Etat detient le monopole...", "A : De violence physique", "B : De la violence morale", "C : De la violence gratuite", "A"],
                 ["Selon Freud les rêves sont...", "A : Refoulés", "B : La voie royale pour l'inconscient", "C : Une illusion de l'inconscient", "B"],
                 ["Qui dit je est un autre ?", "A : Rimbaud", "B : Nietzsche", "C : Sartre", "A"],
                 ["Selon Kant, quand un artist commence son travail ...","A : il doit demander conseil","B : il ne peut pas avoir ue immage présice du résultat","C : il a besoin d'un modèle précis","B"],
                 ["Selon Kant le génie est ","A : universel","B : subjectif","C : individuel","B"],
                 ["Pendant des siècles, l'art avait la même définition que","A : métier","B ; technique","C : travail","B"],
                 ["Complétez la phrase de Klee \n << L'art ne produit pas le visible mais...","A : montre le réel","B : dévoile le monde","C : rend visible","C"]]

# Anime et manga
questionNoire = [["Quand dragon ball est-il sorti ?", "A : 1985", "B : 1992", "C : 1984", "C"],
                 ["Quelle est le mot préféré de Nero Claudius dans Fate/Extra ?", "A : Yay", "B : Umu", "C : dattebayo", "B"],
                 ["Qui est l'auteur de One Piece ?", "A : Hiro Mashima", "B : Eiichiro Oda", "C : Masashi Kishimoto", "B"],
                 ["quel mot en japonais est utilisé pour appeler son aîné ?", "A : sensei", "B : kōhai", "C : senpai", "C"],
                 ["lequel de ces plats n'appartient pas au Japon ?", "A : Gyoza", "B : sushi", "C : Mapo Tofu", "C"],
                 ["Que signifie SAO ?", "A : Sword Art Online", "B : Swim Art Office", "C : Swear As Origine", "A"],
                 ["Combien de classe de servant existe dans Fate Stay Night ?", "A : 8", "B : 7", "C : 9", "B"],
                 ["comment s'appelle le 1er bateau des chapeaux de pailles ?", "A : Vogue Merri", "B : Vogue Mery", "C : Vogue Merry", "C"],
                 ["Opening 1 de sword Art Online", "A : Catch The Moment de LiSA", "B : Crossing Field de LiSA", "C : Rising Hope de LiSA", "B"],
                 ["Opening 1 de sword Art Online II", "A : Ignite de Eir Aoi", "INNOCENCE de Eir Aoi", "C : KASUMI de Eir Aoi", "A"],
                 ["Combien d'opening possède Naruto Shippuden ?", "A : 20 openings", "B : 18 openings", "C : 25 openings", "A"],
                 ["En combien d'épisode c'est terminé Naruto Shippuden ?", "A : 600 épisodes", "800 épisodes", "C : 500 épisodes", "C"],
                 ["Lequel de ces animes n'est pas un anime de sport ?", "A : Kuroko no Basket", "Shokugeki no Soma", "C : Haikyuu", "B"],
                 ["Quel anime sort une phrase philosophique à chaque épisode ?", "A : Classroom crisis", "B : Classroom of the Elite", "C : Assassination Classroom", "B"],
                 ["Comment appelle-t-on les sabres des Shinigami dans Bleach ?", "A : Zanpakutō", "B : Nihontō", "C : Shinokyōfu", "A"],
                 ["Fairy Tail est un manga où...","A : des personnes cherchent le One Piece", "B : des personnes veulent manger le plus", "C : des personnes utilisent de la magie", "C"],
                 ["quelle est le nom de Sanji dans One piece ?", "A : Vinsmoke", "B : Vimsnoke", "C : Vinmoke", "A"],
                 ["Opening 2 de Fate Stay Night UBW", "A : Last Stardust de Aimer", "B : Ninelie de Aimer", "C : Brave Shine de Aimer", "C"],
                 ["Comment s'appelle la 1ère supertechnique de Axel Blaze \n dans Inazuma eleven ?", "A : Tempête de feu", "B : Tornade de feu", "C : tourbillon de feu", "B"],
                 ["Comment s'appelle la 1ère supertechnique de Mark Evans \n dans Inazuma eleven ?", "A : Main Celeste", "B : Main Magique", "C : Main de l'infinie", "A"],
                 ["Chopper de One piece est...", "A : Un Cerf", "B : Un Faon", "C : Un Renne", "C"],
                 ["Shokugeki no soma est un manga sur...", "A : sur la cuisine", "B : sur la boxe", "C : sur la natation", "A"],
                 ["Free est un anime sur...", "A : les prix d'Intermarché", "B : sur la gratuité des produits", "C : sur la natation", "C"],
                 ["Death note est un manga parlant...", "A : d'un stylo pouvant tué des gens", "B : d'un cahier de la mort", "C : d'un papier pouvant tout couper", "B"],
                 ["Inazuma eleven est un anime sur...", "A : le basketball", "B : le surf", "C : le football", "C"],
                 ["eyeshield 21 ets un manga sur...", "A : la musique", "B : le football américain", "C : la course", "B"],
                 ["Hunter x Hunter a subi une remasterisation, \n mais en quelle année ?", "A : 2007", "B : 2011", "C : 2014", "B"],
                 ["Beaucoup de manga se passe dans lieu précis, lequel ?", "A : un monde fantastique", "B : un manoir", "C : un lycée", "C"],
                 ["De quel jeu vidéo s'est inspiré Hiro Mashima pour son \n manga Fairy Tail?", "A : Monster Hunter", "B : Dragon quest", "C : Final Fantasy", "B"],
                 ["Quel est le genre de manga qui se passe dans la vie de \n tous les jours?", "A : slice of life", "B : school life", "C : shonen", "A"],
                 ["Boruto est ...", "A : une suite logique à Naruto", "B : un spin-off", "C : un nolife", "B"]]

# Histoire et Géograhie
questionOrange = [["Quand a été proclamé la République populaire de Chine ?", "A : 1946", "B : 1899", "C : 1949", "C"],
                  ["Quel est le nom du mouvement des Juifs voulant rejoindre \n leur terre d'origine ?", "A : Sionisme", "B : Siaunisme", "C : Retour aux originisme", "A"],
                  ["En quelle année Yuri Gagarine est-il allé dans l'espace ?", "A : 1957", "B : 1963", "C : 1961", "C"],
                  ["Qui est l'auteur de ''La France de Vichy'' ?", "A : Robert Paxton", "B : Eric Zemmour", "C : Alain Resnais", "A"],
                  ["Quelle organisation détient les 2/3 du commerce mondiale ?", "A : la Triade", "B : les FTN", "C : Donald Trump", "A"],
                  ["Qu'est-ce que l'Oural ?", "A : une montagne", "B : une faille", "C : une chaîne de montagnes", "C"],
                  ["Qu'est-ce qu'une ville de plus de 10 millions d'habitants ?", "A : mégalopole", "B : métropole", "C: mégapole","C"],
                  ["Que veut dire EVP ? ", "A : Enfants Vietnamien par Pays","B : Etat Vraiment Puissant","C : Equivalant Vingt Pieds","C"],
                  ["Quesqu'un pays enclavé ?","A : un pays sans ressources","B : un pays sans acces à la mer ?","C : un pays sans acces aérien","B"],
                  ["Qui manifestait lors de Mai 68 ?", "A : les cadres", "B : les ouvriers", "C : les ouvriers et les étudiants", "C"],
                  ["Qu'est-ce que les Trente Glorieuses ?", "A trente années de paix", "B : trente années de dictature", "C : trente années de construction \n démocratique", "A"],
                  ["En quelle année l'URSS a-t-elle disparu ?","A: 1990","B : 1991","C : 1992","B"],
                  ["Quand est mort Charles De Gaulle","A : Novembre 1970","B : Août 1971",'C : Décembre 1972',"A"],
                  ["En quelle année est mort Jean Moulin ?","A : 1942","B : 1940","C : 1943","C"],
                  ["Quesqu'une ONG ?","A : Organisation Né au Gabon","B : Organisation Non Gouvernemental","C : Oscar de Nouvelle Guinée"],
                  ["En quelle année eu lieu le procès de Adolf Eichmann ?","A : 1965","B : 1964","C : 1961","C"],
                  ["A l'issu de quelle conférence fut créée l'ONU ?","A : conférence de Yalta","B : conférence de Bretton Woods","C : conférence de San Francisco","C"],
                  ["En quelle année fut créée la CIA ? ","A : 1946","B : 1947","C : 1949","B"],
                  ["Qui était Robert Paxton ?","A : un historien","B : un ministre","C : un président","A"],
                  ["En quelle année fut lancé le Tiers-Monde ?","A : en 1950","B : en 1955","C : en 1952","C"],
                  ["En quelle année fut proclamé l'indépendance de l'Inde ?","A : en 1945"," B : en 1939","C : en 1947","C"],
                  ["Le 'Grand Bond en avant' est une politique \n économique Chinoise lancé en ..","A : 1958","B : 1956","C : 1955","A"],
                  ["Lequel de ces pays ne possède pas un morceau \n de Sahara dans son territoire ?","A : Le Sudan","B : Le Mali","C : le Nigeria","C"],
                  ["Dans quel pays les Etats-Unis interviennent-ils en 2001 ?","A : en Afghanistan","B : en Iran","C : en Irak","A"],
                  ["Qui accède au pouvoir en Irak à partir de 1979 \n et y établit une dictature ?","A : Saddam Hussein","B : Yasser Arafat","C : Moubarak","A"],
                  ["A quels mouvements nationalistes arabes \n l'URSS accorde-t-elle son soutien ?","A : au Likoud israélien","B : à Nasser en Egypte","C : au parti Baas en Syrie","B"],
                  ["Quel pays indépendant est envahi par la Chine \n communiste de Mao et en quelle année?","A : le Tibet en 1950","B : le Cambodge en 1969","C : la Corée en 1953","A"]]

# Mathématiques
questionRouge = [["quel est la limite de 2 + 1/x en +l'infini ?", "A : +l'infini", "B : 0", "C : 2", "C"],
                 ["Comment appele-t-on l'ensemble de tous \n les résultats d'une aléatoire ?","A : Univers", "B : Galaxie", "C : Livre", "A"],
                 ["Quel est le contraire d'une dérivé ?", "A : une vitesse", "B : une primitive", "C : une accélération", "B"],
                 ["La courbe de la fonction ln(x) admet une asymptote \n verticale, mais de quelle équation ?", "A : x = 1", "B : x = 0", "C : x = log(10)", "B"],
                 ["Que vaut e^ln(37) ?","A : ln(37)","B : e^37","C : 37","C"],
                 ["Que vaut (0,9)^n lorsque n tend vers +l'infini?","A : +l'infini",'B : 0',"C : 0,9","B"],
                 ["que vaut e^x avec x = o", "A : 1", "B : 2,7", "C : 0", "A"],
                 ["Une loi exponentielle est ...?", "A : sans mémoire", "B : la réciproque de loi logarithme", "C : toujours négative", "A"],
                 ["Quelle courbe représente une loi normale?", "A : courbe d'Epérion", "B : courbe de cloche", "C : courbe de Gauss", "C"],
                 ["Comment note-on la partie réelle d'un nombre imaginaire z ?", "A : Re(z)", "B : a", "C : Im(z)","A"],
                 ["Avec quel triangle peut-on calculer un coefficient binomial ?", "A : le triangle des Bermudes", "B : le triangle rectangle", "C : le triangle de Pascal","C"],
                 ["Le théorème de bijection monotone est aussi appelé ?", "A : TVI", "B : TNI", "C : TGV", "A"],
                 ["Qu'est-ce que la  représentation paramétrique d'une droite ?", "A : une équation", "B : un système", "C : un produit scalaire", "B"],
                 ["Le nombre exponentiel e vaut...", "A : 2,17", "B : 3,14", "C : 0", "A"],
                 ["Quel est la derivé de 1/u ","A : -u'/u^2","B : -u/u^2","C : -u'/u","A"],
                 ["Quel est la dérivé de u * v","A : u'v'+uv","B : u'v+u'v","C : u'v+uv'","C"],
                 ["Quel est la dérivé de √u","A : u'/(2*u)","B : u'/(2√u)","C : u/(2√u)","B"],
                 ["Quel est la dérivé de U^n","A : n*u'*(u^n-1)","B : n*u*(u^n-1)","C : n*u'*(u^n)"],
                 ["Pour la fonction exponentielle e^-x est équivalant à","A : e^x","B : e^x/x","C : 1/e^x","C"],
                 ["Pour la fonction exponentielle e^(x+y) est équivalant à","A : e^y/e^x","B : e^x/e^y","C : e^x * e^y","C"],
                 ["La fonction exponentielle est toujours","inférieur à O","constante","supérieur à 0","C"],
                 ["Quel est la dérivé de e^u","A : u*e^u","B : u'*e^u'","C : u'*e^u","C"],
                 ["ln(a/b) est équivalant à","A : ln(a)/ln(b)","B : ln(a)+ln(b)","C : ln(a) - ln(b)","C"]]

# SVT et Anglais
questionVerte = [["When J.F.Kennedy die ?", "A : 22 nov 1963", "B : 15 march 1960", "C : 20 nov 1962", "A"],
                 ["What's the french for beaming ?", "A : souriant", "B : radieux", "C : explosif", "B"],
                 ["what does LMAO mean ?", "A : laughing my ass off", "B : lol my ass on", "C : like my ass octopus", "A"],
                 ["Où naissent les lymphocytes?", "A : Moelle épinière", "B : Thymes", "C : Moelle osseuse", "C"],
                 ["Quel concept explique les différences d'altitudes \n entre croûte continentale et océanique?", "A : Isomérie", "B : Isostasie", "C : Isothérmie", "B"],
                 ["Comment appele-t-on la coopération entre animaux \n et plantes au cours du temps ?", "A : Collaboration", "B : Symbiose", "C : Coévolution", "C"],
                 ["Quel est le nom de la phase de réplication des \n cellules reproductrices ?", "A : Mitose", "B : Méiose", "C : Miose", "B"],
                 ["Quelles cellules sont responsables de la \n réaction inflammatoire","A : les lymphocytes","B : les phagocytes","C : les cellules sentinelles","C"],
                 ["Que sont les anticorps ?","A : des protéines","B : des molécules","C : des cellules","A"],
                 ["que signifie LTc ?", "A : Lymphocyte T cytoplasmique", "Lymphocyte T cytoxique", "C : Lymphocyte T cytotoxique", "C"],
                 ["L'andésite est une roche...?", "A : magmatique", "B : plutonique", "C : ophiolitique", "A"],
                 ["L'Homme a un génome trés proche d'un primate, mais lequel?","A : l'Ourang Outan", "B : le chimpanzé", "C : le bonobo","B"]]

# Culture Générale
questionViolette = [["Capitale de la Mongolie ?", "A : Calcutta", "B : Oulang-Bator", "C : Achgabat", "B"],
                    ["Capitale du Cambodge ?", "A : Phnom penh", "B : Battambang", "C : Kratie", "A"],
                    ["Comment s'appelle le tableau regroupant tous les atomes", "A : tableau de signe", "B : tableau de Mendeleïev", "C : tableau de Einstein","B"],
                    ["Qui est la mère du Prince Albert II de Monaco?", "A : Ingrid Donatello", "B : Grace Kelly", "C : Emmanuelle de Monaco", "B"],
                    ["Quelle est la troisième couleur du drapeau d'Espagne \n sous la seconde République, à part rouge et jaune ?", "A : marron", "B : violet", "C : cyan", "B"],
                    ["Datez la signature du plan Marshall", "A : 1950", "B : 1949", "C : 1947", "C"],
                    ["La marque Samsung est d'origine ?", "A : japonaise", "B : coréenne", "C : vietnamienne", "B"],
                    ["Datez la chute du Mur de Berlin", "A : 1992", "B : 1989", "C : 1990", "B"],
                    ["La Shueisha; au Japon; est ...", "A : une maison d'édition", "B : un siége social", "C une maison de disque","A"],
                    ["La guerre civil espagnole a duré...", "A : 5 ans", "B : 3 ans", "C : 1 ans", "B"],
                    ["Capital du Brésil", "A : Rio de Janeiro", "B : Brasilia", "C : Sao Paulo", "B"],
                    ["Qui est l'auteur de la Joconde ?", "A : Rembrandt", "B : Leonard de Vinci", "Van Gogh", "B"],
                    ["Lequel de ces fruits est un agrume ?", "A : Citron", "B : Banane", "C : Pêche", "A"],
                    ["Un croissant est...", "A : une pâtisserie", "B : Une viennoiserie", "C : Une tarte", "B"],
                    ["Quel peintre se coupa l'oreille ?", "A : Van Gogh", "B : Goya", "C : Cezanne", "A"],]

# Questions de S
questionS = [["Quelle est la forme exponentielle de z= -3i", "A : 4e^iπ/4", "B : 3e^iπ/2", "C : e^iπ/4", "B"],
             ["Les fuseaux neuromusculaires sont à l'origine...", "A : d'un message sensitif","B : d'un message moteur", "C : d'un potentiel de repos","A"],
             ["L'humérus est un os situé dans...", "A : La jambe", "B : Le bras", "C : Le pied", "B : 1976", "C : 1981", "C"],
             ["Quesque la spéciation géographique ?","A : la séparation d'une espèce suite \n à un évènement géographique","B : le réunion d'un espèce suite \n à un évènement géographique","C : la séparation de roches","A"],
             ["Dans un test d'immunodifusion, l'arc de précipitation révèle","A : les antigènes","B : les anticorps","C : les complexes anticorps & antigène ","C"]]

# Questions de L
questionL = [["De quel crime se rend coupable Œdipe ?", " A : parricide", "B : viol", "C : homicide","A"],
             ["Au XIXè siècle, dans quel pays Alexis de Tocqueville a-t-il été mandaté \n par le gouvernement français pour y \n étudier le système pénitentiaire ?","A : l'Angleterre","B: le Canada", "C : Etat-Unis", "C"],
             ["Qui a écrit << La Peste >> ?", "A : Jean-Paul Sartres", "B : Albert Camus", "C : Gustave Flaubert", "B"]]

# Questions de ES
questionES = [["Quelle notion pouvez-vous rattacher au soft power chinois ?", "A : le riz", "B : les mangas", "C : les instituts Confucius", "C"],
              ["Quand a eu lieu la Première Guerre du Golf ?", "A : En 1989-90", "B : En 1990-91", "C : En 1991-92", "B"],
              ["Lequel de ces états est frontalier de la Californie ?", "A : Le Nouveau-Mexique", "B : L'Utah", "C : L'Oregon", "C"],
              ["En quelle année Barack Obama a-t'il obtenue \n le prix nobel de la paix ?", "A : 2009", "B : 2012", "C : 2015", "A"],
              ["En quelle année François Mitterrand a-t-il été élu \n président de la République française ?", "A : 1974", "B :1976", "C : 1981", "C"]]

# Prison
Prison = [["Vous êtes en Prison pour sortir \n il faut faire un 6", "", "", "", ""]]

# Fonctions:

def temps():
    heure.set(time.strftime('%H:%M:%S'))                                        # fonction indiquant l'heure
    fenetre.after(1000,temps)

def lancer1():
    ''' lance un de a six faces '''
    global n1
    global couleur1
    if n1 < 118 :
        de1 = randint(1,6)
        n1 = n1 + de1
        labelResultat.config( text= str(de1)+" au lancé de dé" )
        if n1>119 :
            n1 = 119
            poserQuestionFiliere()
        couleur1 = fond.itemcget( case[n1] , 'fill' )
        coordonneeCase = fond.coords( case[n1] )                                #   coordonnees de la case n
        x1Case = int(coordonneeCase[0])                                         #   abscisse (en haut a gauche) de la case n
        y1Case = int(coordonneeCase[1])                                         #   ordonnee (en haut a gauche) de la case n
        fond.coords( joueur1 , x1Case+5 , y1Case+5 , x1Case+25 , y1Case+25 )
        if couleur1=='white' :
            prisonnier()
        else :
            poserQuestion()

def poserQuestion() :
    ''' pose une question   '''
    #   choix aleatoire d'une question
    global numeroCouleur
    global numeroQuestion
    numeroCouleur = couleur.index( couleur1 )                                   #   numero de cette couleur du joueur1
    nbQuestionCetteCouleur = len( question[numeroCouleur])                      #   nombre de questions pour cette couleur
    numeroQuestion = randint( 0 , nbQuestionCetteCouleur-1 )                    #   choix aleatoire d'un numero de question
    #   modification des textes
    etQuestion.config( text = question[numeroCouleur][numeroQuestion][0] )      #   question posée
    bouton1.config( text =  question[numeroCouleur][numeroQuestion][1] )        #   réponse A proposée
    bouton2.config( text =  question[numeroCouleur][numeroQuestion][2] )        #   réponse B proposée
    bouton3.config( text =  question[numeroCouleur][numeroQuestion][3] )        #   réponse C proposée

##  fonction ajoutee
def poserQuestionFiliere() :
    ''' pose une question dans chaque filiere '''
    global numeroCouleur
    global numeroQuestion
    if n1==119 :
        fond.coords( joueur1 , 1060 , 570 , 1080 , 590 )                        #   deplacement du pion
        numeroCouleur = couleur.index( "orangered" )                            #   couleur de la case S
    elif n1==120 :
        fond.coords( joueur1 , 1060 , 420 , 1080 , 440 )                        #   deplacement du pion
        numeroCouleur = couleur.index( "deepskyblue" )                          #   couleur de la case L
    elif n1==121 :
        fond.coords( joueur1 , 1060 , 270 , 1080 , 290 )                        #   deplacement du pion
        numeroCouleur = couleur.index( "chocolate" )                            #   couleur de la case ES
    elif n1==122 :
        fond.coords( joueur1 , 1060 , 120 , 1080 , 140 )                        #   deplacement du pion
        heureFin = time.strftime('%H:%M:%S')
        print( "heure de fin de partie :" , heureFin )
        if points>10 :
            texteFinal = "Bravo, vous avez eu votre baccalauréat !"
        else :
            texteFinal = "Dommage vous êtes recalé, vous devez repasser le baccalauréat"
        etQuestion.config( text = texteFinal )                                  #   message de fin
        bouton1.destroy()
        bouton2.destroy()
        bouton3  .destroy()
        btValider.destroy()
        resultatJoueur.destroy()
    if n1<122 :
        nbQuestionCetteCouleur = len( question[numeroCouleur])                  #   nombre de questions pour cette couleur
        numeroQuestion = randint( 0 , nbQuestionCetteCouleur-1 )                #   choix aleatoire d'un numero de question
        etQuestion.config( text = question[numeroCouleur][numeroQuestion][0] )
        bouton1.config( text =  question[numeroCouleur][numeroQuestion][1] )
        bouton2.config( text =  question[numeroCouleur][numeroQuestion][2] )
        bouton3.config( text =  question[numeroCouleur][numeroQuestion][3] )

##  fin de la fonction

def validation():
    ''' valide le choix et permet de continuer a poser des questions    '''
    global nbValidations
    global points
    global n1
    if n1<119 :
        nbValidations = nbValidations+1                                         #   le nombre de clics sur le bouton valider est incremente
        if (nbValidations%2==1) :                                               #   si le nombre de clics est impair
            if (choix.get() == question[numeroCouleur][numeroQuestion][4]) :    #   si le choix correspond a la bonne reponse
                etSelection.config( text="VRAI" )
                points = points + 1                                             #   on gagne un point a chaque bonne reponse
            else :                                                              #   si le choix ne correspond pas a la bonne reponse
                etSelection.config( text="FAUX, la bonne réponse était " + question[numeroCouleur][numeroQuestion][4] )
            resultatJoueur.config(text = 'score : '+ str(points))
            btValider.config( text="Lancer" )
        else :
            lancer1()
            etSelection.config( text="Choisissez une réponse" )
            btValider.config( text="Valider" )
    ##  nouvelle partie de la fonction
    else :                                                                      #   validation avec les dernières cases
        if (choix.get() == question[numeroCouleur][numeroQuestion][4]) :        #   si le choix correspond a la bonne reponse
            etSelection.config( text="VRAI" )
            n1 = n1 + 1                                                         #   on passe a la case suivante
        else :                                                                  #   si le choix ne correspond pas a la bonne reponse
            etSelection.config( text="FAUX, essayez à nouveau" )
            points = points - 1                                                 #   on perd un point a chaque mauvaise reponse
        resultatJoueur.config(text = 'score : '+ str(points))
        poserQuestionFiliere()
    ##  fin de la nouvelle partie

def selection() :
    selection = "Vous avez choisi la réponse " + choix.get()
    etSelection.config( text=selection )                                        #   modifie le texte de l'etiquette
    labelResultat.config( text="" )                                             #   efface le resultat du de


def lancerPrison():                                                             # Lance un dé en prison
    global dePrison
    dePrison = randint(1,6)
    resultatPrison.config( text = str(dePrison) )
    prisonnier()

def prisonnier() :                                                              # fonction Prison
    global n1
    coordonneeCase = fond.coords( case[123] )
    x1Case = int(coordonneeCase[0])
    y1Case = int(coordonneeCase[1])
    fond.coords( joueur1 , x1Case+5 , y1Case+5 , x1Case+25 , y1Case+25 )
    couleur1 = fond.itemcget( case[123] , 'fill' )
    btValider.place_forget()
    boutonPrison.place(x = 680, y = 710)
    resultatPrison.place(x = 700, y = 740)
    if dePrison==6 :
        n1 = n1-1
        coordonneeCase = fond.coords( case[n1-1] )
        x1Case = int(coordonneeCase[0])
        y1Case = int(coordonneeCase[1])
        fond.coords( joueur1 , x1Case+5 , y1Case+5 , x1Case+25 , y1Case+25 )
        boutonPrison.place_forget()
        btValider.place(x = 1320, y = 300)

if __name__=='__main__' :

    #   joueur1
    x, y = 50, 770
    joueur1 = fond.create_oval(x, y, x+20, y+20, fill = 'gold')
    n1 = 0                                                                      #   numero de la case du joueur1
    couleur1 = 'white'

    #   affiche le résultat du dé
    labelResultat = Label(fenetre , text = "" , fg = 'black' , bg = 'white')
    labelResultat.place( x=1400 , y=300 )

    #   score du joueur
    resultatJoueur = Label(fenetre, text = "", fg = 'black', bg = 'white')
    resultatJoueur.place( x = 1205, y = 350)

    heure = StringVar()                                                         #   variable de controle de type chaine de caracteres
    etHeure = Label(fenetre, textvariable=heure)
    etHeure.place( x=950 , y=10 )                                               #   pour faire apparaitre l'heure dans la fenetre
    temps()

    points = 0                                                                  #  nombre de points
    couleur = [ "red", "green", "blue", "purple", "black", "yellow", "orange", "orangered", "deepskyblue", "chocolate", "navy" ]
    question = [ questionRouge, questionVerte, questionBleue, questionViolette, questionNoire, questionJaune, questionOrange, questionS, questionL, questionES, Prison ]
    numeroCouleur = -1                                                          #   initialisation arbitraire
    numeroQuestion = -1                                                         #   initialisation arbitraire

    #   composants de la fenetre
    etQuestion = Label(fenetre, text = "question" )
    etQuestion.place(x = 1205, y = 10)

    choix = StringVar()                                                         #   variable de controle de type chaine de caracteres
    bouton1 = Radiobutton(fenetre, text = "reponse A", variable = choix, value = 'A', command = selection)
    bouton1.place(x = 1290, y = 100)
    bouton2 = Radiobutton(fenetre, text = "reponse B", variable = choix, value = 'B', command = selection)
    bouton2.place(x = 1290, y = 150)
    bouton3 = Radiobutton(fenetre, text = "reponse C", variable = choix, value = 'C', command = selection)
    bouton3.place(x = 1290, y = 200)
    etSelection = Label( fenetre, text="Faites votre choix" )                   #   etiquette indiquant la selection
    etSelection.place(x = 1270, y = 250)

    nbValidations = -1                                                          #   initialisation à -1 car on clique d'abord sur 'commencer' avant de lancer le premier dé
    btValider = Button(fenetre, text = "Commencer", command = validation)
    btValider.place(x = 1320, y = 300)

    boutonPrison = Button(fenetre, text = "Lancer", command = lancerPrison)
    resultatPrison = Label(fenetre, text = "", fg = 'red', bg = 'white')
    dePrison = 0

    heureDebut = time.strftime('%H:%M:%S')
    print( "heure de debut de partie :" , heureDebut )
    fenetre.mainloop()
