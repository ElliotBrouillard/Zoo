# Elliot Brouillard
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.Dialog_enclos
from PyQt5 import QtWidgets

import Classes.Classe_Enclos

#####################################################
######## Définitions des fonctions ##################
#####################################################

def verifier_enclos_liste(p_num_enclos):
    """
        Vérifie si l'enclos existe dans la liste des enclos
    :param p_num_enclos: le numéro d'enclos
    :return: True si l'enclos est trouvé dans la liste des enclos et False sinon
    """
    for elt in Classes.Classe_Enclos.Enclos.ls_enclos:
        if elt._numero_enclos == p_num_enclos.capitalize():
            return True
    return False

def cacher_labels_erreur(objet):
    """
    Cacher les différents labels d'erreur
    """
    objet.label_erreur_numero_enclos_existe.setVisible(False)
    objet.label_erreur_numero_enclos_existe_pas.setVisible(False)
    objet.label_erreur_validation_numero_enclos.setVisible(False)
    objet.label_erreur_nom_enclos.setVisible(False)

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetreenclos(QtWidgets.QDialog, UI_PY.Dialog_enclos.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetreenclos, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Enclos")

    # Gestionnaire d'événement du bouton ajouter_enclos
    @pyqtSlot()
    def on_pushButton_ajouter_enclos_clicked(self):
        """
        Gestionnaire d'événement du bouton Ajouter enclos
        """
        # Cacher les labels d'erreur
        cacher_labels_erreur(self)
        # Instancier un objet enclos
        enclos = Classes.Classe_Enclos.Enclos()
        #Entrée de donnée pour les attributs de l'objet Enclos
        enclos.Numero_enclos = self.lineEdit_numero_enclos.text()
        enclos.Nom_enclos = self.lineEdit_nom_enclos.text().capitalize()
        enclos.Localisation = self.comboBox_localisation.currentText()
        enclos.Taille = self.comboBox_taille_enclos.currentText()
        enclos.Type = self.comboBox_type_enclos.currentText()
        # Booléen qui nous permet de savoir si le numéro d'enclos exist ou pas dans la liste des enclos
        verifier_enclos = verifier_enclos_liste(enclos._numero_enclos)
        # Si le numéro d'enclos est valide mais existe déjà dans la liste des enclos
        if verifier_enclos is True:
            # Effacer le lineEdit du numéro d'enclos et afficher le message d'errreur
            self.lineEdit_numero_enclos.clear()
            self.label_erreur_numero_enclos_existe.setVisible(False)
            #self.label_erreur_
        # si le nom d'enclos est invalide afficher le message d'erreur
        if enclos._nom_enclos == "":
            self.lineEdit_nom_enclos.clear()
            self.label_erreur_nom_enclos.setVisible(True)
        # si le numéro d'enclos est invalide, effacer le lineEdit et afficher le message d'erreur
        if enclos._numero_enclos == "":
            self.lineEdit_numero_enclos.clear()
            self.label_erreur_numero_enclos_existe_pas.setVisible(True)
        if enclos._nom_enclos != "" and enclos._numero_enclos != "" and verifier_enclos is False:
            # Ajouter l'objet instancié à la liste des enclos
            Classes.Classe_Enclos.Enclos.ls_enclos.append(enclos)

    # Gestionnaire du bouton supprimer enclos
    @pyqtSlot()
    def on_pushButton_supprimer_enclos_clicked(self):
        """
        Gestionnaire d'vénement
        """
        # Cacher les labels d'erreur
        cacher_labels_erreur(self)
        # Instancier un objet Enclos
        enclos=Classes.Classe_Enclos.Enclos
        # Entrée de donnée pours les attributs de l'objet Enclos
        enclos._nom_enclos = self.lineEdit_nom_enclos.text().capitalize()
        enclos._numero_enclos = self.lineEdit_numero_enclos.text()
        # Boolen qui nous permet si le numéro d'enclos existe ou pas dans la liste d'enclos
        verifier_enclos = verifier_enclos_liste(enclos._numero_enclos)
        # Si le nom, le numéro sont valides et l'enclos existe dans la liste des étudiants
        if enclos._nom_enclos != "" and enclos._numero_enclos != "" and verifier_enclos is True:
            trouve = False
            for elt in Classes.Classe_Enclos.Enclos.ls_enclos:
                # Chercher dans la liste des enclos un enclos ayant les informations entrées
                if elt._numero_enclos == self.lineEdit_numero_enclos.text() and elt._nom_enclos == self.lineEdit_nom_enclos.text().capitalize():
                    # Supprimer l'enclos de la liste des enclos
                    trouve = True
                    Classes.Classe_Enclos.Enclos.ls_enclos.remove(elt)
                    break
            # Si l'enclos n'existe pas dans la liste affficher un message d'erreur dans le label_erreur_enclos_existe_pas
            if not trouve:
                self.label_erreur_numero_enclos_existe_pas.setVisible(True)
            else:
                # Réafficher la liste
                Classes.Classe_Enclos.Enclos.ls_enclos.clear()
                for elt in Classes.Classe_Enclos.Enclos.ls_enclos:
                    Classes.Classe_Enclos.Enclos.ls_enclos.append(elt.__str__())
                # Réinitialiser les lineEdit et le dateEdit
                self.lineEdit_numero_enclos.clear()
                self.lineEdit_nom_enclos.clear()
        if verifier_enclos is False and enclos._numero_enclos != "":
            # Effacer le lineEdit du numéro d'enclos et afficher le message d'erreur
            self.lineEdit_numero_enclos.clear()
            self.label_erreur_numero_enclos_existe_pas.setVisible(True)
            # si le nom est invalide, affcher un message d'erreur
            if enclos._numero_enclos == "":
                self.lineEdit_numero_enclos.clear()
                self.label_erreur_validation_numero_enclos.setVisible(True)
            # si lle nom est invalide, afficher un message d'erreur
            if enclos._nom_enclos == "":
                self.lineEdit_nom_enclos.clear()
                self.label_erreur_nom_enclos.setVisible(True)
            # Si le numéro d'enclos est invalide, effacer le lineEdit du numéro étudiant et afficher un message d'erreur
            self.lineEdit_numero_enclos.clear()
            self.label_erreur_validation_numero_enclos.setVisible(True)


