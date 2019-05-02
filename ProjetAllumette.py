 # script Allumete.py

from tkinter import *
import random
from random import *
from tkinter.messagebox import*


def allumette():
    """ Placer les allumettes à partir de x=50 et y=20 au NW  """
    x = 50
    y = 20
    Compteur_Allumette=0
    Liste_Allumette=[]
    Nombre_Allumette =len(Canevas.find_all())
    
    if Nombre_Allumette==0:
        for i in range(36):
            Allumette = Canevas.create_image(x,y, anchor=NW, image=gifAllumette)
            Compteur_Allumette= Compteur_Allumette+1
            Liste_Allumette.append(Compteur_Allumette)  
            x += 51
            if x>Largeur-50:
                x=50
                y += 103
            
        print("Création du jeu de" ,  Compteur_Allumette ," allumettes")
        # affichage la liste des allumettes
        print(Liste_Allumette)
        
      
    
    
def Qui_Commence():
    Liste_Allumette = Canevas.find_all()
    qui_commence = randint(1,2)
    if qui_commence == 1:
        
        print( "Le hasard décide que l'ordinateur commence et il enlève 1 allumette !")
        showinfo("Ordinateur", "Le hasard décide que l'ordinateur commence et il enlève 1 allumette !")
        Canevas.delete(Liste_Allumette[-1])
        
    if qui_commence == 2 :
        print(" C'est vous qui commencez !")
        showinfo("Ordinateur", "C'est vous qui commencez !")

        
def jouer():
    Nombre_Allumette =len(Canevas.find_all())
    if Nombre_Allumette==0:
        allumette()
        Qui_Commence()
    else :
        if Nombre_Allumette>0:
            showwarning("Attention !", "Une partie est déjà en cours terminez-là avant!")
    


def Undo():
    if len(Canevas.find_all()) > 0:
        try:
            Liste_Allumette = Canevas.find_all()
            # on efface la dernière allumette
            Canevas.delete(Liste_Allumette[-1])
            print("Le joueur à retiré 1 allumette")
            Dernier_Nombre_Allumette =len(Canevas.find_all())
            showinfo("Joueur","Vous avez décidé de retirer 1 allumette!")
            print("il reste donc ", Dernier_Nombre_Allumette, "allumette(s)")
            Ordi()
        except IndexError:
            showwarning("Attention", "Non je rigole ça sert à rien")
    



def Undo2():
    if len(Canevas.find_all()) > 0:
        try:
            Liste_Allumette = Canevas.find_all()
            # on efface les 2 dernières allumette
            Canevas.delete(Liste_Allumette[-1],Liste_Allumette[-2])
            Dernier_Nombre_Allumette =len(Canevas.find_all())
            print("Le joueur à retiré 2 allumettes")
            showinfo("Joueur","Vous avez décidé de retirer 2 allumettes!")
            print("il reste donc ", Dernier_Nombre_Allumette, "allumette(s)")
            Ordi()
        except IndexError:
            showwarning("Attention", "Vous ne pouvez pas retirer 2 allumettes s'il n'y en a moins")
        
def Undo3():
    if len(Canevas.find_all()) > 0:
        try:
            Liste_Allumette = Canevas.find_all()
            # on efface les 3 dernières allumettes
            Canevas.delete(Liste_Allumette[-1],Liste_Allumette[-2],Liste_Allumette[-3])
            Dernier_Nombre_Allumette =len(Canevas.find_all())
            print("Le joueur à retiré 3 allumettes")
            print("il reste donc ", Dernier_Nombre_Allumette, "allumette(s)")
            showinfo("Joueur","Vous avez décidé de retirer 3 allumettes!")
            Ordi()
        except IndexError:
            showwarning("Attention", "Vous ne pouvez pas retirer 3 allumettes s'il n'y en a moins")
        

        
        
def Undo4():
    if len(Canevas.find_all()) > 0:
        try:
            Liste_Allumette = Canevas.find_all()
            # on efface les 4 dernières allumettes
            Canevas.delete(Liste_Allumette[-1],Liste_Allumette[-2],Liste_Allumette[-3],Liste_Allumette[-4])
            print("Le joueur à retiré 4 allumettes")
            Dernier_Nombre_Allumette =len(Canevas.find_all())
            showinfo("Joueur","Vous avez décidé de retirer 4 allumettes!")
            print("il reste donc ", Dernier_Nombre_Allumette, "allumette(s)")
            Ordi()
        except IndexError:
            showwarning("Attention", "Vous ne pouvez pas retirer 4 allumettes s'il n'y en a moins")

def Undo5():
    if len(Canevas.find_all()) > 0:
        try:
            Liste_Allumette = Canevas.find_all()
            # on efface les 5 dernières allumettes
            Canevas.delete(Liste_Allumette[-1],Liste_Allumette[-2],Liste_Allumette[-3],Liste_Allumette[-4],Liste_Allumette[-5])
            print("Le joueur à retiré 5 allumettes")
            showinfo("Joueur","Vous avez décidé de retirer 5 allumettes!")
            Dernier_Nombre_Allumette =len(Canevas.find_all())
            print("il reste donc ", Dernier_Nombre_Allumette, "allumette(s)")
            Ordi()
        
        except IndexError:
            showwarning("Attention", "Vous ne pouvez pas retirer 5 allumettes s'il n'y en a moins")
        
