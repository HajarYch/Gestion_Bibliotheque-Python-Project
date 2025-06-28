import customtkinter as ctk
import matplotlib as plt
from src.visualisations import genre_pie,année_bar



def statistiques_tab(tab, bibliotheque):
    # background color
    tab.configure(fg_color="#FFF2E0")
    frame = ctk.CTkFrame(tab,fg_color="#FFF2E0")
    frame.pack(expand=True, fill="both", padx=10, pady=10)
    ctk.CTkLabel(frame,text="Statistiques",font=("Great Vibes", 50, "bold"),text_color="#2E4053").pack(pady=10)

    # Boutton pour generer pie chart des genres
    btn_genre = ctk.CTkButton(frame,text="Livres Par Genre",command=lambda: genre_pie(bibliotheque))
    btn_genre.pack(pady=10, padx=20, fill="x")


    # Boutton pour generer distribution par an
    btn_year = ctk.CTkButton(frame,text="Livre par année",command=lambda: année_bar(bibliotheque) )
    btn_year.pack(pady=10, padx=20, fill="x")

