# Elliot Brouillard
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.Dialog_veterinaire
from PyQt5 import QtWidgets


#     objet.label_erreur_numero_employe__existe.setVisible(False)
#     objet.label_erreur_numero_employe_invalide.setVisible(False)
#     objet.label_erreur_numero_employe_existe_pas.setVisible(False)
#     objet.label_erreur_nom_employe.setVisible(False)
#     objet.label_erreur_prenom_employe.setVisible(False)
#     objet.label_erreur_date_naiss.setVisible(False)


######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetreveterinaire(QtWidgets.QDialog, UI_PY.Dialog_veterinaire.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetreveterinaire, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Vétérinaire")

    # Définitions des fonctions
    def serialiser(self):
        pass

    def on_pushButton
