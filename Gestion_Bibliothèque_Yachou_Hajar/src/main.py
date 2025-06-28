# In main.py
import customtkinter as ctk
from src.Bibliotheque import Bibliotheque
from views.Statistiques import statistiques_tab
from views.accueil import accueil_tab
from views.livre import livres_tab
from views.membres import membres_tab
from views.emprunts import emprunts_tab


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x700")
        self.title("Mon Bibliothèque")

        self.bibliotheque = Bibliotheque()
        self.bibliotheque.charger_livres("livres.txt")
        self.bibliotheque.charger_membres("membres.txt")

        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(expand=True, fill="both")

        # Add tabs
        self.tab1 = self.tabview.add("Accueil")
        self.tab2 = self.tabview.add("Livres")
        self.tab3 = self.tabview.add("Membres")
        self.tab4 = self.tabview.add("Emprunts")
        self.tab5 = self.tabview.add("Statistiques")

        # Initialize tabs
        self.refresh_all_tabs()
   #Forcer le mis à jour de chaque tab
    def refresh_all_tabs(self):
        accueil_tab(self.tab1)

        for widget in self.tab2.winfo_children():
            widget.destroy()
        livres_tab(self.tab2, self.bibliotheque)

        for widget in self.tab3.winfo_children():
            widget.destroy()
        membres_tab(self.tab3, self.bibliotheque)

        for widget in self.tab4.winfo_children():
            widget.destroy()
        emprunts_tab(self.tab4, self.bibliotheque, refresh_callback=self.refresh_all_tabs)

        statistiques_tab(self.tab5, self.bibliotheque)

app = App()
app.mainloop()