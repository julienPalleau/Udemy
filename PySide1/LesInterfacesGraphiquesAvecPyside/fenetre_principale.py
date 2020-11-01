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

## COORDONNEES ABSOLUES
# class MonApplication(QtWidgets.QWidget):
#     def __init__(self):
#         super(MonApplication, self).__init__()
#
#         btn_bonjour = QtWidgets.QPushButton('Bonjour', self)
#         btn_bonjour.move(10, 10)  # coordonnees en absolues (par rapport au point 0,0 situe en haut à gauche)
#
#         btn_auRevoir = QtWidgets.QPushButton('Au revoir', self)
#         btn_auRevoir.move(50, 50)  # coordonnees en absolues (par rapport au point 0,0 situe en haut à gauche)


## Le QGridLayout
class MonApplication(QtWidgets.QWidget):
    def __init__(self):
        super(MonApplication, self).__init__()

        layout = QtWidgets.QGridLayout(self)

        # # Exemple 1
        # btn_1 = QtWidgets.QPushButton('0.0')
        # btn_2 = QtWidgets.QPushButton('0.1')
        # btn_3 = QtWidgets.QPushButton('0.2')
        # btn_4 = QtWidgets.QPushButton('1.0')
        # btn_5 = QtWidgets.QPushButton('1.1')
        # btn_6 = QtWidgets.QPushButton('1.2')
        # btn_7 = QtWidgets.QPushButton('2.0')
        # btn_8 = QtWidgets.QPushButton('2.1')
        # btn_9 = QtWidgets.QPushButton('2.2')
        #
        # layout.addWidget(btn_1, 0, 0)
        # layout.addWidget(btn_2, 0, 1)
        # layout.addWidget(btn_3, 0, 2)
        # layout.addWidget(btn_4, 1, 0)
        # layout.addWidget(btn_5, 1, 1)
        # layout.addWidget(btn_6, 1, 2)
        # layout.addWidget(btn_7, 2, 0)
        # layout.addWidget(btn_8, 2, 1)
        # layout.addWidget(btn_9, 2, 2)

        # Exemple 2
        btn_1 = QtWidgets.QPushButton('0.0-1x3')
        btn_2 = QtWidgets.QPushButton('1.0-1x1')
        btn_3 = QtWidgets.QPushButton('1.1-1x1')
        btn_4 = QtWidgets.QPushButton('1.2-1x1')

        layout.addWidget(btn_1, 0, 0, 1, 3)
        layout.addWidget(btn_2, 1, 0, 1, 1)
        layout.addWidget(btn_3, 1, 1, 1, 1)
        layout.addWidget(btn_4, 1, 2, 1, 1)


## Le QHBoxLayout et le QVBoxLayout


        self.resize(500, 500)

app = QtWidgets.QApplication([])
fenetre = MonApplication()
fenetre.show()
app.exec_()