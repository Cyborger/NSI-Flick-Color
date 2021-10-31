from tkinter import Tk, PhotoImage
from tkinter.ttk import Style

import menu

root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.resizable(False, False)

# Préchargement les images pour en éviter leur suppression par le collecteur de déchets Python
root.images = {
    "titre": PhotoImage(file="./titre.png")
}

# Changement du thème Tkinter par défaut vers le thème Breeze inspiré par le thème prévu pour l'environnement de bureau KDE.
# Bibliothèque tcl fourni par MaxPerl sous la licence GNU LGPL v2.1 (https://github.com/MaxPerl/ttk-Breeze).
root.tk.call('lappend', 'auto_path', 'style')
root.tk.call('package', 'require', 'ttk::theme::Breeze')

s = Style()
s.theme_use("Breeze")

menu.afficher_menu(root)

root.mainloop()
