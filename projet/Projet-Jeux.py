import time
import os
from random import randint
import requests
##vie = 100 
#degat = 50
#monstrevie = 45
#monstreAtt = 23
monstreLVL = 0
#monstreXp = 0
#mana = 100
#degatMagique = 100       # 40 mana utilisé
#attM = 40
#gdegatMagique = 200      # 60 mana
#gAttM = 60
#soin = 50                # 40 mana utilisé
#soinM = 40
vague = 0
win = 0
#niveau = 1
#xpReq = 100
#xp = 0


class Mob:
    def attaque_mob(self, mob):
        degat = self.degat + randint(1, 100)
        monstres.prend_des_degats(degat)
 

class Perso(Mob):
    VIE = 100
    DEGAT = 50
    MANA = 100
    DEGATMAGIQUE = 100
    GDEGAMAGIQUE = 200
    SOIN = 100
    NIVEAU = 1
    VIE_MAX = 100
    MANA_MAX = 100
    def __init__(self, nom, NIVEAU = 1):
        self.niveau = NIVEAU
        self.nom = nom
        self.vie = round (self.VIE)
        self.vie_max = self.VIE_MAX 
        self.degat = self.DEGAT 
        self.mana = self.MANA 
        self.mana_max = self.MANA_MAX 
        self.degatMagique = self.DEGATMAGIQUE       # 40 mana utilisé
        self.attM = 40
        self.gdegatMagique = self.GDEGAMAGIQUE   # 60 mana
        self.gAttM = 60
        self.soin = self.SOIN                # 40 mana utilisé
        self.soinM = 40
        self.xpReq = 250
        self.xp = 0


class Mage(Perso):
    pass

class Guerrier(Perso):
    pass

class Item(Mob):
    NOM = 'anneau'
    ITEM_POP = 1
    ANNEAU_VIE = 100
    DOUBLE_VIE = 0
    ANNEAU_DEGAT = 50
    DOUBLE_DEGAT = 0
    ANNEAU_DEGAT_M = 75
    DOUBLE_DEGAT_M = 0
    ANNEAU_SOIN = 100
    DOUBLE_SOIN = 0
    ANNEAU_WIN = 0

    def __repr__(self):
        return self.nom

    def __init__(self):

        self.nom = type(self).__name__.lower()
        self.anneau_vie = self.ANNEAU_VIE
        self.double_vie = self.DOUBLE_VIE
        self.anneau_degat = self.ANNEAU_DEGAT
        self.double_degat = self.DOUBLE_DEGAT
        self.anneau_degat_m = self.ANNEAU_DEGAT_M
        self.double_degat_m = self.DOUBLE_DEGAT_M
        self.anneau_soin = self.ANNEAU_SOIN
        self.double_soin = self.DOUBLE_SOIN
        self.anneau_win = self.ANNEAU_WIN

class rien(Item):
    NOM = 'rien'
    ITEM_POP = 1

class anneau_vie(Item):
    NOM = 'un anneau de vie'
    ITEM_POP = 90
    ANNEAU_VIE = 100
    DOUBLE_VIE = 0

class anneau_degat(Item):
    NOM = 'un anneau de dégat'
    ITEM_POP = 92
    ANNEAU_DEGAT = 50
    DOUBLE_DEGAT = 0

class anneau_degat_m(Item):
    NOM = 'un anneau de dégat magique'
    ITEM_POP = 94
    ANNEAU_DEGAT_M = 75
    DOUBLE_DEGAT_M = 0

class anneau_soin(Item):
    NOM = 'un anneau de soin'
    ITEM_POP = 96
    ANNEAU_SOIN = 100
    DOUBLE_SOIN = 0

class anneau_win(Item):
    NOM = ' un anneau sacré'
    ITEM_POP = 98
    ANNEAU_WIN = 0

LIST_ITEM = sorted([rien, anneau_degat, anneau_degat_m, anneau_soin, anneau_vie, anneau_win], key=lambda x: -x.ITEM_POP)
def pop_item():
    pop_value = randint(1, 100)
    for item in LIST_ITEM:
        if pop_value > item.ITEM_POP:
            return item

class Monstre(Mob):
    NOM = 'Monstre'
    CHANCE_POP = 1
    vie_BASE = 45
    attaque_BASE = 23
    XP_DROP = 1

    def __repr__(self):
        return self.nom

    def __init__(self, lvl=1):
        self.nom = type(self).__name__.lower()
        self.level = lvl
        self.xp_drop = round (self.XP_DROP * (lvl / 25 + 1))
        self.vie = round (self.vie_BASE * (lvl / 25 + 1))
        self.attaque = round (self.attaque_BASE + lvl)
    
