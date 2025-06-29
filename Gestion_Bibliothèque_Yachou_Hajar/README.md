# 📚 Application de Gestion de Bibliothèque

Cette application de bureau développée en Python permet de gérer les opérations courantes d'une bibliothèque : gestion des livres, des membres, emprunts/retours, et visualisation de statistiques à l'aide de graphiques. Elle propose une interface moderne construite avec `customtkinter`.

---

## 👤 Auteur

- **Nom** : Hajar Yachou

---

## Presentation du project

- **Lien** : https://drive.google.com/drive/u/2/folders/1vnlwp0A_ADVCsEb8QwUUpyoicMPS0Bai

---


## 🛠️ Guide d'installation

1. **Prérequis** : Python 3.10 ou plus  
   Vérifiez votre version avec la commande suivante :

   ```bash
   python --version
   ```

2. **Installation des dépendances** :

   ```bash
   pip install -r requirements.txt
   ```

3. **Lancement de l’application** :

   ```bash
   python main.py
   ```

📌 **Remarques** :
- Les fichiers `livres.txt` et `membres.txt` situés dans le dossier `data/` contiennent les informations persistantes de la bibliothèque.
- Le fichier `historique.csv` conserve un suivi daté de chaque emprunt et retour.
- Les graphiques générés sont enregistrés dans `assests/charts/`.

---

## 💡 Exemples d'utilisation

### ➕ Ajouter un livre
- Rendez-vous dans l’onglet **"Livres"**
- Remplissez les champs : ISBN, Titre, Auteur, Année, Genre
- Cliquez sur **"Ajouter Livre"**

### 👤 Ajouter un membre
- Onglet **"Membres"**
- Renseignez l’ID et le Nom
- Cliquez sur **"Ajouter Membre"**

### 🔄 Emprunter un livre
- Onglet **"Emprunts"**
- Saisir l’**ID du membre** et l’**ISBN du livre**
- Cliquez sur **"Emprunter"**

### ✅ Retourner un livre
- Dans l’onglet **"Emprunts"**, cliquez sur **"Retourner"** à côté du livre emprunté

### 📊 Statistiques
- Onglet **"Statistiques"**
- Visualisez la répartition des livres par genre et par année sous forme de graphiques

---

