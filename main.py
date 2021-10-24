from tkinter import *
from tkinter import ttk

import grille

root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.resizable(False, False)

taille = 10

root.geometry((f"{50*taille}x"*2)[:-1])

couleurs = grille.generation_couleurs(taille)

canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

canvas.bind("<Button-1>", lambda info_clic: grille.attention_aux_couleurs(couleurs, canvas, info_clic))

grille.generation_grille(couleurs, canvas)

root.mainloop()