class Gobelin(Monstre):
    CHANCE_POP = 0
    vie_BASE = 45
    attaque_BASE = 25
    XP_DROP = 100

class Loup(Monstre):
    CHANCE_POP = 60
    vie_BASE = 60
    attaque_BASE = 40
    XP_DROP = 200

class Phoenix(Monstre):
    CHANCE_POP = 80
    vie_BASE = 70
    attaque_BASE = 55
    XP_DROP = 300

class Hydre(Monstre):
    CHANCE_POP = 90
    vie_BASE = 90
    attaque_BASE = 70
    XP_DROP = 500

class Crapaud(Monstre):
    CHANCE_POP = 98
    vie_BASE = 50
    attaque_BASE = 0
    XP_DROP = 3000


LIST_MONSTRES = sorted([Crapaud, Hydre, Phoenix, Loup, Gobelin], key=lambda x: -x.CHANCE_POP)
def pop_monstre(lvl):
    pop_value = randint(1, 100)
    for monstre in LIST_MONSTRES:
        if pop_value > monstre.CHANCE_POP:
            return monstre(lvl)


os.system("cls")
joueur1 = Perso('Mage')
joueur2 = Perso('Guerrier')

print("Bienvenue jeune aventurier.")
choix = int(input("Veux-tu commencer une dangereuse quête ?\n1: oui\n2: non\n"))
os.system("cls")
if choix == 1:
    print("Ok, bienvenue dans ce monde magique et plein de mystère.")
    choix2 = int (input("Veux-tu que je t'explique les règles de ce monde magique ?\n1: oui\n2: non\n"))
    os.system("cls")

    if choix2 == 1:
        print("Ok, je vais t'expliquer les règles de ce monde.\n\npour commencer dans ce monde, il existe 5 différents type de créature:\n\n- Le Gobelin (le plus faible)\n- Le Loup\n- Le Phoenix\n- L'hydre (le plus fort)\n- Le Crapaud qui est un monstre qui n'attaque presque pas, mais qui va te donner plein d'XP.\n ")
        input("Appuis sur la touche entrée pour aller a la page suivante.")
        os.system("cls")
        print("ensuite parlons des combats.\n\nLes combats sont du tour par tour sauf pour le heal ou le monstre ne vas pas t'attaquer mais tu perdra du mana.\n\npendant les combats tu auras la possibilité d'esquiver tu pourra choisir si oui ou non tu veut esquiver tu devra choisir un nombre entre 1 et 6.\n\nSi par contre tu n'arrive pas a esquiver le monstre vas t'infliger plus de degat.\n ")
        input("Appuis sur la touche entrée pour aller a la page suivante.")
        os.system("cls")
        print("Il y a aussi les niveau.\n\nPour les niveaux du joueur,\ntu pourras récupérer de l'Xp en tuant des monstre et quand tu montera de niveau tu pourras augmenter une compétance de ton choix.\n\nPour les niveau du monstre,\nils seront défini aléatoirement en fonction de ton nombre de vague plus ton nombre de vague est haut plus son niveau sera élever.\n")
        input("Appuis sur la touche entrée pour aller a la page suivante.")
        os.system("cls")
        print("parlons un peu des items que tu pourra encontrer. Il existe 5 différents type d'item: 4 qui donne des bonus et 1 qui te fera gagner la partie.\n")
        input("Appuis sur la touche entrée pour aller a la page suivante.")
        os.system("cls")
        print("Ok, je vais t'expliquer le but de ton aventure.\nIl n'y a pas très longtemps, j'ai perdu un anneau nommé (Anneau Sacré) qui servait a protéger mon village des monstres, je sais juste qu'un monstre me l'a voler tu doit donc je retrouvais pour me le rendre.")
        print("Pour finir, je voulais te dire que tous les messages que tu auras pendant cette aventure, tu devras appuyer sur la touche entre quand tu les auras lu.")
        input("Appuis sur la touche entrée pour aller a la page suivante.")
        os.system("cls")

    if choix2 == 2:
        input("Ok, je vais t'expliquer le but de ton aventure.\nIl n'y a pas très longtemps, j'ai perdu un anneau nommé (Anneau Sacré) qui servait a protéger mon village des monstres, je sais juste qu'un monstre me l'a voler tu doit donc je retrouvais pour me le rendre.")
        os.system("cls")
         
if choix == 2:
    print("Ok, revient me voir quand tu seras prêt.")
    exit(0)
