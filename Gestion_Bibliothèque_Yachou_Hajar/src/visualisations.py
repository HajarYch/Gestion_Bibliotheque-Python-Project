import matplotlib.pyplot as plt
import os

#pie chart de genre des livres
def genre_pie(bibliotheque):
    #stocker dans un dictionnaire le nombre de chaque genre
    genres = {}
    for livre in bibliotheque.livres:
        genres[livre.genre] = genres.get(livre.genre, 0) + 1
    if not genres:
        return
    #plot
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.pie(genres.values(), labels=genres.keys())
    ax.set_title("Livres Par Genre")
    #save in path
    os.makedirs("../assests/charts", exist_ok=True)
    save_path = os.path.join("../assests/charts", "stats_genre")
    plt.savefig(save_path)
    plt.close(fig)
    return save_path
#bar chart des années des livres
def année_bar(bibliotheque):
    #stocker dans un dictionnaire le nombre de chaque année
    years = {}
    for livre in bibliotheque.livres:
        years[livre.année] = years.get(livre.année, 0) + 1
    if not years:
        return
    #plot
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(years.keys(), years.values())
    ax.set_title("Livre par an")
    ax.set_xlabel("Année")
    ax.set_ylabel("Count")
    #save in path
    os.makedirs("../assests/charts", exist_ok=True)
    save_path = os.path.join("../assests/charts", "stats_années")
    plt.savefig(save_path)
    plt.close(fig)
    return save_path