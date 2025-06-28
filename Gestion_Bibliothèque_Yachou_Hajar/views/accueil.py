import customtkinter as ctk
from customtkinter import *


def accueil_tab(tab1):
    tab1.configure(fg_color="#FFF2E0")

    # Main title
    CTkLabel(tab1,
             text="Bienvenue dans votre Bibliothèque Digitale ",
             font=("Great Vibes", 60, "bold"),
             text_color="#2E4053").pack(pady=(30, 10))

    # Sous_lign
    CTkFrame(tab1, height=2, width=500, fg_color="#E67E22").pack(pady=5)

    # Description
    description = [
        "📚 Gestion complète de votre collection de livres",
        "👥 Suivi des membres et de leurs emprunts",
        "⏱ Historique des prêts et des retours",
        "💾 Sauvegarde et restauration de vos données",
        "🔍 Recherche avancée par titre, auteur ou genre",
        "📊 Statistiques et rapports personnalisables"
    ]

    for ligne in description:
        CTkLabel(tab1,
                 text=ligne,
                 font=("ABeeZee", 18),
                 text_color="#2C3E50",
                 justify="center",).pack(pady=2, padx=20, anchor="center")  # anchor="w" aligns left
    # Inspirational quote
    CTkLabel(tab1,
             text='"Une bibliothèque est une chambre d\'amis" - Tahar Ben Jelloun',
             font=("Abhaya Libre", 14),
             text_color="#7F8C8D").pack(pady=(30, 10))


    CTkLabel(tab1,
             text="Commencez par explorer les tabs ci-dessus !",
             font=("Raleway", 16, "bold"),
             text_color="#E67E22").pack(pady=10)