#______________________________________________________________________________________________________________________________________
while joueur1.vie > 0:

    if win == 1:
        break
    monstreLVL = 1
    vague += 1
    if vague % 3 == 0:
        joueur1.vie = joueur1.vie + 100
        print("Vous récuperez récuperez 100 Pv.")
        input()

    if vague % 5 == 0:
        joueur1.mana = joueur1.mana + 100
        print("Vous récuperez récuperez 100 mana.")
        input()

    if vague > 5:
        monstreLVL += randint(vague, vague + 10) 
    else:
        monstreLVL += randint(vague, vague + 10)  
   
    monstre_apparu = pop_monstre(monstreLVL)
    item_apparu = pop_item()
#______________________________________________________________________________________________________________________________________
    while True:
        if joueur1.vie <= 0:
            break 

        if joueur1.xp >= joueur1.xpReq:

            while joueur1.xpReq <= joueur1.xp:
                joueur1.xp -= joueur1.xpReq
                joueur1.xpReq *= 1.5
                joueur1.niveau += 1
                print("Bien jouer vous avez augmenter de niveau.\nVous etes maintenant niveau", joueur1.niveau)
                print("\nQuelle competance voulez-vous augmenter ?\n")
                choix = int(input("1: attaque normale (+10).\n2: Attaque magique (+15).\n3: Grosse attaque magique (+20).\n4: Soin (+50).\n" ))
                if choix == 1:
                    joueur1.degat += 10
                    joueur1.vie += 10
                    joueur1.VIE_MAX += 10
                if choix == 2:
                    joueur1.degatMagique += 15
                    joueur1.vie += 10
                    joueur1.VIE_MAX += 10
                if choix == 3:
                    joueur1.gdegatMagique += 20
                    joueur1.vie += 10
                    joueur1.VIE_MAX += 10
                if choix == 4:
                    joueur1.soin += 50
                    joueur1.vie += 10
                    joueur1.VIE_MAX += 10
                os.system("cls")

        
        print("Vous rencontrez un" ,monstre_apparu.nom)
        print("Choissez une action a faire:\n")
        reponse = int(input("1: Voir les statistique du joueur.\n2: Voir les statistique du monstre.\n3: Voir les différentes attaques.\n4: Voir les différents items.\n5: attaque normale. \n6: attaque magique.\n7: Grosse attaque magique.\n8: Soin.\n9: Suicide.\n"))
        os.system("cls")
#______________________________________________________________________________________________________________________________________
        if reponse == 1:
            print("Vous êtes à la vague",vague,"\n")
            print("Vous êtes au niveau",joueur1.niveau,"\n")
            print("Xp manquante avant prochain niveau : %dxp\n" % (joueur1.xpReq - joueur1.xp))
            print("vous avez",joueur1.xp,"xp\n")
            print("Vous avez %d Hp\n" % joueur1.vie)
            print("Vous avez",joueur1.mana,"mana\n")
            print("Votre attaque normale fait",joueur1.degat,"Dégat\n")
            print("Votre attaque magique fait",joueur1.degatMagique,"Dégat\n")
            print("Votre grosse attaque magique fait",joueur1.gdegatMagique,"Dégat\n")
            print("Vous pouvez vous heal de",joueur1.soin,"Hp\n")
            input("Quand vous avez terminé de consulter vos statistiques tapez sur une touche.\n")
            os.system("cls")
#______________________________________________________________________________________________________________________________________
        if reponse == 2:
            print("le monstre est un", monstre_apparu.nom,"\n")
            print("Le monstre est LVL",monstre_apparu.level,"\n")
            print("Le monstre a",monstre_apparu.vie,"PV\n")
            print("Le monstre fait",monstre_apparu.attaque,"degat\n")
            print("Le monstre drop", monstre_apparu.xp_drop, "Xp\n\n")
            input("Quand vous avez terminé de consulter les statistiques tapez sur une touche.\n")
            os.system("cls")
#______________________________________________________________________________________________________________________________________       
        if reponse == 3:
            print("attaque normale:\nDegat = ",joueur1.degat,"\nmana utilisé = 0\n")
            print("attaque magique:\nDegat = ",joueur1.degatMagique,"\nmana utilisé = ",joueur1.attM)
            print("\nGrosse attaque magique:\nDegat = ",joueur1.gdegatMagique,"\nmana utilisé = ",joueur1.gAttM)
            print("\nSoin:\nPV ajouter = ",joueur1.soin,"\nmana utilisé = ",joueur1.soinM)
            input("Quand vous avez terminé de consulter les attaques tapez sur une touche.\n")
            os.system("cls")  
