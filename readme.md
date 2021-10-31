# NSI - Projet n°1 (Terminale)

## Description du jeu

Faites s'étendre les couleurs, de manière à ce qu'il n'en reste plus qu'une seule à la fin du jeu. Le joueur doit remplir la grille d'une seule couleur en un minimum de coups.

- À chaque coup, le joueur clique sur la case de son choix pour sélectionner une couleur.
- À partir du coin supérieur gauche, la nouvelle couleur se propage aux cases adjacentes de même couleur.

## Contraintes

- Vous devez utiliser Tkinter pour l'interface graphique.
- Votre programme devra comporter :
	- un écran d'accueil pour démarrer le jeu
	- un écran de jeu
	- un écran de sortie à la fin du jeu
- Proposer deux niveaux de jeu :
	- niveau 1 : grille 5*5
	- niveau 2 : grille 10*10
- Nous considérerons qu'une grille de jeu est une liste de listes, et que chaque ligne de la grille de jeu est une liste de couleurs.
- Les cases de la grille de jeu peuvent prendre 6 couleurs différentes.
- Les grilles de jeu sont générées de manière aléatoire et sont différentes à chaque partie.
- L'écran de jeu doit posséder une zone d'affichage du nombre de coups joués. Cet affichage doit se mettre à jour chaque fois que le joueur choisit une nouvelle couleur.
- Vous devez utiliser une fonction récursive pour propager la couleur :

```python
def colorier(grille,i,j,couleur_initiale,couleur_finale):
	""" propage, si la case i,j est de couleur initiale,
	la couleur finale à la case i,j et à toutes les cases adjacentes
	de même couleur initiale.
	Deux cases adjacentes sont côte à côte soit horizontalement, soit verticalement.
	"""
```

Par exemple, `colorier(grille, 3, 1, "blue", "yellow")` donne,

- Votre code devra être structuré avec des fonctions de taille raisonnable.
- Vous adopterez une approche modulaire (programme principal appelant des sous-programmes ou modules), et vous devrez notamment séparer la partie graphique de la partie fonctionnelle.

- **Vous devrez rédiger un rapport qui devra préciser :**
	- votre démarche générale : les objectifs successifs que vous vous êtes fixés et les difficultés que vous avez rencontrées (il est conseillé de tenir un journal de bord)
	- l'arborescence de votre programme

## Critères pris en compte

- Résultat final
- Implication en classe durant les séances de projet
- Respect des consignes
- Organisation et propreté du code informatique
- Présence de commentaires dans le code (avec #)
- Spécifications des fonctions ("""...""")
- Rapport clair avec un contenu significatif

**Remarque :** Une question orale portant sur le code informatique pourra être posée à certains élèves à l'issue du projet.

## Délai

Remise du projet au format `zip` contenant le programme et le rapport au format `pdf` le 15 novembre 2021 sur Toutatice.
