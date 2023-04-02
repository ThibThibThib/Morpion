import tkinter as tk
from tkinter import messagebox
import webbrowser


## -------Joueur-------##
player1 = 3
player2 = 1
compteur = 0
compteur2 = 0
# Constantes
LARGEUR = 300
HAUTEUR = 305


def Jouer_Rejouer():
    """ Efface la zone graphique et reset case 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8, 9 ..... """
    surface_dessin.delete(tk.ALL)

    """Dessine la grille du Morpion """
    surface_dessin.create_line(100, 300, 100, 0, fill="green", width=5)
    surface_dessin.create_line(200, 300, 200, 0, fill="green", width=5)
    surface_dessin.create_line(0, 100, 300, 100, fill="green", width=5)
    surface_dessin.create_line(0, 200, 300, 200, fill="green", width=5)
    surface_dessin.create_line(0, 2, 300, 2, fill="green", width=5)
    surface_dessin.create_line(0, 302, 300, 302, fill="green", width=5)
    surface_dessin.create_line(300, 0, 300, 300, fill="green", width=5)
    surface_dessin.create_line(3, 0, 3, 300, fill="green", width=5)

    """       Tout les clics        """
    toute_les_clics = ["clic1", "clic2", "clic3", "clic4",
                       "clic5", "clic6", "clic7", "clic8", "clic9"]

    """     initialiser chaque variable à False      """
    for toute_les_clics in toute_les_clics:
        globals()[toute_les_clics] = False

    """Toute les cases"""
    toute_les_cases = ["case1", "case2", "case3", "case4", "case5", "case6", "case7", "case8", "case9",
                       "case1b", "case2b", "case3b", "case4b", "case5b", "case6b", "case7b", "case8b", "case9b",]

    """initialiser chaque variable à False """
    for toute_les_cases in toute_les_cases:
        globals()[toute_les_cases] = False


## -------Jeu-------##