#______________________________________________________________________________________________________________________________________
        if reponse == 4:
            print(anneau_vie.NOM,":\n+",anneau_vie.ANNEAU_VIE,"vie.\n")
            print(anneau_degat.NOM,":\n+",anneau_vie.ANNEAU_DEGAT,"dégat.\n")
            print(anneau_degat_m.NOM,":\n+",anneau_vie.ANNEAU_DEGAT_M,"dégat magique.\n")
            print(anneau_soin.NOM,":\n+",anneau_vie.ANNEAU_SOIN,"soin.\n")
            print(anneau_win.NOM,":\n Victoire.")
            
            print(item_apparu.NOM)
            if item_apparu.NOM == "rien":
                print(item_apparu.NOM, "tttttttttttttttttttttttttttttttttttt")
                win = 1
                print(win)
                input()
                break
                

            input()
            os.system("cls")
#______________________________________________________________________________________________________________________________________       
        if reponse == 5:
            monstre_apparu.vie -= joueur1.degat
            print("Vous attaquez le monstre, Vous lui infligez",joueur1.degat,"PV.\n")
            
            if monstre_apparu.vie <= 0:
                print("vous avez tuer un",monstre_apparu.nom)
                print("Le",monstre_apparu.nom,"vous drop",monstre_apparu.xp_drop,"Xp.")
                joueur1.xp += monstre_apparu.xp_drop
                input()
                os.system("cls")
                break

            print("Le",monstre_apparu.nom," vas vous attaquer voulez-vous esseyer de l'Esquiver?")
            reponse2 = int (input("1: Oui\n2: Non\n"))

            if reponse2 == 1:
                reponse3 = int (input("Ok, choisissez un chiffre entre 1 et 6.\n"))
                rand = randint(1, 6)
                print(rand)

                if rand == reponse3:
                    input("Bravo! Tu as réussi a ésquiver l'attaque.\n")
                    os.system("cls")
                else:
                    print("Domage! Tu n'as pas réussi a esquiver l'attaque le" ,monstre_apparu.nom,"vous inflige %d degat." % (monstre_apparu.attaque * 1.2))
                    joueur1.vie -= monstre_apparu.attaque*1.2
                    input()
                    os.system("cls")

            if reponse2 == 2:
                joueur1.vie -= monstre_apparu.attaque
                print("l'attaque du" ,monstre_apparu.nom, "vous inflige",monstre_apparu.attaque,".")
                input()
                os.system("cls")  
#______________________________________________________________________________________________________________________________________
        if reponse == 6:

            if joueur1.mana - joueur1.attM <   0:
                input("vous n'avez pas assez de mana\n")
                os.system("cls")

                if monstre_apparu.vie <= 0:
                    print("vous avez tuer un",monstre_apparu.nom)
                    print("Le",monstre_apparu.nom,"vous drop",monstre_apparu.xp_drop,"Xp.")
                    joueur1.xp += monstre_apparu.xp_drop

                    input()
                    os.system("cls")
                    break

            else:
                monstre_apparu.vie -= joueur1.degatMagique
                print("Vous attaquez le",monstre_apparu.nom, ", Vous lui infligez",joueur1.degat,"PV.\n") 
                joueur1.mana -= joueur1.attM
                print("vous perdez",joueur1.attM,"mana\n")

                if monstre_apparu.vie <= 0:
                    print("vous avez tuer un",monstre_apparu.nom)
                    print("\nLe",monstre_apparu.nom,"vous drop",monstre_apparu.xp_drop,"Xp.")
                    joueur1.xp += monstre_apparu.xp_drop
                    input()
                    os.system("cls")
                    break

                print("Le ",monstre_apparu.nom," vas vous attaquer voulez-vous esseyer de l'Esquiver?")
                reponse2 = int (input("1: Oui\n2: Non\n"))


                if reponse2 == 1:
                    reponse3 = int (input("Ok, choisissez un chiffre entre 1 et 6.\n"))
                    rand = randint(1, 6)
                    print(rand)

                    if rand == reponse3:
                        input("Bravo! Tu as réussi a ésquiver l'attaque.\n")
                        os.system("cls")
                    else:
                        print("Domage! Tu n'as pas réussi a esquiver l'attaque le " ,monstre_apparu.nom, " vous inflige %d degat." % (monstre_apparu.attaque * 1.2))
                        joueur1.vie -= monstre_apparu.attaque * 1.2
                        print("Le" ,monstre_apparu.nom, "vous attaque.\n")
                        input()
                        os.system("cls")

                if reponse2 == 2:
                    joueur1.vie -= monstre_apparu.attaque
                    print("l'attaque du ",monstre_apparu.nom ,"vous inflige",monstre_apparu.attaque,".")
                    input()
                    os.system("cls")
