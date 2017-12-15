from tkinter import *
from Classes import *

class Fenetre(Tk):    
	def __init__(self):
		"""

		Constructeur de la class Fenetre

		""" 	   
		super(Fenetre, self).__init__()
		self.resizable(width=False, height=False)
		self.grid_columnconfigure(0, weight=2)
		self.grid_rowconfigure(0, weight=2)
		self.lesRegles = ListeRegle().charger()
		self.fenetreListerRegle()

	def fenetreCreerRegle(self):
		"""

		Affiche la fenêtre pour créer une règle
		Une fois les paramètres entrés, la fonction creer() se chargera de creer la règle
		parameters: NULL
		return: NULL

		"""
		self.clearScreen()
		self.createMenu()

		Label(self, text="Créer une règle", font=("Helvetica", 22)).grid(row=0, column=0, rowspan=1,  columnspan=7, pady=10)

		Label(self, text="Nom de la règle", font=("Helvetica", 16)).grid(row=3, column=2, rowspan=1,  columnspan=2)
		self.regle = Entry(self, font=("Helvetica", 16))
		self.regle.grid(row=3, column=4, pady=40)

		Label(self, text="Amorce", font=("Helvetica", 13)).grid(row=6, column=1, padx=20)
		self.amorce = self.creerListe(["Aucune","Lettre","Chiffre"])
		self.amorce.grid(row=7, column=1, rowspan=5,  columnspan=1, padx=20)
		Label(self, text="À partir de", font=("Helvetica", 13)).grid(row=12, column=1, padx=20)
		self.aPartirDe = Entry(self, font=("Helvetica", 13))
		self.aPartirDe.grid(row=13, column=1, padx=20, pady=10)

		Label(self, text="Préfixe", font=("Helvetica", 13)).grid(row=6, column=2)
		self.prefixe = Entry(self, font=("Helvetica", 13))
		self.prefixe.grid(sticky=N, row=7, column=2)
		
		Label(self, text="Nom du fichier", font=("Helvetica", 13)).grid(row=6, column=3,  columnspan=1)
		self.checkRadio = IntVar()
		self.boutonNomOriginal = Radiobutton(self, text="Nom original", font=("Helvetica", 13), value=1, variable=self.checkRadio)
		self.boutonNomOriginal.grid(sticky=W, row=7, column=3)
		self.boutonNouveauNom = Radiobutton(self, value=2, variable=self.checkRadio)
		self.boutonNouveauNom.grid(sticky=W, row=8, column=3)
		self.nomFichier = Entry(self, font=("Helvetica", 13), width=11)
		self.nomFichier.bind('<Button-1>', self.selectBoutonNouveauNom)
		self.nomFichier.grid(sticky=E, row=8, column=3)

		Label(self, text="Suffixe", font=("Helvetica", 13)).grid(row=6, column=4)
		self.suffixe = Entry(self, font=("Helvetica", 13))
		self.suffixe.grid(sticky=N, row=7, column=4)

		Label(self, text="Extensions concernées", font=("Helvetica", 13)).grid(row=6, column=5, padx=20)
		self.extension = Entry(self, text="gif, jpg")
		self.extension.grid(sticky=N, row=7, column=5, padx=20)
		self.envoyer = Button(self, text="Créer", command=lambda :self.creer())
		self.envoyer.grid(sticky=N, row=8, column=5, rowspan=1,  columnspan=1, padx=20)

	def fenetreRenommerRepertoire(self):
		"""

		Afficher la fenêtre permettant de renommer tous les fichiers d'un répertoire.
		La fonction traitementRenommer() se chargera de les renommer lorque le bouton "Renommer" se solicité
		parameters: NULL
		return: NULL

		"""
		self.clearScreen()
		self.createMenu()

		Label(self, text="Renommer en lots", font=("Helvetica", 22)).grid(row=0, column=0, rowspan=1,  columnspan=7, pady=10)

		Label(self, text="Nom du répertoire", font=("Helvetica", 16)).grid(row=3, column=2, rowspan=1,  columnspan=2)
		self.nomRepertoire = Entry(self, font=("Helvetica", 16))
		self.nomRepertoire.grid(row=3, column=4, pady=40)

		Label(self, text="Amorce", font=("Helvetica", 13)).grid(row=6, column=1, padx=20)
		self.amorce = self.creerListe(["Aucune","Lettre","Chiffre"])
		self.amorce.grid(row=7, column=1, rowspan=5,  columnspan=1, padx=20)
		Label(self, text="À partir de", font=("Helvetica", 13)).grid(row=12, column=1, padx=20)
		self.aPartirDe = Entry(self, font=("Helvetica", 13))
		self.aPartirDe.grid(row=13, column=1, padx=20, pady=10)

		Label(self, text="Préfixe", font=("Helvetica", 13)).grid(row=6, column=2)
		self.prefixe = Entry(self, font=("Helvetica", 13))
		self.prefixe.grid(sticky=N, row=7, column=2)
		
		Label(self, text="Nom du fichier", font=("Helvetica", 13)).grid(row=6, column=3,  columnspan=1)
		self.checkRadio = IntVar()
		self.boutonNomOriginal = Radiobutton(self, text="Nom original", font=("Helvetica", 13), value=1, variable=self.checkRadio)
		self.boutonNomOriginal.grid(sticky=W, row=7, column=3)
		self.boutonNouveauNom = Radiobutton(self, value=2, variable=self.checkRadio)
		self.boutonNouveauNom.grid(sticky=W, row=8, column=3)
		self.nomFichier = Entry(self, font=("Helvetica", 13), width=11)
		self.nomFichier.bind('<Button-1>', self.selectBoutonNouveauNom)
		self.nomFichier.grid(sticky=E, row=8, column=3)

		Label(self, text="Suffixe", font=("Helvetica", 13)).grid(row=6, column=4)
		self.suffixe = Entry(self, font=("Helvetica", 13))
		self.suffixe.grid(sticky=N, row=7, column=4)

		Label(self, text="Extensions concernées", font=("Helvetica", 13)).grid(row=6, column=5, padx=20)
		self.extension = Entry(self, text="gif, jpg")
		self.extension.grid(sticky=N, row=7, column=5, padx=20)
		self.envoyer = Button(self, text="Renommer", command=self.traitementRenommer())
		self.envoyer.grid(sticky=N, row=8, column=5, rowspan=1,  columnspan=1, padx=20, pady=50)

	def fenetreListerRegle(self):
		"""

		Affiche la fenetre avec la liste des règles enregistrées
		Le bouton "Utiliser" chargera les champs sur le fenetre renommage avec les paramètres de la règle
		Le bouton "Supprimer" Supprimera la règle du fichier dans lequel elle est enregistrée

		"""
		self.clearScreen()
		self.createMenu()
		Label(self, text="Toutes les règles", font=("Helvetica", 22)).grid(row=0, column=0, rowspan=1,  columnspan=8, pady=10)
		Label(self, text="Amorce", font=("Helvetica bold", 13)).grid(row=1, column=2, padx=10, pady=10)
		Label(self, text="À partir de", font=("Helvetica bold", 13)).grid(row=1, column=3, padx=10, pady=10)
		Label(self, text="Préfixe", font=("Helvetica bold", 13)).grid(row=1, column=4, padx=10, pady=10)
		Label(self, text="Nom du fichier", font=("Helvetica bold", 13)).grid(row=1, column=5, padx=10, pady=10)
		Label(self, text="Suffixe", font=("Helvetica bold", 13)).grid(row=1, column=6, padx=10, pady=10)
		Label(self, text="Extension", font=("Helvetica bold", 13)).grid(row=1, column=7, padx=10, pady=10)
		ligne = 2

		for regle in self.lesRegles.getRegles():
			Label(self, text=regle.getNomRegle(), font=("Helvetica", 13)).grid(row=ligne, column=1, padx=10, pady=10)
			Label(self, text=regle.getAmorce(), font=("Helvetica", 13)).grid(row=ligne, column=2, padx=10, pady=10)
			Label(self, text=regle.getAPartirDe(), font=("Helvetica", 13)).grid(row=ligne, column=3, padx=10, pady=10)
			Label(self, text=regle.getPrefixe(), font=("Helvetica", 13)).grid(row=ligne, column=4, padx=10, pady=10)
			Label(self, text=regle.getNomFichier(), font=("Helvetica", 13)).grid(row=ligne, column=5, padx=10, pady=10)
			Label(self, text=regle.getSuffixe(), font=("Helvetica", 13)).grid(row=ligne, column=6, padx=10, pady=10)
			Label(self, text=regle.getExtension(), font=("Helvetica", 13)).grid(row=ligne, column=7, padx=10, pady=10)
			self.utiliser = Button(self, text="Utiliser", command=lambda regle=regle: self.traitementUtiliser(regle))
			self.utiliser.grid(sticky=N, row=ligne, column=8, padx=10, pady=10)
			self.supprimer = Button(self, text="Supprimer", command=lambda regle=regle: self.supprimer(regle))
			self.supprimer.grid(sticky=N, row=ligne, column=9, padx=10, pady=10)

			ligne += 1

	def createMenu(self):
		"""
		
		Permet de créer un menu dans l'entête de la fenêtre menant vers:
		la fenêtre pour renommer les fichiers
		la fenêtre listant toutes les règles sauvegardées
		la fenêtre servant à sauvegarder une nouvelle règle

		"""
		self.barreMenu = Menu(self)
		self.barreMenu.add_command(label="Renommer", command=self.fenetreRenommerRepertoire)
		self.regles = Menu(self.barreMenu, tearoff=0)
		self.regles.add_command(label="Lister", command=self.fenetreListerRegle)
		self.regles.add_command(label="Creer", command=self.fenetreCreerRegle)
		self.barreMenu.add_cascade(label="Règles", menu=self.regles)
		self.barreMenu.add_command(label="?", command=self.aide)
		self.config(menu=self.barreMenu)

	def selectBoutonNouveauNom(self, event):
		self.boutonNouveauNom.select()

	def clearScreen(self):

		for widget in self.winfo_children():
			widget.grid_remove()
			widget.destroy()

	def creer(self):
		"""

		Fonction qui récupère tous les paramètres entrés par l'utilisateur dans la fenêtre pour créer une règle et les envois à la fonction sauvegarder

		"""
		traitOk = True

		if self.regle.get() == "" or self.regle.get() == None :
			traitOk = False

		else:
			nomRegle = self.regle.get()


		if self.amorce.curselection()[0] == 0:
			amorce = "aucun"
			aPartirDe = ""

		elif self.amorce.curselection()[0] == 1:
			amorce = "lettre"
			aPartirDe = self.aPartirDe.get()

		elif self.amorce.curselection()[0] == 2:
			amorce = "chiffre"

			try:
				aPartirDe = int(self.aPartirDe.get())

			except Exception as e:
				traitOk = False

		if self.prefixe.get() == "" or self.prefixe.get() == None :
			traitOk = False

		else:
			prefixe = self.prefixe.get()

		if self.checkRadio.get() == 2:
			choixNomFichier = "True"

		else:
			choixNomFichier = "False"

		if self.nomFichier.get() == "" or self.nomFichier.get() == None :
			traitOk = False

		else:
			nomFichier = self.nomFichier.get()

		if self.suffixe.get() == "" or self.suffixe.get() == None :
			traitOk = False

		else:
			suffixe = self.suffixe.get()
		if self.suffixe.get() == "" or self.suffixe.get() == None :
			traitOk = False

		else:
			suffixe = self.suffixe.get()
		extension = self.extension.get()

		if traitOk:
			print(Regle(nomRegle, amorce, aPartirDe, prefixe, choixNomFichier, nomFichier, suffixe, extension))
			self.lesRegles.ajouterRegle(Regle(nomRegle, amorce, aPartirDe, prefixe, choixNomFichier, nomFichier, suffixe, extension)).sauvegarder()
			self.fenetreListerRegle()

	def traitementRenommer(self):

		"""

		Utilise les paramètres actuellement entrés et les envois à la fonction renommer()

		"""
		traitOk = True
		nomRegle = "Règle Actuelle"

		if self.nomRepertoire.get() == "" or self.nomRepertoire.get() == None :
			traitOk = False
		else:
			nomRepertoire = self.nomRepertoire.get()

		if self.amorce.curselection()[0] == 0:
			amorce = "aucun"
			aPartirDe = ""
		elif self.amorce.curselection()[0] == 1:
			amorce = "lettre"
			aPartirDe = self.aPartirDe.get()
		elif self.amorce.curselection()[0] == 2:
			amorce = "chiffre"
			try:
				aPartirDe = int(self.aPartirDe.get())
			except Exception as e:
				traitOk = False
		
		if self.checkRadio.get() == 2:
			choixNomFichier = "True"
		else:
			choixNomFichier = "False"
		
		if self.nomFichier.get() == "" or self.nomFichier.get() == None :
			traitOk = False
		else:
			nomFichier = self.nomFichier.get()
		
		prefixe = self.prefixe.get()
		suffixe = self.suffixe.get()
		extension = self.extension.get()

		if traitOk:

			self.regleRenommage = Regle(nomRegle, amorce, aPartirDe, prefixe, choixNomFichier, nomFichier, suffixe, extension)
			Renommage(nomRepertoire, self.regleRenommage).renommer()


	def traitementUtiliser(self, regle):

		self.fenetreRenommerRepertoire()
		if regle.getAmorce() == "aucun":
			self.amorce.select_set(0)

		elif regle.getAmorce() == "lettre":
			self.amorce.select_set(1)

		elif regle.getAmorce() == "chiffre":
			self.amorce.select_set(2)

		self.aPartirDe.insert(0, regle.getAPartirDe())
		self.prefixe.insert(0, regle.getPrefixe())

		if regle.getChoixNomFichier() == False:

			self.nomFichier.insert(0, regle.getNomFichier())
			self.nomFichier.bind('<Button-1>', self.selectBoutonNouveauNom)

		self.suffixe.insert(0, regle.getSuffixe())
		self.extension.insert(0, regle.getExtension())

	def supprimer(self, regle):
		self.clearScreen()
		self.createMenu()
		self.lesRegles.supprimerRegle(regle).sauvegarder()
		self.fenetreListerRegle()

	def aide(self):
		self.showinfo()

	def creerListe(self, listeElems):
		liste = Listbox(self, exportselection=False)

		for valeur in range(len(listeElems)):
			liste.insert(valeur + 1, listeElems[valeur])

		liste.select_set(0)
		return liste