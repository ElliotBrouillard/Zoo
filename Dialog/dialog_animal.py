# Elliot Brouillard
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import Classes.Classe_Enclos
import UI_PY.Dialog_animal
from PyQt5 import QtWidgets
#import Dialog.dialog_enclos
#import Classes.Classe_Animal
import Classes.Classe_Mammifere


######################################################
###### Défintions des fonctions ######################

def Verifier_numero_animal_existe(p_numero_a):
    """
    Vérifier si le numéro de local existe déjà
    """
    for elt in Mammifere.ls_animaux:
        if elt.Numero_animal == p_numero_a:
            return True
        else:
            return False
# Fonction permettant de cacher les labels d'erreur
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
        # Désactiver les labels, lineEdits et comboBox de Oiseau et Reptile
        self.label_longueur_bec.setDisabled(True)
        self.lineEdit_longueur_bec.setDisabled(True)
        self.label_venimeux.setDisabled(True)
        self.comboBox_venimeux.setDisabled(True)
        # Si une famille est sélectionnée, exécuter la méthode ChoisirFamilleAnimal()
        self.comboBox_famille_animal.currentIndexChanged.connect(self.ChoisirFamilleAnimal)


    # # Entrée de donnée
        self.comboBox_enclos_animal.addItems("E1", "E2", "E3")
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
    # Fonction permettant de réinitialiser les labels d'erreur
    def Reinitialiser_label_erreur(self):
        """
        Réinitialiser les labels d'erreur
        """
        self.label_erreur_longueur_bec.setText("")
        self.label_erreur_numero_animal_existe.setText("")
        self.label_erreur_numero_animal_existe_pas.setText("")
        self.label_erreur_numero_animal_invalide.setText("")
        self.label_erreur_poids_animal.setText("")

    # Méthode pour réinitialiser les contrôles
    def Reinitialiser_controles(self):
        """
        Réinitialiser les lineEdits
        """
        self.lineEdit_numero_animal.clear()
        self.lineEdit_longueur_bec.clear()
        self.lineEdit_surnom_animal.clear()
        self.lineEdit_poids_animal.clear()

    # Méthode qui permet d'activer et désactiver les contrôles selon le choix
    def Activer_contrôles_animal(self, p_var: int):
        """
        Activer et désactiver les contrôles selon le choix de l'utilisateur :
        mammifère, oiseau ou reptile
        """
        # Activer/désactiver les contrôles
        self.label_venimeux.setDisabled(p_var=3)
        self.comboBox_venimeux.setDisabled(p_var)
        self.label_couleur_poil.setDisabled(p_var=1)
        self.comboBox_couleur_poil.setDisabled(p_var=1)
        self.label_longueur_bec.setDisabled(p_var=2)
        self.lineEdit_longueur_bec.setDisabled(p_var=2)


    # Méthode permettant de choisir la famille de l'animal
    def ChoisirFamilleAnimal(self):
        """
        Permet de tester le choix de l'utilisateur(Mammifère, oiseau ou reptile)
        et d'appeler la méthode qui active less contrôles
        """
        if self.comboBox_famille_animal.currentText()=="Mammifère":
            v=1
        elif self.comboBox_famille_animal.currentText()=="Oiseau":
            v=2
        else:
            v=3
        self.Activer_contrôles_animal(v)

    # Gestionnaire d'événement du bouton ajouter animal
    @pyqtSlot()
    def on_pushButton_ajouter_animal_clicked(self):
        #Cacher les labels d'erreur
        cacher_labels_erreur(self)
        # Instancier un objet animal
        animal = Classes.Animal()
        # Entrée de donnée pour les attrbuts de l'objet animal
        animal._numero_animal=self.lineEdit_numero_animal.text()
        animal._poids=self.lineEdit_poids_animal.text()
        animal.Famille=self.comboBox_famille_animal.currentText()
        animal.Surnom=self.lineEdit_surnom_animal.text().capitalize()

        # isHidden
        # Instancier un mammifère, un oiseau ou un reptile
        if self.comboBox_famille_animal.currentText()=="Mammifère":
            MonAnimal= Mammifere()

        elif self.comboBox_famille_animal.currentText()=="Reptile":
            MonAnimal= Oiseau()

        else:
            MonAnimal = Reptile()
        # Validation
        MonAnimal.Famille_Animal = self.comboBox_famille_animal.currentText()
        MonAnimal.Numero_animal = self.lineEdit_numero_animal.Text()
        if MonAnimal.Numero_animal == "":
            self.label_erreur_numero_animal.setText("<font color=\"#ff0000\">2 letttres suivies d'un tiret puis de cinq chiffres</font>")
        else:
            Verifie_numero_animal= Verifier_numero_animal_existe(MonAnimal.Numero_animal)
            if Verifie_numero_animal:
                self.label_erreur_numero_local.setTxt("<font colr=\"#ff0000\">Numéro de local existe déjà</font>")

        MonAnimal.Enclos_animal=self.comboBox_enclos_animal.currentText()
        try:
            MonAnimal.surnom_animal=self.lineEdit_surnom_animal.text()
        # Si tous les attributs sont valides
        if MonAnimal.Numero_animal != "" and MonAnimal.Enclos_animal != "" and MonAnimal.surnom_animal != "" and not Verifie_numero_animal:
            # Ajouter l'animal dans la liste des animaux
            Classes.Animal.ls_animaux.append(MonAnimal)
            self.Reinitialiser_controles()
        # Sinon si la famille de l'animal est oiseau
        elif self.comboBox_famille_animal.currentText=="Oiseau":
            MonAnimal.longueur_bec = self.lineEdit_longueur_bec.text()
            try:
                if MonAnimal.longueur_bec == 0:
                    self.label_erreur_longueur_bec.setText("<font color=\"#ff0000\">Entrer un nombre entier supérieur à 18</font>")
            except:
                self.label_erreur_longueur_bec.setText("<font color=\"#ff0000\">Entrer un nombre entier>")
            # Si tous les attribut sont valides
            if MonAnimal.Numero_animal != "" and MonAnimal.surnom_animal != "" and MonAnimal.Enclos_animal != "" and not Verifie_numero_animal:
                # Ajouter l'animal à la liste d'animaux
                Classes.Animal.ls_animaux.append(MonAnimal)
                self.Reinitialiser_controles()










    @pyqtSlot()
    def on_pushButton_rechercher_animal_clicked(self):
        # Cacher les labels d'erreur
        cacher_labels_erreur(self)

