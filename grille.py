from random import choice

def generation_couleurs(taille):
    """
    Génération aléatoire de la grille de couleurs.

    Paramètres
    ----------
    taille : int
        Taille de la grille.

    Renvois
    -------
    list
        Grille de couleurs.
    """ 
    defauts = ["red", "blue", "yellow", "green", "purple", "white"]
    return [[choice(defauts) for _ in range(taille)] for _ in range(taille)]

def colorier(grille, i , j, couleur_initiale, couleur_finale):
    """
    Propagation des couleurs sur la grille.

    Propage la couleur finale au point i, j et à toutes les cases adjacentes (côte à côte horizontalement ou verticalement) de même couleur initiale.

    Paramètres
    ----------
    grille : list
        Grille de couleurs à modifier.
    i : int
        Position en abscisse du point à partir duquel propager la couleur.
    j : int
        Position en ordonnée du point à partir duquel propager la couleur.
    couleur_initiale : str
        Couleur initiale du point i, j.
    couleur_finale : str
        Couleur à propager.
    """
    if not(0 <= i < len(grille) and 0 <= j < len(grille)) or grille[j][i] != couleur_initiale or couleur_initiale == couleur_finale:
        return

    grille[j][i] = couleur_finale

    colorier(grille, i + 1, j, couleur_initiale, couleur_finale)
    colorier(grille, i, j + 1, couleur_initiale, couleur_finale)
    colorier(grille, i - 1, j, couleur_initiale, couleur_finale)
    colorier(grille, i, j - 1, couleur_initiale, couleur_finale)

def afficher_rectangles(couleurs, canvas):
    """
    Construit la partie graphique de la grille.

    À partir de la grille de couleurs, création des rectangles affichés par l'intermédiaire du canvas donné.

    Paramètres
    ----------
    couleurs : list
        Grille de couleurs.
    canvas : tkinter.Canvas
        Canvas Tkinter à utiliser pour la création des rectangles.
    """
    x = 0
    y = 0

    for ligne in couleurs:
        for colonne in ligne:
            canvas.create_rectangle(x, y, x + 50, y + 50, fill=colonne, outline="black")
            x += 50
        y += 50
        x = 0

def attention_pour_les_couleurs(couleurs, canvas, info_clic):
    """
    Action executée au clic sur la grille graphique.

    Propage la couleur cliquée à partir du point 0, 0 selon les conditions énumérées dans la fonction colorier. Met à jour la partie graphique de la grille.

    Paramètres
    ----------
    couleurs : list
        Grille de couleurs à modifier.
    canvas : tkinter.Canvas
        Canvas Tkinter à modifier.
    info_clic : tkinter.Event
        Évènement Tkinter contenant les informations sur le clic.
    """ 
    colorier(couleurs, 0, 0, couleurs[0][0], couleurs[info_clic.y // 50][info_clic.x // 50])
    canvas.delete("all")  # Supprime tous les rectangles du Canvas pour libérer la mémoire
    afficher_rectangles(couleurs, canvas)
