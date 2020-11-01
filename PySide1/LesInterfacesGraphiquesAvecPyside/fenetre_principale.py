from PySide2 import QtWidgets
"""
PySide documentation: http://pyside.github.io/docs/pyside/
"""

####################
# QUELQUES WIDGETS #
####################

## CREATION D'UNE FENETRE VIDE
# class FenetrePrincipale(QtWidgets.QWidget):
#     def __init__(self):
#         super(FenetrePrincipale, self).__init__()
#
#         self.setWindowTitle("Ma Premiere Applicaiton")
#
# app = QtWidgets.QApplication([])
# fenetre = FenetrePrincipale()
# fenetre.show()
# app.exec_()

## QLABEL
# app = QtWidgets.QApplication([])
# label = QtWidgets.QLabel('Bonjour tout le monde')
# print(label.text())
# label.setText('Au revoir tout le monde')
# print(label.text())
# label.show()
# app.exec_()

## QPUSHBUTTON
# app = QtWidgets.QApplication([])
# bouton = QtWidgets.QPushButton('Clique sur le bouton')
#
# # modification du texte sur le bouton
# bouton.setText('Cliquez sur le bouton')
#
# # Recuperation du texte du bouton que l'on affiche dans la console
# print(bouton.text())
#
# bouton.show()
# app.exec_()

## QLINEDIT
# app = QtWidgets.QApplication([])
# lineEdit = QtWidgets.QLineEdit()
#
# # Affichage d'un texte gris pale qui va disparaitre quand on va cliquer dans la boite
# lineEdit.setPlaceholderText('Entrez votre nom')
# lineEdit.show()
# lineEdit.clearFocus()  # Si on on clear pas le focus on ne voie pas Entrez votre nom
# lineEdit.setText('Julien')
# print(lineEdit.text())  # Imprime dans la console ce qui est ecrie dans le linedit
# app.exec_()

###############
# LES LAYOUTS #
###############
