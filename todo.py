import os

def afficher_menu():
    print("\n=== Todo List ===")
    print("1. Afficher la liste")
    print("2. Ajouter une tâche")
    print("3. Marquer une tâche comme terminée")
    print("4. Afficher les tâches terminées")
    print("5. Supprimer une tâche")
    print("6. Quitter")

def afficher_liste(taches):
    if not taches:
        print("Aucune tâche en cours.")
    else:
        for index, tache in enumerate(taches, start=1):
            print(f"{index}. {tache}")

def ajouter_tache(taches, nouvelle_tache):
    taches.append(nouvelle_tache)
    sauvegarder_taches(taches)
    print("Tâche ajoutée avec succès.")

def marquer_terminee(taches, index):
    if 1 <= index <= len(taches):
        tache_terminee = taches.pop(index - 1)
        sauvegarder_taches(taches)
        sauvegarder_tache_terminee(tache_terminee)
        print(f"Tâche '{tache_terminee}' marquée comme terminée.")
    else:
        print("Index invalide.")

def afficher_taches_terminees():
    taches_terminees = charger_taches_terminees()
    afficher_liste(taches_terminees)

def supprimer_tache(taches, index):
    if 1 <= index <= len(taches):
        tache_supprimee = taches.pop(index - 1)
        sauvegarder_taches(taches)
        print(f"Tâche '{tache_supprimee}' supprimée avec succès.")
    else:
        print("Index invalide.")

def sauvegarder_taches(taches):
    with open("todo.txt", "w") as fichier:
        for tache in taches:
            fichier.write(f"{tache}\n")

def sauvegarder_tache_terminee(tache):
    with open("done.txt", "a") as fichier:
        fichier.write(f"{tache}\n")

def charger_taches():
    taches = []
    if os.path.exists("todo.txt"):
        with open("todo.txt", "r") as fichier:
            taches = [ligne.strip() for ligne in fichier.readlines()]
    return taches

def charger_taches_terminees():
    taches_terminees = []
    if os.path.exists("done.txt"):
        with open("done.txt", "r") as fichier:
            taches_terminees = [ligne.strip() for ligne in fichier.readlines()]
    return taches_terminees

def main():
    taches = charger_taches()

    while True:
        afficher_menu()
        choix = input("Choisissez une option (1-6): ")

        if choix == "1":
            afficher_liste(taches)
        elif choix == "2":
            nouvelle_tache = input("Entrez la nouvelle tâche : ")
            ajouter_tache(taches, nouvelle_tache)
        elif choix == "3":
            index_terminee = int(input("Entrez le numéro de la tâche terminée : "))
            marquer_terminee(taches, index_terminee)
        elif choix == "4":
            print("\n=== Tâches terminées ===")
            afficher_taches_terminees()
        elif choix == "5":
            index_supprimer = int(input("Entrez le numéro de la tâche à supprimer : "))
            supprimer_tache(taches, index_supprimer)
        elif choix == "6":
            print("Au revoir !")
            break

if __name__ == "__main__":
    main()
