# Elliot Brouillard
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import Classes.Classe_Enclos
import UI_PY.Dialog_animal
from PyQt5 import QtWidgets
#import Dialog.dialog_enclos


######################################################
###### Défintions des fonctions ######################
def cacher_labels_erreur(objet):
    objet.label_erreur_poids_animal.setVisible(False)
    objet.label_erreur_numero_animal_existe_pas.setVisible(False)
    objet.label_erreur_numero_animal_existe.setVisible(False)
    objet.label_erreur_numero_animal_invalide.setVisible(False)
    objet.label_erreur_longueur_bec.setVisible(False)
######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetreanimal(QtWidgets.QDialog, UI_PY.Dialog_animal.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetreanimal, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue animal")


    # # Entrée de donnée
    #     self.comboBox_enclos_animal.addItems("E1", "E2")
    #     self.comboBox_enclos_animal.setItemText(0, "E1")
    #     self.comboBox_enclos_animal.setItemText(1, "E2")
    #     self.comboBox_enclos_animal.setItemText(2, "E3")
    #     self.comboBox_enclos_animal.addItem()
    #     self.comboBox_enclos_animal.addItems(Classes.Classe_Enclos.Enclos.ls_enclos)
    #
    #
    #     # Question 3 de boite de dialogue animal
    #     self.comboBox_surnom.setItemtext(0, "Minou")
    #     self.lineEdit_surnom_animal.setText("Minou")

    @pyqtSlot()
    def on_pushbutton