def clic(event):
    """ Gestion de l'événement clic gauche sur la zone graphique """
    global player1, player2
    global clic1, clic2, clic3, clic4, clic5, clic6, clic7, clic8, clic9
    global case1, case2, case3, case4, case5, case6, case7, case8, case9, case1b, case2b, case3b, case4b, case5b, case6b, case7b, case8b, case9b
    X = event.x
    Y = event.y

    # -------Création de rond et croix et quand les joueurs doivent jouer-------##
    if X < 100 and Y < 100:
        clic1 = True
        if player1 % 2 == 0:
            if case1b == True:
                tk.messagebox.showinfo(
                    title="Impossible", message="Les ronds ont déjà jouer")
            else:
                surface_dessin.create_line(8, 8, 95, 95, fill="blue", width=10)
                surface_dessin.create_line(95, 8, 8, 95, fill="blue", width=10)
                player2 += 1
                player1 += 1
                case1 = True
        else:
            if case1 == True:
                tk.messagebox.showinfo(
                    title="Impossible", message="Les croix ont déjà jouer")
            else:
                surface_dessin.create_circle(
                    50, 50, 43,  outline="red", width=4)
                player2 += 1
                player1 += 1
                case1b = True
    elif X < 200 and Y < 100:
        clic2 = True
        if player1 % 2 == 0:
            if case2b == True:
                tk.messagebox.showinfo(
                    title="Impossible", message="Les ronds ont déjà jouer")
            else:
                surface_dessin.create_line(
                    108, 8, 195, 95, fill="blue", width=10)
                surface_dessin.create_line(
                    195, 8, 108, 95, fill="blue", width=10)
                player2 += 1
                player1 += 1
                case2 = True
        else:
            if case2 == True:
                tk.messagebox.showinfo(
                    title="Impossible", message="Les croix ont déjà jouer")
            else:
                surface_dessin.create_circle(
                    150, 50, 43,  outline="red", width=4)
                player2 += 1
                player1 += 1
                case2b = True
    elif X < 300 and Y < 100:
        clic3 = True
        if player1 % 2 == 0:
            if case3b == True:
                tk.messagebox.showinfo(
                    title="Impossible", message="Les ronds ont déjà jouer")
            else:
                surface_dessin.create_line(
                    208, 8, 295, 95, fill="blue", width=10)
                surface_dessin.create_line(
                    295, 8, 208, 95, fill="blue", width=10)
                player2 += 1
                player1 += 1
                case3 = True
        else:
            if case3 == True:
                tk.messagebox.showinfo(
                    title="Impossible", message="Les croix ont déjà jouer")
            else:
                surface_dessin.create_circle(
                    250, 50, 43,  outline="red", width=4)
                player2 += 1
                player1 += 1
                case3b = True
    elif X < 100 and Y < 200:
        clic4 = True
        if player1 % 2 == 0:
            if case4b == True:
                tk.messagebox.showinfo(
                    title="Impossible", message="Les ronds ont déjà jouer")
            else:
                surface_dessin.create_line(
                    8, 108, 95, 195, fill="blue", width=10)
                surface_dessin.create_line(
                    95, 108, 8, 195, fill="blue", width=10)
                player2 += 1
                player1 += 1
                case4 = True
        else:
            if case4 == True:
                tk.messagebox.showinfo(
                    title="Impossible", message="Les ronds ont déjà jouer")
            else:
                surface_dessin.create_circle(
                    50, 150, 43,  outline="red", width=4)
                player2 += 1
                player1 += 1
                case4b = True
    elif X < 200 and Y < 200:
        clic5 = True
        if player1 % 2 == 0:
            if case5b == True:
                tk.messagebox.showinfo(
                    title="Impossible", message="Les ronds ont déjà jouer")
            else:
                surface_dessin.create_line(
                    108, 108, 195, 195, fill="blue", width=10)
                surface_dessin.create_line(
                    195, 108, 108, 195, fill="blue", width=10)
                player2 += 1
                player1 += 1
                case5 = True
        else:
            if case5 == True:
                tk.messagebox.showinfo(
                    title="Impossible", message="Les croix ont déjà jouer")
            else:
                surface_dessin.create_circle(
                    150, 150, 43,  outline="red", width=4)
                player2 += 1
                player1 += 1
                case5b = True
    elif X < 300 and Y < 200:
        clic6 = True
        if player1 % 2 == 0:
            if case6b == True:
                tk.messagebox.showinfo(
                    title="Impossible", message="Les ronds ont déjà jouer")
            else:
                surface_dessin.create_line(
                    208, 108, 295, 195, fill="blue", width=10)
                surface_dessin.create_line(
                    295, 108, 208, 195, fill="blue", width=10)
                player2 += 1
                player1 += 1
                case6 = True
        else:
            if case6 == True:
                tk.messagebox.showinfo(
                    title="Impossible", message="Les croix ont déjà jouer")
            else:
                surface_dessin.create_circle(
                    250, 150, 43,  outline="red", width=4)
                player2 += 1
                player1 += 1
                case6b = True
    elif X < 100 and Y < 300:
        clic7 = True
        if player1 % 2 == 0:
            if case7b == True:
                tk.messagebox.showinfo(
                    title="Impossible", message="Les ronds ont déjà jouer")
            else:
                surface_dessin.create_line(
                    8, 208, 95, 295, fill="blue", width=10)
                surface_dessin.create_line(
                    95, 208, 8, 295, fill="blue", width=10)
                player2 += 1
                player1 += 1
                case7 = True
        else:
            if case7 == True:
                tk.messagebox.showinfo(
                    title="Impossible", message="Les croix ont déjà jouer")
            else:
                surface_dessin.create_circle(
                    50, 250, 43,  outline="red", width=4)
                player2 += 1
                player1 += 1
                case7b = True
    elif X < 200 and Y < 300:
        clic8 = True
        if player1 % 2 == 0:
            if case8b == True:
                tk.messagebox.showinfo(
                    title="Impossible", message="Les ronds ont déjà jouer")
            else:
                surface_dessin.create_line(
                    108, 208, 195, 295, fill="blue", width=10)
                surface_dessin.create_line(
                    195, 208, 108, 295, fill="blue", width=10)
                player2 += 1
                player1 += 1
                case8 = True
        else:
            if case8 == True:
                tk.messagebox.showinfo(
                    title="Impossible", message="Les croix ont déjà jouer")
            else:
                surface_dessin.create_circle(
                    150, 250, 43,  outline="red", width=4)
                player2 += 1
                player1 += 1
                case8b = True
    elif X < 300 and Y < 300:
        clic9 = True
        if player1 % 2 == 0:
            if case9b == True:
                tk.messagebox.showinfo(
                    title="Impossible", message="Les ronds ont déjà jouer")
            else:
                surface_dessin.create_line(
                    208, 208, 295, 295, fill="blue", width=10)
                surface_dessin.create_line(
                    295, 208, 208, 295, fill="blue", width=10)
                player2 += 1
                player1 += 1
                case9 = True
        else:
            if case9 == True:
                tk.messagebox.showinfo(
                    title="Impossible", message="Les croix ont déjà jouer")
            else:
                surface_dessin.create_circle(
                    250, 250, 43,  outline="red", width=4)
                player2 += 1
                player1 += 1
                case9b = True

    global compteur, compteur2
    if case1 == True and case2 == True and case3 == True:
        surface_dessin.create_line(0, 50, 300, 50, fill="blue", width=10)
        tk.messagebox.showinfo(title="Bravo", message="Les croix ont gagner")
        surface_dessin.delete(tk.ALL)
        compteur += 1
        text.set("Compteur croix = " + str(compteur))
    elif case4 == True and case5 == True and case6 == True:
        surface_dessin.create_line(0, 150, 300, 150, fill="blue", width=10)
        tk.messagebox.showinfo(title="Bravo", message="Les croix ont gagner")
        surface_dessin.delete(tk.ALL)
        compteur += 1
        text.set("Compteur croix = " + str(compteur))
    elif case7 == True and case8 == True and case9 == True:
        surface_dessin.create_line(0, 250, 300, 250, fill="blue", width=10)
        tk.messagebox.showinfo(title="Bravo", message="Les croix ont gagner")
        surface_dessin.delete(tk.ALL)
        compteur += 1
        text.set("Compteur croix = " + str(compteur))
    elif case1 == True and case4 == True and case7 == True:
        surface_dessin.create_line(50, 0, 50, 300, fill="blue", width=10)
        tk.messagebox.showinfo(title="Bravo", message="Les croix ont gagner")
        surface_dessin.delete(tk.ALL)
        compteur += 1
        text.set("Compteur croix = " + str(compteur))
    elif case2 == True and case5 == True and case8 == True:
        surface_dessin.create_line(150, 0, 150, 300, fill="blue", width=10)
        tk.messagebox.showinfo(title="Bravo", message="Les croix ont gagner")
        surface_dessin.delete(tk.ALL)
        compteur += 1
        text.set("Compteur croix = " + str(compteur))
    elif case3 == True and case6 == True and case9 == True:
        surface_dessin.create_line(250, 0, 250, 300, fill="blue", width=10)
        tk.messagebox.showinfo(title="Bravo", message="Les croix ont gagner")
        surface_dessin.delete(tk.ALL)
        compteur += 1
        text.set("Compteur croix = " + str(compteur))
    elif case1 == True and case5 == True and case9 == True:
        surface_dessin.create_line(0, 0, 300, 300, fill="blue", width=10)
        tk.messagebox.showinfo(title="Bravo", message="Les croix ont gagner")
        surface_dessin.delete(tk.ALL)
        compteur += 1
        text.set("Compteur croix = " + str(compteur))
    elif case3 == True and case5 == True and case7 == True:
        surface_dessin.create_line(300, 0, 0, 300, fill="blue", width=10)
        tk.messagebox.showinfo(title="Bravo", message="Les croix ont gagner")
        surface_dessin.delete(tk.ALL)
        compteur += 1
        text.set("Compteur croix = " + str(compteur))
    elif case1b == True and case2b == True and case3b == True:
        surface_dessin.create_line(0, 50, 300, 50, fill="red", width=10)
        tk.messagebox.showinfo(title="Bravo", message="Les ronds ont gagner")
        surface_dessin.delete(tk.ALL)
        compteur2 += 1
        text2.set("Compteur rond = " + str(compteur2))
    elif case4b == True and case5b == True and case6b == True:
        surface_dessin.create_line(0, 150, 300, 150, fill="red", width=10)
        tk.messagebox.showinfo(title="Bravo", message="Les ronds ont gagnier")
        surface_dessin.delete(tk.ALL)
        compteur2 += 1
        text2.set("Compteur rond = " + str(compteur2))
    elif case7b == True and case8b == True and case9b == True:
        surface_dessin.create_line(0, 250, 300, 250, fill="red", width=10)
        tk.messagebox.showinfo(title="Bravo", message="Les ronds ont gagnier")
        surface_dessin.delete(tk.ALL)
        compteur2 += 1
        text2.set("Compteur rond = " + str(compteur2))
    elif case1b == True and case4b == True and case7b == True:
        surface_dessin.create_line(50, 0, 50, 300, fill="red", width=10)
        tk.messagebox.showinfo(title="Bravo", message="Les ronds ont gagnier")
        surface_dessin.delete(tk.ALL)
        compteur2 += 1
        text2.set("Compteur rond = " + str(compteur2))
    elif case2b == True and case5b == True and case8b == True:
        surface_dessin.create_line(150, 0, 150, 300, fill="red", width=10)
        tk.messagebox.showinfo(title="Bravo", message="Les ronds ont gagnier")
        surface_dessin.delete(tk.ALL)
        compteur2 += 1
        text2.set("Compteur rond = " + str(compteur2))
    elif case3b == True and case6b == True and case9b == True:
        surface_dessin.create_line(250, 0, 250, 300, fill="red", width=10)
        tk.messagebox.showinfo(title="Bravo", message="Les ronds ont gagnier")
        surface_dessin.delete(tk.ALL)
        compteur2 += 1
        text2.set("Compteur rond = " + str(compteur2))
    elif case1b == True and case5b == True and case9b == True:
        surface_dessin.create_line(0, 0, 300, 300, fill="red", width=10)
        tk.messagebox.showinfo(title="Bravo", message="Les ronds ont gagnier")
        surface_dessin.delete(tk.ALL)
        compteur2 += 1
        text2.set("Compteur rond = " + str(compteur2))
    elif case3b == True and case5b == True and case7b == True:
        surface_dessin.create_line(300, 0, 0, 300, fill="red", width=10)
        tk.messagebox.showinfo(title="Bravo", message="Les ronds ont gagnier")
        surface_dessin.delete(tk.ALL)
        compteur2 += 1
        text2.set("Compteur rond = " + str(compteur2))
    elif clic1 == True and clic2 == True and clic3 == True and clic4 == True and clic5 == True and clic6 == True and clic7 == True and clic8 == True and clic9 == True:
        tk.messagebox.showinfo(
            title="égalité", message="Vous avez fait égalité")
        surface_dessin.delete(tk.ALL)


