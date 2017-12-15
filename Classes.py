import io
import os
import string


################################################
################################################
##################-- ACTION --##################
################################################
################################################


class Action(object):
	"""docstring for Action"""
	def __init__(self, nomDuRepertoire, regle):
		"""

		Constructeur de la classe Action
		Parameters: String nomDuRepertoire, List regle
		return: NULL

		"""
		super(Action, self).__init__()
		self.setNomDuRepertoire(nomDuRepertoire)
		self.setRegle(regle)

	def getNomDuRepertoire(self):
		"""

		Getter de nomDuRepertoire
		parameters: NULL
		return: string

		"""
		return self.nomDuRepertoire
	def setNomDuRepertoire(self, nomDuRepertoire):
		"""

		Setter de nomDuRepertoire
		parameters: string
		return: NULL

		"""
		self.nomDuRepertoire = nomDuRepertoire

################- GETTERS -################

	def getRegle(self):
		"""

		Getter de regle
		parameters: NULL
		return: List

		"""
		return self.regle

################Fin GETTERS################


################- SETTERS -################

	def setRegle(self, regle):
		"""

		Setter de regle
		parameters: List
		return: NULL

		"""
		self.regle = regle

################Fin SETTERS################

	def __str__(self):
		"""

		Affiche le contenu d'un objet de la class Action

		"""
		return self.__dict__()


################################################
################################################
################-- RENOMMAGE --#################
################################################
################################################

class Renommage(Action):
	"""

	La class Renommage hérite de la class Action

	"""
	def __init__(self, nomDuRepertoire, regle):
		"""

		Constructeur de la class Renommage

		"""
		super(Renommage, self).__init__(nomDuRepertoire, regle)
	
	def renommer(self):
		"""

		Méthode permettant de renommer tous les fichier d'un dossier en suivant une regle
		Le nom du répertoire est présent dans un objet de la class Action la class Renommage en hérite.
		parameters: NULL
		return: NULL

		"""
		if self.regle.getAmorce() == "aucun":
			newName = ""

		elif self.regle.getAmorce() == "chiffre":
			if self.regle.getAPartirDe() == '':
				i = 0

			else : 
				i = int(self.regle.getAPartirDe())

		else:
			if self.regle.getAPartirDe() == '':
				i = 0

			else : 
				i = self.lettreVersChiffre(self.regle.getAPartirDe())

		for filename in os.listdir(self.nomDuRepertoire):
			*nomActuel, extension = filename.split(".")

			if "." + extension in self.regle.getExtension():
				i += 1

				if self.regle.getAmorce() == "chiffre":
					newName = i

				elif self.regle.getAmorce() == "lettre":
					newName = self.chiffreVersLettre(i)

				newName = newName + self.regle.getPrefixe()

				if self.regle.getChoixNomFichier() == False:
					for text in nomActuel:
						newName = newName + text + "."

				else:
					newName += self.regle.getNomFichier()

				newName = newName + self.regle.getSuffixe() + "." + extension
				print("voici : " + newName)
				os.rename(self.nomDuRepertoire + "/" + filename, self.nomDuRepertoire + "/" + newName)
	
	def chiffreVersLettre(self, chiffre):
		"""

		Sert pour générer une Amorce sous forme A, AB, BC etc...
		On se sert d'un chiffre pour se repérer dans le code que l'on convertis dans une amorce sous forme de lettre

	    """
		chaine = ""
		
		while chiffre > 0:
			chiffre, retenue = divmod(chiffre - 1, 26)
			chaine = chr(65 + retenue) + chaine

		return chaine

	def lettreVersChiffre(self, lettres):
	    """

		Fait l'inverse de la fonction chiffreVersLettre
		Lorsque l'utilisateur entre une amorce de départ cette fonction permet de retrouver sa valeur en chiffre pour pouvoir la traiter ensuite

	    """
	    chiffre=-25

	    for lettre in lettres:
	        if not lettre in string.ascii_letters:

	            return False

	        chiffre+=ord(lettre.upper())-64+25

	    return chiffre
	
	def __str__(self):

		return self.__dict__()


###############################################
###############################################
##################-- REGLE --##################
###############################################
###############################################


class Regle(object):
	
	def __init__(self, nomRegle, amorce, aPartirDe, prefixe, choixNomFichier, nomFichier, postFixe, extension):
		super(Regle, self).__init__()
		self.setNomRegle(nomRegle)
		self.setAmorce(amorce)
		self.setAPartirDe(aPartirDe)
		self.setPrefixe(prefixe)
		self.setChoixNomFichier(choixNomFichier)
		self.setNomFichier(nomFichier)
		self.setSuffixe(postFixe)
		self.setExtension(extension)