def Undo6():
    if len(Canevas.find_all()) > 0:
        try:
            Liste_Allumette = Canevas.find_all()
            # on efface les 6 dernière allumettes
            Canevas.delete(Liste_Allumette[-1],Liste_Allumette[-2],Liste_Allumette[-3],Liste_Allumette[-4],Liste_Allumette[-5],Liste_Allumette[-6])
            print("Le joueur à retiré 6 allumettes")
            showinfo("Joueur","Vous avez décidé de retirer 6 allumettes!")
            Dernier_Nombre_Allumette =len(Canevas.find_all())
            print("il reste donc ", Dernier_Nombre_Allumette, "allumette(s)")
            Ordi()

        except IndexError:
            showwarning("Attention", "Vous ne pouvez pas retirer 6 allumettes s'il n'y en a moins")
        
def Ordi():
    Mafenetre.after(1000)
    Liste_Allumette = Canevas.find_all()
    Dernier_Nombre_Allumette = len(Liste_Allumette)
    Compteur_Allumettes_Retirées_par_Ordi=0
    
    Allumettes_retirées_par_Ordi= "L'ordinateur decide de retirer",   Compteur_Allumettes_Retirées_par_Ordi , 'allumette(s)!'
    
    if Dernier_Nombre_Allumette==0:
        showinfo("Ordinateur", " Partie terminée, l'ordinateur a perdu! \n Tu es un(e) vrai(e) pro")
        retry()
        
    
    
    if Dernier_Nombre_Allumette>0:
        if Dernier_Nombre_Allumette%7>=1:
            while Dernier_Nombre_Allumette%7>=1:
                Canevas.delete(Liste_Allumette[-1])
                Liste_Allumette = Canevas.find_all()
                Dernier_Nombre_Allumette= Dernier_Nombre_Allumette-1
                Compteur_Allumettes_Retirées_par_Ordi= Compteur_Allumettes_Retirées_par_Ordi+1
            
            Allumettes_retirées_par_Ordi= "L'ordinateur decide de retirer",   Compteur_Allumettes_Retirées_par_Ordi , 'allumette(s)!'
            showinfo("Ordinateur", Allumettes_retirées_par_Ordi)


        else:
            if Dernier_Nombre_Allumette%7==0:
                h= randint(1,6)
                for n in range(h):
                    Canevas.delete(Liste_Allumette[-1])
                    Liste_Allumette = Canevas.find_all()
                    Dernier_Nombre_Allumette= Dernier_Nombre_Allumette-1
                    Compteur_Allumettes_Retirées_par_Ordi= Compteur_Allumettes_Retirées_par_Ordi+1
            Allumettes_retirées_par_Ordi= 'l ordinateur decide de retirer',   Compteur_Allumettes_Retirées_par_Ordi , 'allumette(s)!'
            showinfo("Ordinateur", Allumettes_retirées_par_Ordi)
            
        print("l'ordinateur decide de retirer ", Compteur_Allumettes_Retirées_par_Ordi ," allumettes")
        print("Il reste donc ", Dernier_Nombre_Allumette, "allumette(s)")
            
        if Dernier_Nombre_Allumette==0:
            showinfo("Ordinateur", " Partie terminée, l'ordinateur est triomphant!")
            retry()
    
        
            
def retry(): #Fonction pour recommencer lorsque que l'on perd ou gagne
    if askyesno('Ordinateur', 'Voulez vous recommencer?'):
        jouer()
    else:
        showinfo('Ordinateur', 'Dommage...')
        Mafenetre.destroy()
            
    


# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title('Jeux des allumettes')

# Image de fond
gifAllumette = PhotoImage(file="allumette2.gif")

# Création d'un widget Canvas (zone graphique)
Largeur = 356
Hauteur = 638
Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg = "white")
Canevas.pack(padx =5, pady =5)

# Création d'un widget Button Jouer
BoutonGo = Button(Mafenetre, text ='Jouer', command = jouer)
BoutonGo.pack(side = LEFT, padx = 5, pady = 5)

# Création d'un widget Button Retirer une allumette
BoutonEffacer1 = Button(Mafenetre, text ='Retirer une allumette', command = Undo)
BoutonEffacer1.pack(side = LEFT, padx = 5, pady = 5)

#Création d'un widget Button Retirer deux allumettes
BoutonEffacer2 = Button(Mafenetre, text ='Retirer deux allumettes', command = Undo2)
BoutonEffacer2.pack(side = LEFT, padx = 5, pady = 5)

#Création d'un widget Button Retirer trois allumettes
BoutonEffacer3 = Button(Mafenetre, text ='Retirer trois allumettes', command = Undo3 )
BoutonEffacer3.pack(side = LEFT, padx = 5, pady = 5)

#Création d'un widget Button Retirer quatre allumettes
BoutonEffacer4 = Button(Mafenetre, text ='Retirer quatre allumettes', command = Undo4)
BoutonEffacer4.pack(side = LEFT, padx = 5, pady = 5)

#Création d'un widget Button Retirer cinq allumettes
BoutonEffacer5 = Button(Mafenetre, text ='Retirer cinq allumettes', command = Undo5)
BoutonEffacer5.pack(side = LEFT, padx = 5, pady = 5)

#Création d'un wiget Button Retirer six allumettes
BoutonEffacer6 = Button(Mafenetre, text ='Retirer six allumettes', command = Undo6)
BoutonEffacer6.pack(side = LEFT, padx = 5, pady = 5)

# Création d'un widget Button (bouton Quitter)
BoutonQuitter = Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy)
BoutonQuitter.pack(side = LEFT, padx = 5, pady = 5)


Mafenetre.mainloop()
  