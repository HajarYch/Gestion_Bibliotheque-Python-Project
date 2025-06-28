import customtkinter as ctk
from datetime import datetime
from src.Bibliotheque import Bibliotheque
import csv
from src.Exceptions import LivreIndisponibleError, QuotaEmpruntDepasseError, MembreInexistantError, LivreInexistantError


def emprunts_tab(tab,bibliotheque,refresh_callback=None):

    #background color
    tab.configure(fg_color="#FFF2E0")


    #frame principal
    main_frame = ctk.CTkFrame(tab)
    main_frame.pack(fill="both", expand=True, padx=10, pady=10)

    #emprunts list frame
    list_frame = ctk.CTkScrollableFrame(main_frame, width=500, fg_color="#FFF2E0")
    list_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)

    ctk.CTkLabel(list_frame, text="Livres Empruntés", font=("Great Vibes", 50, "bold"), text_color="#2E4053").pack(pady=10)
    emprunts_container = ctk.CTkFrame(list_frame, fg_color="#FFF2E0")
    emprunts_container.pack(fill="both", expand=True, padx=5, pady=5)

    #Formulaire : saisie de nom du membre et ISBN du livre
    form_frame = ctk.CTkFrame(main_frame, width=300, fg_color="#2E4053")
    form_frame.pack(side="right", fill="y", padx=5, pady=5)

    ctk.CTkLabel(form_frame, text="Emprunter Livre", font=("ABeeZee", 16))\
        .grid(row=0, column=0, columnspan=2, pady=10)

    # Champs de saisie
    ctk.CTkLabel(form_frame, text="ID du Membre:", font=("ABeeZee", 16))\
        .grid(row=1, column=0, padx=5, pady=5, sticky="e")
    id_membre_entry = ctk.CTkEntry(form_frame)
    id_membre_entry.grid(row=1, column=1, padx=5, pady=5)

    ctk.CTkLabel(form_frame, text="ISBN du Livre:", font=("ABeeZee", 16))\
        .grid(row=2, column=0, padx=5, pady=5, sticky="e")
    isbn_livre_entry = ctk.CTkEntry(form_frame)
    isbn_livre_entry.grid(row=2, column=1, padx=5, pady=5)

    output = ctk.CTkLabel(form_frame, text="", font=("ABeeZee", 14))
    output.grid(row=3, column=0, columnspan=2, pady=5)

    #enregistrer la date des emprunts et retours dans historique.csv
    def enregistrer_historique(livre, membre, action):
        with open("../data/historique.csv", "a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow([datetime.now().isoformat(), livre.ISBN, membre.ID, action])

    #fonction d'emprunt
    def effectuer_emprunt():
        try:
            id_membre = id_membre_entry.get().strip()
            isbn_livre = isbn_livre_entry.get().strip()

            membre = next((m for m in bibliotheque.membres if m.ID == id_membre), None)
            if not membre:
                raise MembreInexistantError()  #exception

            livre = next((l for l in bibliotheque.livres if l.ISBN == isbn_livre), None)
            if not livre:
                raise LivreInexistantError() #exception

            # max =3
            if len(membre.list_emprunte) >= 3:
                raise QuotaEmpruntDepasseError() #exception

            bibliotheque.emprunt(livre, membre) #fontion du class biblio : pour changer le statuts de livre à 1
            bibliotheque.sauvegarder_livre()
            bibliotheque.sauvegarder_membre()
            enregistrer_historique(livre, membre, "emprunt")

            output.configure(text="Emprunt effectué !", text_color="green")

            if refresh_callback:
                refresh_callback()  # This will refresh all tabs
            else:
                # Fallback: manually reload data
                bibliotheque.charger_livres("../data/livres.txt")
                bibliotheque.charger_membres("../data/membres.txt")

            afficher_emprunts()

        except Exception as e:
            output.configure(text=str(e), text_color="red")
    #fonction de retour
    def effectuer_retour(livre, membre):
        try:
            bibliotheque.retour(livre, membre) #fonction du class biblio pour changer statut
            bibliotheque.sauvegarder_livre()
            bibliotheque.sauvegarder_membre()
            enregistrer_historique(livre, membre, "retour")
            output.configure(text="Retour effectué !", text_color="green")
            if refresh_callback:
                refresh_callback()  # This will refresh all tabs
            else:
                # Fallback: manually reload data
                bibliotheque.charger_livres("../data/livres.txt")
                bibliotheque.charger_membres("../data/membres.txt")

            afficher_emprunts()
        except Exception as e:
            output.configure(text=str(e), text_color="red")
    #affichage de l'emprunt dans un container
    def afficher_emprunts():
        for widget in emprunts_container.winfo_children():
            widget.destroy()

        for membre in bibliotheque.membres:
            for livre in membre.list_emprunte:
                container = ctk.CTkFrame(emprunts_container, border_width=1, corner_radius=5)
                container.pack(fill="x", padx=5, pady=5)

                infos = [f"Membre: {membre.nom} ({membre.ID})",f"ISBN: {livre.ISBN}",f"Titre: {livre.titre}",f"Auteur: {livre.auteur}",f"Année: {livre.année}",f"Genre: {livre.genre}"]
                for info in infos:
                    ctk.CTkLabel(container, text=info, font=("ABeeZee", 16), anchor="w").pack(fill="x", padx=5, pady=2)
                btns = ctk.CTkFrame(container, fg_color="transparent")
                btns.pack(fill="x", padx=5, pady=5)
                ctk.CTkButton(
                    btns, text="Retourner", font=("ABeeZee", 16),
                    command=lambda l=livre, m=membre: effectuer_retour(l, m),
                    width=80, fg_color="green"
                ).pack(side="left", padx=2)

    ctk.CTkButton(form_frame, text="Emprunter", font=("ABeeZee", 16), command=effectuer_emprunt)\
        .grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

    afficher_emprunts()