#______________________________________________________________________________________________________________________________________
        if reponse == 7:

            if joueur1.mana - joueur1.gAttM < 0:
                input("vous n'avez pas assez de mana\n")
                os.system("cls")
    
            else:
                monstre_apparu.vie -= joueur1.gdegatMagique
                print("Vous attaquez le ",monstre_apparu.nom ,", Vous lui infligez",joueur1.degat,"PV.\n") 
                joueur1.mana -= joueur1.gAttM
                print("vous perdez",joueur1.gAttM,"mana\n")

                if monstre_apparu.vie <= 0:
                    print("vous avez tuer un",monstre_apparu)
                    print("\nLe",monstre_apparu.nom ,"vous drop",monstre_apparu.xp_drop,"Xp.")
                    joueur1.xp += monstre_apparu.xp_drop
                    input()
                    os.system("cls")
                    break                

                print("Le ",monstre_apparu.nom ," vas vous attaquer voulez-vous esseyer de l'Esquiver?")
                reponse2 = int (input("1: Oui\n2: Non\n"))

                if reponse2 == 1:
                    reponse3 = int (input("Ok, choisissez un chiffre entre 1 et 6.\n"))
                    rand = randint(1, 6)
                    print(rand)

                    if rand == reponse3:
                        input("Bravo! Tu as réussi a ésquiver l'attaque.")
                        os.system("cls")
                    else:
                        print("Domage! Tu n'as pas réussi a esquiver l'attaque le " ,monstre_apparu.nom, " vous inflige %d degat." % (monstre_apparu.attaque * 1.2))
                        joueur1.vie -= monstre_apparu.attaque * 1.2
                        input()
                        os.system("cls")

                if reponse2 == 2:
                    joueur1.vie -= monstre_apparu.attaque
                    print("l'attaque du ",monstre_apparu.nom," vous inflige",monstre_apparu.attaque,".")
                    os.system("cls")
#______________________________________________________________________________________________________________________________________
        if reponse == 8:

            if joueur1.mana - joueur1.soinM < 0 :
                input("vous n'avez pas assez de mana\n")
                os.system("cls")

            else:
                print("Voulez-vous esseyer de Doubler le soin?")
                reponse2 = int (input("1: Oui\n2: Non\n"))

                if reponse2 == 1:
                    reponse3 = int (input("Ok, choisissez un chiffre entre 1 et 6.\n"))
                    rand = randint(1, 6)
                    print(rand)

                    if rand == reponse3:
                        print("Bravo! Tu as réussi tu double ton soin.")
                        joueur1.vie += joueur1.soin * 2
                        print("vous venez de vous soigner.\n") 
                        joueur1.mana -= joueur1.soinM
                        print("vous perdez",joueur1.soinM,"mana\n")
                        input()
                        os.system("cls")

                    else:
                        print("Domage! Tu n'as pas réussi a doubler le soin.")
                        joueur1.vie += joueur1.soin
                        print("vous venez de vous soigner.\n") 
                        joueur1.mana -= joueur1.soinM
                        print("vous perdez",joueur1.soinM,"mana\n")
                        input()
                        os.system("cls")

                if reponse2 == 2:
                    joueur1.vie += joueur1.soin
                    print("vous venez de vous soigner.\n") 
                    joueur1.mana -= joueur1.soinM
                    print("vous perdez",joueur1.soinM,"mana\n")
                    input()
                    os.system("cls")
#______________________________________________________________________________________________________________________________________
        if reponse == 9:
            print("Cela veut dire que vous Abandonnez la partie.") 
            print("Êtes-vous sur de vouloirs vous suicider ?")
            reponse2 = int (input("1: Oui\n2: Non\n"))
            if reponse2 == 1:
                joueur1.vie = 0
                os.system("cls")
                break

            if reponse2 == 2:
                input("Ok, continuez")
                os.system("cls")

if joueur1.vie <= 0 or win == 1:
    print("Vous etes mort!")
    user = input("Choisissez votre pseudo\n")
    print("Merci d'avoir joué",user,".")
    url = "http://localhost:2004/history.py?vie="+str(joueur1.vie)+"&name="+user+"&vague="+str(vague)+"&niveau="+str(joueur1.niveau)
    r = requests.get(url)