################- GETTERS -################
	
	def getNomRegle(self):
		"""

		Getter de nomRegle
		parameters: NULL
		return: string

		"""
		return self.nomRegle
	
	def getAmorce(self):
		"""
		
		Getter de Amorce
		parameters: NULL
		return: string

		"""
		return self.amorce
	
	def getAPartirDe(self):
		"""
		
		Getter de APartirDe
		parameters: NULL
		return: string

		"""
		return self.aPartirDe
	

	def getPrefixe(self):
		"""
		
		Getter de prefixe
		parameters: NULL
		return: string

		"""
		return self.prefixe
	

	def getChoixNomFichier(self):
		"""
		
		Getter de choixNomFichier
		parameters: NULL
		return: string

		"""
		return self.choixNomFichier
	

	def getNomFichier(self):
		"""
		
		Getter de nomFichier
		parameters: NULL
		return: string

		"""
		return self.nomFichier
	

	def getSuffixe(self):
		"""
		
		Getter de suffixe
		parameters: NULL
		return: string

		"""
		return self.postFixe
	

	def getExtension(self):
		"""
		
		Getter de Extension
		parameters: NULL
		return: string

		"""
		return self.extension

################Fin GETTERS################


################- SETTERS -################


	def setNomRegle(self, nomRegle):
		"""

		Setter de nomRegle
		parameters: string
		return: NULL

		"""
		self.nomRegle = nomRegle

	def setAmorce(self, amorce):
		"""

		Setter de amorce
		parameters: string
		return: NULL

		"""
		self.amorce = amorce

	def setAPartirDe(self, aPartirDe):
		"""

		Setter de aPartirDe
		parameters: string
		return: NULL

		"""
		self.aPartirDe = aPartirDe

	def setPrefixe(self, prefixe):
		"""

		Setter de prefixe
		parameters: string
		return: NULL

		"""
		self.prefixe = prefixe

	def setChoixNomFichier(self, choixNomFichier):
		"""

		Setter de choixNomFichier
		parameters: string
		return: NULL

		"""
		if choixNomFichier == "True":
			self.choixNomFichier = True

		elif choixNomFichier == "False":
			self.choixNomFichier = False

		else:
			raise TypeError

	def setNomFichier(self, nomFichier):
		"""

		Setter de nomFichier
		parameters: string
		return: NULL

		"""
		if self.getChoixNomFichier():
			self.nomFichier = nomFichier

		else:
			self.nomFichier = None

	def setSuffixe(self, postFixe):
		"""

		Setter de suffixe
		parameters: string
		return: NULL

		"""
		self.postFixe = postFixe

	def setExtension(self, extension):
		"""

		Setter de extension 
		parameters: string
		return: NULL

		"""
		self.extension = extension.split(",")

################Fin SETTERS################

	def __str__(self):
		"""

		Méthode permettant de d'afficher toutes les variables d'un objet de la class Regle

		"""
		extension = ""
		longueur = len(self.extension)

		for x in self.extension:
			if longueur > 1:
				extension = extension + x + ","
				longueur -= 1

			else:
				extension = extension + x

		return str(self.getNomRegle()) + ";"+ str(self.getAmorce()) + ";"+ str(self.getAPartirDe()) + ";"+ str(self.getPrefixe()) + ";"+ str(self.getChoixNomFichier()) + ";"+ str(self.getNomFichier()) + ";"+ str(self.getSuffixe()) + ";" + str(extension)


################################################
################################################
################-- LISTEREGLE --################
################################################
################################################


class ListeRegle(object):
	"""docstring for ListeRegle"""
	def __init__(self, regles=None):
		"""

		Constructeur de la class listeRegle 

		"""
		self.setRegles(regles)

################- GETTERS -################
	
	def getRegles(self):
		"""

		Getter de regles
		parameters: NULL
		return: List

		"""
		return self.regles

################Fin GETTERS################


################- SETTERS -################

	def setRegles(self, regles):
		"""

		Setter de regles
		parameters: List
		return: NULL

		"""
		self.regles = regles

################Fin SETTERS################


	def ajouterRegle(self, maRegle):
		"""

		Ajoute une règle à la liste des règles
		parameters: String
		return: List

		"""
		self.regles.append(maRegle)

		return self

	def charger(self):
		"""
		
		Récupère la règle dans un fichier puis:
		Remplace les paramètres de la règle en cours d'utilisation par ceux de la règle que l'on souhaite charger
		parameters:NULL
		return: List

		"""
		mesRegles = []

		for regle in io.open("ListeDesRegles.txt", "r", encoding="ISO-8859-1").readlines():
			regleTab = regle.replace("\n","").split(";")
			mesRegles.append(Regle(regleTab[0], regleTab[1], regleTab[2], regleTab[3], regleTab[4], regleTab[5], regleTab[6], regleTab[7]))

		self.setRegles(mesRegles)
		return self

	def sauvegarder(self):
		"""
		
		Sauvegarde la règle dans un fichier
		parameters: NULL
		return: NULL

		"""
		file = open("ListeDesRegles.txt", "w")

		for regle in self.regles:
			file.write(str(regle) + "\n")

	def supprimerRegle(self, regle):
		"""

		Supprime une règle présente dans un fichier
		parameters: List
		return:

		"""
		nouvelleListe = []

		for regleTest in self.getRegles():
			if str(regleTest) != str(regle):
				nouvelleListe.append(regleTest)

		self.setRegles(nouvelleListe)
		return self

	def __str__(self):
		"""

		Méthode permettant de d'afficher toutes les variables d'un objet de la class ListeRegle

		"""
		return self.__dict__()