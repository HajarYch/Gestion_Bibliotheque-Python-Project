import customtkinter as ctk
from src.Bibliotheque import Bibliotheque, Livre


def livres_tab(tab,bibliotheque):
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

    ctk.CTkLabel( list_frame, text="Liste des Livres",font=("Great Vibes", 50, "bold"),text_color="#2E4053").pack(pady=10)

    livres_container = ctk.CTkFrame(list_frame,fg_color="#FFF2E0")
    livres_container.pack(fill="both", expand=True, padx=5, pady=5)

    # formulaire d'insertion
    form_frame = ctk.CTkFrame(main_frame, width=300, fg_color="#2E4053")
    form_frame.pack(side="right", fill="y", padx=5, pady=5)

    ctk.CTkLabel(form_frame, text="Ajouter un Livre", font=("ABeeZee", 16)) \
        .grid(row=0, column=0, columnspan=2, pady=10)

    # Champs du formulaire
    livre_fields = ["ISBN:","Titre:","Auteur:","Année:","Genre:"]
    entrées = {}
    for i, label in enumerate(livre_fields, start=1):
        ctk.CTkLabel(form_frame, text=label, font=("ABeeZee", 16)).grid(row=i, column=0, padx=5, pady=5, sticky="e")
        entré = ctk.CTkEntry(form_frame)
        entré.grid(row=i, column=1, padx=5, pady=5)
        entrées[i-1] = entré

    #Afficher tous les livres
    def afficher_list():
        livres_container.pack_forget()
        livres_container.pack(fill="both", expand=True, padx=5, pady=5)
        for widget in livres_container.winfo_children():
            widget.destroy()

        for livre in bibliotheque.livres:
            afficher_livre(livre)

    #supprime un livre est fait mis à jour au list
    def supprimer_livre(livre):
        bibliotheque.supprimer_livre(livre) #fonction supprimer du class biblio
        bibliotheque.sauvegarder_livre()
        afficher_list()

    #affichage/load d'un livre dans un container
    def afficher_livre(livre):
        container = ctk.CTkFrame(livres_container, border_width=1, corner_radius=5)
        container.pack(fill="x", padx=5, pady=5)
        #Condition de coleur
        if livre.statut== 0 :
            statut= "Disponible"
            couleur= "green"
        else :
            statut= "Emprunté"
            couleur= "red"

        infos = [f"ISBN: {livre.ISBN}", f"Titre: {livre.titre}",f"Auteur: {livre.auteur}", f"Année: {livre.année}", f"Genre: {livre.genre}",f"Statut: {statut}" ]
        #Affichage les 4 premiers attributs
        for info in infos[:5]:
         ctk.CTkLabel(container, text=info,font=("ABeeZee",16), anchor="w").pack(fill="x", padx=5, pady=2)
        #Affichage de status en coleur
        ctk.CTkLabel(container, text=infos[5],font=("ABeeZee",16), anchor="w", text_color=couleur).pack(fill="x", padx=5, pady=2)

        # Button de suppression
        btns = ctk.CTkFrame(container, fg_color="transparent")
        btns.pack(fill="x", padx=5, pady=5)
        ctk.CTkButton(btns, text="Supprimer",font=("ABeeZee",16),command=lambda :supprimer_livre(livre), width=80, fg_color="red").pack(side="left", padx=2)

    def ajouter_livre():
        try:
            for i in entrées:
                entrées[i] = entrées[i].get()
            if not all(entrées.values()):
                raise ValueError("Veuillez remplir tous les champs.")
            nouveau = Livre(entrées[0], entrées[1], entrées[2],entrées[3], entrées[4])
            bibliotheque.ajouter_livre(nouveau)
            bibliotheque.sauvegarder_livre()
            afficher_list()
            for entré in entrées.values():
                entré.delete(0, "end")
        except Exception as e:
            print(f"Erreur: {e}")

    # bouton d'ajout
    ctk.CTkButton(
        form_frame, text="Ajouter Livre",font=("ABeeZee",16), command=ajouter_livre).grid(row=len(livre_fields) + 1, column=0, columnspan=2, pady=10, sticky="ew")
    afficher_list()
