from tkinter import Canvas, ttk
import grille


def afficher(root, taille):
    """
    Affiche le jeu.

    Génère tous les éléments requis à l'affichage de la grille.

    Parameters
    ----------
    root : tkinter.Tk
        Classe Tkinter qui contiendra la grille de couleurs à afficher.
    taille : int
        Taille de la grille à générer.
    """
    root.geometry(f"{50 * taille + 20}x{50 * taille + 25}")  # L'ajout de 25 permet l'affichage du nombre de coups restant

    couleurs = grille.generation_couleurs(taille)  # Permet de générer la grille

    jeu = ttk.Frame(root, padding=(10, 10, 12, 0))
    jeu.pack()

    # Création du canvas avec mise en valeur du contour
    canvas = Canvas(jeu, width=50 * taille, height=49 * taille, highlightthickness=1, highlightbackground="black")
    canvas.pack()

    coups_restants = {
        "utilises": 0,
        "total": round(taille * 2.5),
        "label": ttk.Label(jeu)
    }

    coups_restants["label"]["text"] = f"Coups restants : {coups_restants['total']}"
    coups_restants["label"].pack()

    canvas.bind("<Button-1>", lambda info_clic: grille.clic(root, jeu, canvas, couleurs, coups_restants, info_clic))

    grille.generation_rectangles(couleurs, canvas)
