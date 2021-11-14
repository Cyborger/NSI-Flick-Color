from tkinter import ttk
import jeu


def afficher(root):
    """
    Affichage des éléments du menu.

    Génération d'une Frame principale contenant tous les éléments du menu.

    Paramètres
    ----------
    root : tkinter.Tk
        Classe Tkinter qui contiendra la Frame principale du menu.
    """
    root.geometry("400x500")

    menu = ttk.Frame(root, padding=(10, 10, 12, 12))
    menu.pack()

    ttk.Label(menu, image=root.images["titre"]).pack()

    ttk.Button(menu, text="Grille 5x5", command=lambda: clic(root, menu, 5)).pack()
    ttk.Button(menu, text="Grille 10x10", command=lambda: clic(root, menu, 10)).pack()
    ttk.Button(menu, text="Quitter", command=root.destroy).pack()


def clic(root, menu, taille):
    """
    Action executée au clic sur l'un des boutons de jeu du menu.

    Supprimme les éléments du menu et affiche le jeu.

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
    jeu.afficher(root, taille)
