from random import choice

def generation_couleurs(taille):
    """Génère une grille de couleurs aléatoire selon une taille donnée.

    Paramètre :
        - taille (int): Définie la taille de la liste et des sous-listes renvoyées.
    
    Retourne :
        list: Liste de sous-listes contenant les valeurs aléatoires sélectionnées parmis la liste de couleurs par défaut.
    """
    defauts = ["red", "blue", "yellow", "green", "purple", "white"]
    return [[choice(defauts) for _ in range(taille)] for _ in range(taille)]

def colorier(grille, i , j, couleur_initiale, couleur_finale):
    """À l'aide d'une grille de couleur donnée, effectue la propagation d'une couleur initiale vers une nouvelle couleur au point (i, j).
    """
    if not(0 <= i < len(grille) and 0 <= j < len(grille)) or grille[j][i] != couleur_initiale or couleur_initiale == couleur_finale:
        return

    grille[j][i] = couleur_finale

    colorier(grille, i + 1, j, couleur_initiale, couleur_finale)
    colorier(grille, i, j + 1, couleur_initiale, couleur_finale)
    colorier(grille, i - 1, j, couleur_initiale, couleur_finale)
    colorier(grille, i, j - 1, couleur_initiale, couleur_finale)

def generation_grille(couleurs, canvas):
    x = 0
    y = 0

    for ligne in couleurs:
        for colonne in ligne:
            canvas.create_rectangle(x, y, x + 50, y + 50, fill=colonne, outline="black")
            x += 50
        y += 50
        x = 0

def attention_aux_couleurs(couleurs, canvas, info_clic):
    colorier(couleurs, 0, 0, couleurs[0][0], couleurs[info_clic.y // 50][info_clic.x // 50])
    canvas.delete("all")
    generation_grille(couleurs, canvas)