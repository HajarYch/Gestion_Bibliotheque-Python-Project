import customtkinter as ctk
from src.Bibliotheque import Bibliotheque, Membre


def membres_tab(tab,bibliotheque):
    for widget in tab.winfo_children():
        widget.destroy()

    #charger les données
    bibliotheque.charger_livres("../data/livres.txt")
    bibliotheque.charger_membres("../data/membres.txt")
    # background color
    tab.configure(fg_color="#FFF2E0")

    # Cadre principal
    main_frame = ctk.CTkFrame(tab)
    main_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # list des livres
    list_frame = ctk.CTkScrollableFrame(main_frame, width=500, fg_color="#FFF2E0")
    list_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)

    ctk.CTkLabel(list_frame,text="Liste des Membres",font=("Great Vibes", 50, "bold"),text_color="#2E4053").pack(pady=10)

    membres_container = ctk.CTkFrame(list_frame,fg_color="#FFF2E0")
    membres_container.pack(fill="both", expand=True, padx=5, pady=5)

    # formulaire d'insertion
    form_frame = ctk.CTkFrame(main_frame, width=300, fg_color="#2E4053")
    form_frame.pack(side="right", fill="y", padx=5, pady=5)

    ctk.CTkLabel(form_frame, text="Ajouter un membre", font=("ABeeZee", 16)) \
        .grid(row=0, column=0, columnspan=2, pady=10)

    # Champs du formulaire
    membre_fields = ["ID:","Nom:"]
    entrées = {}
    for i, label in enumerate(membre_fields, start=1):
        ctk.CTkLabel(form_frame, text=label, font=("ABeeZee", 16)).grid(row=i, column=0, padx=5, pady=5, sticky="e")
        entré = ctk.CTkEntry(form_frame)
        entré.grid(row=i, column=1, padx=5, pady=5)
        entrées[i-1] = entré

    #Afficher les livres
    def afficher_list():
        membres_container.pack_forget()
        membres_container.pack(fill="both", expand=True, padx=5, pady=5)
        for widget in membres_container.winfo_children():
            widget.destroy()

        for membre in bibliotheque.membres:
            afficher_membre(membre)

    #affichage/load d'un livre dans un container
    def afficher_membre(membre):
        container = ctk.CTkFrame(membres_container, border_width=1, corner_radius=5)
        container.pack(fill="x", padx=5, pady=5)

        infos = [f"ID: {membre.ID}", f"Titre: {membre.nom}" ]
        #Affichage les 4 premiers attributs
        for info in infos[:3]:
         ctk.CTkLabel(container, text=info,font=("ABeeZee",16), anchor="w").pack(fill="x", padx=5, pady=2)
        ctk.CTkLabel(container, text="Livres empruntés : ", font=("ABeeZee", 16), anchor="w").pack(fill="x", padx=5, pady=2)
        for l in membre.list_emprunte:
            livre=f"{l.titre} ({l.ISBN})"
            ctk.CTkLabel(container, text=livre, font=("ABeeZee", 16), anchor="w").pack(fill="x", padx=5, pady=2)
    #ajouter un membre dans list des membres de bibliothèque
    def ajouter_membre():
        try:
            for i in entrées:
                entrées[i] = entrées[i].get()
            if not all(entrées.values()):
                raise ValueError("Veuillez remplir tous les champs.")
            nouveau = Membre(
                entrées[0], entrées[1])
            bibliotheque.enregistrer_membre(nouveau)
            bibliotheque.sauvegarder_membre()
            afficher_list()
            for entré in entrées.values():
                entré.delete(0, "end")
        except Exception as e:
            print(f"Erreur: {e}")

    # bouton d'ajout
    ctk.CTkButton(form_frame, text="Ajouter Membre",font=("ABeeZee",16), command=ajouter_membre).grid(row=len(membre_fields) + 1, column=0, columnspan=2, pady=10, sticky="ew")
    afficher_list()
