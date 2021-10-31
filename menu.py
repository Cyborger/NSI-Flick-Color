from tkinter import *
from tkinter import ttk

import grille

def afficher_menu(root):
    """
    Affichage des éléments du menu.

    Génération d'une Frame principale contenant tous les éléments du menu.

    Paramètres
    ----------
    root : tkinter.Tk
        Classe Tkinter qui contiendra la Frame principale du menu.
    """
    root.geometry("400x500")

    frame = ttk.Frame(root, padding=(10, 10, 12, 12))
    frame.grid(column=0, row=0, sticky=(N, S, E, W))

    title = ttk.Label(frame, image=root.images["titre"])
    title.grid(column=0, row=0, sticky=(N, E, W,))

    cinq_par_cinq = ttk.Button(frame, text="Grille 5x5")
    cinq_par_cinq.grid(column=0, row=1, sticky=(N,))
    
    cinq_par_cinq.bind("<Button-1>", lambda _: clic_menu(root, frame, 5))

    dix_par_dix = ttk.Button(frame, text="Grille 10x10")
    dix_par_dix.grid(column=0, row=2, sticky=(N,))

    dix_par_dix.bind("<Button-1>", lambda _: clic_menu(root, frame, 10))
    
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)

def clic_menu(root, menu, taille):
    """
    Action executée au clic sur l'un des boutons de jeu du menu.

    Supprimme les éléments du menu et génère la grille de couleurs afin de l'afficher.

    Parameters
    ----------
    root : tkinter.Tk
        Classe Tkinter qui contiendra la grille de couleurs à afficher.
    menu : tkinter.Frame
        Frame qui contient les éléments du menu à supprimmer.
    taille : int
        Taille de la grille à générer.
    """
    menu.destroy()

    root.geometry((f"{50*taille}x"*2)[:-1])

    couleurs = grille.generation_couleurs(taille)

    canvas = Canvas(root)
    canvas.grid(column=0, row=0, sticky=(N, W, E, S))

    canvas.bind("<Button-1>", lambda info_clic: grille.attention_pour_les_couleurs(couleurs, canvas, info_clic))

    grille.afficher_rectangles(couleurs, canvas)


