from tkinter import ttk
import menu


def retour_menu(root, fin):
    """
    Permet le retour au menu.

    Supprime l'écran de fin.

    Paramètres
    ----------
    root : tkinter.Tk
        Fenêtre principale du jeu.
    fin : tkinter.Frame
        Frame qui contient les éléments de l'écran de fin.
    """
    fin.destroy()
    menu.afficher(root)


def afficher(root, jeu, coups_utilises, taille, victoire):
    """
    Affichage des éléments de l'écran de fin.

    Génération d'une frame principale qui contient les éléments du menu.

    Paramètres
    ----------
    root : tkinter.Tk
        Fenêtre principale du jeu.
    jeu : tkinter.Frame
        Frame qui contient les éléments du jeu.
    coups_utilises : int
        Nombre de coups utilisés dans le jeu.
    taille : int
        Taille de la grille à générer en cas d'appui sur le bouton recommencer.
    victoire : bool
        Vrai si le joueur a remporté la partie, faux dans le cas contraire.
    """
    jeu.destroy()

    root.geometry("400x500")

    fin = ttk.Frame(root, padding=(10, 10, 12, 12))
    fin.pack()

    ttk.Label(fin, image=root.images["titre"]).pack()

    if victoire:
        ttk.Label(fin, text="Vous avez remporté la partie !").pack()
        ttk.Label(fin, text="Nombre de coups utilisés : " + str(coups_utilises)).pack()
    else:
        ttk.Label(fin, text="Vous avez perdu la partie...").pack()

    ttk.Button(fin, text="Recommencer", command=lambda: menu.clic(root, fin, taille)).pack()
    ttk.Button(fin, text="Menu principal", command=lambda: retour_menu(root, fin)).pack()
    ttk.Button(fin, text="Quitter", command=root.destroy).pack()
