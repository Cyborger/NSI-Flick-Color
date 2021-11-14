from random import choice
import fin


def colorier(grille, i, j, couleur_initiale, couleur_finale):
    """
    Propagation des couleurs sur la grille.

    Propage la couleur finale au point i, j et à toutes les cases adjacentes (côte à côte horizontalement ou
    verticalement) de même couleur initiale.

    Paramètres
    ----------
    grille : list
        Grille de couleurs à modifier.
    i : int
        Position en abscisse du point à partir duquel propager la couleur.
    j : int
        Position en ordonnée du point à partir duquel propager la couleur.
    couleur_initiale : str
        Couleur initiale du point (i, j).
    couleur_finale : str
        Couleur à propager.
    """
    # Vérifie si l'élément de position (i, j) est compris dans les bords de la grille et qu'il est de même couleur
    # que la couleur initiale
    if not (0 <= i < len(grille) and 0 <= j < len(grille)) or grille[j][i] != couleur_initiale:
        return

    grille[j][i] = couleur_finale

    colorier(grille, i + 1, j, couleur_initiale, couleur_finale)
    colorier(grille, i, j + 1, couleur_initiale, couleur_finale)
    colorier(grille, i - 1, j, couleur_initiale, couleur_finale)
    colorier(grille, i, j - 1, couleur_initiale, couleur_finale)


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


def generation_rectangles(couleurs, canvas):
    """
    Construit la partie graphique de la grille.

    À partir de la grille de couleurs, création des rectangles affichés par l'intermédiaire d'un canvas donné.

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
            canvas.create_rectangle(x, y, x + 50, y + 50, fill=colonne)  # Option de remplissage correspondant à la couleur
            x += 50
        y += 50
        x = 0


def elements_identiques(grille):
    """
    Indique si les éléments d'une grille sont tous identiques.

    Rassemble tous les éléments de la grille dans une liste qui ne tolère pas les dupliqués et vérifie si son nombre
    d'élément dépasse 1.

    Paramètres
    ----------
    grille : list
        Grille à vérifier.

    Renvois
    -------
    bool
        Vrai si les éléments sont tous identiques, faux dans le cas contraire.
    """
    elements_uniques = []

    for ligne in grille:
        for colonne in ligne:
            if colonne not in elements_uniques:
                elements_uniques.append(colonne)

    if len(elements_uniques) > 1:
        return False
    return True


def clic(root, jeu, canvas, couleurs, coups_restants, info_clic):
    """
    Action executée au clic de la grille graphique.

    Propage la couleur cliquée à partir du point 0, 0 selon les conditions énumérées dans la fonction colorier. Met à
    jour la partie graphique de la grille.

    Paramètres
    ----------
    root : tkinter.Tk
        Fenêtre principale du jeu.
    jeu : tkinter.Frame
        Frame qui contient les éléments du jeu.
    canvas : tkinter.Canvas
        Canvas Tkinter à modifier.
    couleurs : list
        Grille de couleurs à modifier.
    coups_restants : dict
        Dictionnaire contenant le nombre total et le nombre de coups utilisés ainsi que le label à afficher au joueur.
    info_clic : tkinter.Event
        Évènement Tkinter contenant les informations sur le clic.
    """
    # Permet d'éviter de propager et compter plusieurs fois la même couleur
    if couleurs[info_clic.y // 50][info_clic.x // 50] == couleurs[0][0]:
        return

    # Mise à jour de la partie fonctionnelle de la grille
    colorier(couleurs, 0, 0, couleurs[0][0], couleurs[info_clic.y // 50][info_clic.x // 50])
    coups_restants["utilises"] += 1

    # Arrêts du jeu
    if elements_identiques(couleurs):  # Si toutes les couleurs sont identiques et que le joueur remporte la partie
        fin.afficher(root, jeu, coups_restants["utilises"], len(couleurs), True)
        return
    elif not coups_restants["total"] - coups_restants[
        "utilises"]:  # Si le nombre de coup restant est épuisé et que le joueur perd la partie
        fin.afficher(root, jeu, coups_restants["utilises"], len(couleurs), False)
        return

    # Mise à jour du compteur de coups
    coups_restants["label"]["text"] = f"Coups restants : {coups_restants['total'] - coups_restants['utilises']}"

    # Mise à jour de la partie graphique de la grille
    canvas.delete("all")  # Supprime tous les rectangles du Canvas pour libérer la mémoire
    generation_rectangles(couleurs, canvas)
