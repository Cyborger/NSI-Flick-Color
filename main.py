from tkinter import Tk, PhotoImage
from tkinter.ttk import Style
import menu

root = Tk()
root.resizable(False, False)  # Pour empêcher à l'utilisateur de redéfinir la taille de la fenêtre

# Préchargement les images pour en éviter leur suppression par le collecteur de déchets Python
root.images = {
    "titre": PhotoImage(file="./titre.png")
}

# Changement du thème Tkinter par défaut vers le thème Breeze inspiré par le thème prévu pour l'environnement de bureau
# KDE. Bibliothèque tcl fourni par MaxPerl sous la licence GNU LGPL v2.1 (https://github.com/MaxPerl/ttk-Breeze).
root.tk.call('lappend', 'auto_path', 'ttk-Breeze')
root.tk.call('package', 'require', 'ttk::theme::Breeze')
s = Style()
s.theme_use("Breeze")

menu.afficher(root)
root.mainloop()