## -------Commande pour quitter-------##


def ExitApp():
    MsgBox = tk.messagebox.askquestion(
        'Quitter', 'Voulez vous vraiment quitter ?', icon='error')
    if MsgBox == 'yes':
        mon_app.destroy()
    else:
        tk.messagebox.showinfo('Welcome back', 'Welcome back')


# Création de la fenêtre principale (main window)
mon_app = tk.Tk()
mon_app.title('Morpion')

# Création d'un widget Canvas (zone graphique)
surface_dessin = tk.Canvas(mon_app, width=LARGEUR, height=HAUTEUR, bg='white')
surface_dessin.pack(padx=5, pady=5)


# La méthode bind() permet de lier un événement avec une fonction :
# un clic gauche sur la surface provoquera l'appel de la fonction clic()
surface_dessin.bind('<Button-1>', clic)
surface_dessin.pack(padx=5, pady=5)


global text
text = tk.StringVar()
text.set("Compteur croix = 0")
label = tk.Label(mon_app, textvariable=text)
label.pack(side="right")

global text2
text2 = tk.StringVar()
text2.set("Compteur rond = 0")
label2 = tk.Label(mon_app, textvariable=text2)
label2.pack(side="right")

## -------Création de cercle-------##


def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)


tk.Canvas.create_circle = _create_circle


def _create_circle_arc(self, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)


tk.Canvas.create_circle_arc = _create_circle_arc


# Création d'un widget Button (bouton effacer)
tk.Button(mon_app, text='Jouer / Rejouer', command=Jouer_Rejouer).pack(
    side=tk.LEFT, padx=10, pady=10)
# Création d'un widget Button (bouton Quitter)
buttonEg = tk.Button(mon_app, text='Quitter', command=ExitApp).pack(
    side=tk.RIGHT, padx=10, pady=10)

# Scanne toute la page
mon_app.mainloop()
