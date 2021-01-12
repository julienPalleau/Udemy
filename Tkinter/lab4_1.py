# X:\backup\IT stuff\Cours de programmation\Python\[Linkedin Learning] L'essentiel de Python 3\05 - Construire une interface graphique sous Tkinter

from tkinter import *
# Creation d'un container avec les onglets Ouvrir, Fermer et Reduire
fenetre = Tk()
fenetre.title("Titre de la fenetre")
fenetre.geometry("500x500")
fenetre.iconbitmap("Book.ico")

label = Label(fenetre, text="Vive la programmation sous Python 3")
label.pack()

# # Widget label
# # bg = background
# label = Label(fenetre, text="Un autre label", bg="red")
# label.pack()
#
# # Widget label
# label = Label(fenetre, text="Le bouton ci-dessous permet de fermer la fenetre.", background="yellow")
# label.pack()
#
# # Widget label couleur avec le code hexadecimal
# # Trouvez votre couleur sur http://www.code-couleur.com/
# label = Label(fenetre, text="Le bouton ci-dessous permet de fermer la fenetre.", background='#40E0D0')
# label.pack()
#
# TitreCadre = LabelFrame(fenetre, text="Le titre du cadre")
# TitreCadre.pack(fill="both", expand="yes")

# Widget Bouton
# Bouton est dans le container... commande associee quit
bouton1 = Button(fenetre, text="style de type FLAT", fg="red", relief=FLAT, command=fenetre.quit).pack()
bouton2 = Button(fenetre, text="style de type RAISED", fg="orange", relief=RAISED, command=fenetre.quit).pack()
bouton3 = Button(fenetre, text="style de type SUNKEN", bg="green", relief=SUNKEN, command=fenetre.quit).pack()
bouton4 = Button(fenetre, text="style de type GROOVE", relief=GROOVE, command=fenetre.quit).pack()
bouton5 = Button(fenetre, text="style de type RIDGE", relief=RIDGE, command=fenetre.quit).pack()

fenetre.mainloop()