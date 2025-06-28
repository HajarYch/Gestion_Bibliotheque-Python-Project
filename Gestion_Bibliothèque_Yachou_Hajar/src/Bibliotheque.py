import csv
from datetime import datetime

from Exceptions import QuotaEmpruntDepasseError,LivreIndisponibleError,MembreInexistantError,LivreInexistantError
import os
#Class Bibleotheque
class Bibliotheque :
 def __init__(self):
     self.livres = []
     self.membres = []

 #Ajouter un livre
 def ajouter_livre(self, livre):
     self.livres.append(livre)

 #Supprimer un livre
 def supprimer_livre(self, livre):
     for l in self.livres:
         if l.ISBN == livre.ISBN:
             self.livres.remove(l)
             return

 #Sauvegarder un livre
 def sauvegarder_livre(self):
     with open("../data/livres.txt", "w", encoding="utf-8") as f:
         for livre in self.livres:
             ligne = f"{livre.ISBN};{livre.titre};{livre.auteur};{livre.année};{livre.genre};{livre.statut}\n"
             f.write(ligne)
 #charger les livres
 def charger_livres(self, filename="../data/livres.txt"):
     self.livres = []
     if os.path.exists(filename):
         with open(filename, "r", encoding="utf-8") as f:
             for ligne in f:
                 parts = ligne.strip().split(";")
                 if len(parts) == 6:
                     ISBN, titre, auteur, annee, genre, statut = parts
                     livre = Livre(ISBN, titre, auteur, annee, genre, int(statut))
                     self.livres.append(livre)
 #Ajouter un membre
 def enregistrer_membre(self, membre):
     self.membres.append(membre)

 #Sauvegarder un membre
 def sauvegarder_membre(self):
     with open("../data/membres.txt", "w", encoding="utf-8") as f:
         for membre in self.membres:
             emprunts = ",".join([livre.ISBN for livre in membre.list_emprunte])
             ligne = f"{membre.ID};{membre.nom};{emprunts}\n"
             f.write(ligne)

 # charger les membres
 def charger_membres(self, filename="../data/membres.txt"):
     self.membres = []
     if os.path.exists(filename):
         with open(filename, "r", encoding="utf-8") as f:
             for ligne in f:
                 parts = ligne.strip().split(";")
                 if len(parts) >= 2:
                     ID, nom = parts[0], parts[1]
                     membre = Membre(ID, nom)
                     if len(parts) == 3 and parts[2]:
                         isbn_list = parts[2].split(",")
                         for isbn in isbn_list:
                             livre = next((l for l in self.livres if l.ISBN == isbn), None)
                             if livre:
                                 membre.list_emprunte.append(livre)
                                 livre.statut = 1  # Mark book as borrowed
                     self.membres.append(membre)
#Gerer les empruntes
 def retour(self,livre,membre):
     if livre in membre.list_emprunte:
         livre.statut = 0
         membre.list_emprunte.remove(livre)
         self.sauvegarder_livre()
         self.sauvegarder_membre()
         print(f"Membre {membre.ID} a retourné livre {livre.ISBN}!")

 def emprunt(self,livre,membre):
     if livre.statut==0 :
         livre.statut=1
         membre.list_emprunte.append(livre)
         self.sauvegarder_livre()
         self.sauvegarder_membre()
     else:
         raise LivreIndisponibleError("Le livre n'est pas disponible!")

#enregistrer la date des emprunts et retours dans historique.csv
 def enregistrer_historique(livre, membre, action):
        with open("../data/historique.csv", "a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow([datetime.now().isoformat(), livre.ISBN, membre.ID, action])


#Class Livre
class Livre :
    def __init__(self,ISBN,titre,auteur,année,genre,statut=0): #le livre est disponible par defaut
        self._ISBN=ISBN
        self._titre=titre
        self._auteur=auteur
        self._année=année
        self._genre=genre
        self._statut=statut

 #Getters
    @property
    def ISBN(self):
        return self._ISBN
    @property
    def titre(self):
        return self._titre
    @property
    def auteur(self):
        return self._auteur
    @property
    def année(self):
        return self._année
    @property
    def genre(self):
        return self._genre
    @property
    def statut(self):
        return self._statut
 #Setters
    @ISBN.setter
    def ISBN(self,ISBN):
        self._ISBN=ISBN
    @titre.setter
    def titre(self,titre):
        self._titre=titre
    @auteur.setter
    def auteur(self,auteur):
        self._auteur=auteur
    @année.setter
    def année(self,année):
        self._année=année
    @genre.setter
    def genre(self,genre):
        self._genre=genre
    @statut.setter
    def statut(self,statut):
        self._statut=statut

#Class Membre
class Membre :
    def __init__(self,ID,nom):
        self._ID = ID
        self._nom = nom
        self._list_emprunte = []

 #Getters
    @property
    def ID(self):
        return self._ID
    @property
    def nom(self):
        return self._nom
    @property
    def list_emprunte(self):
        return self._list_emprunte

 #Setters
    @ID.setter
    def ID(self,ID):
        self._ID = ID
    @nom.setter
    def nom(self,nom):
        self._nom = nom
    @list_emprunte.setter
    def list_emprunte(self,list_emprunte):
        self._list_emprunte = list_emprunte