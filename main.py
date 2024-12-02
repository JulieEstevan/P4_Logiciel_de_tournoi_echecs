from controllers.PlayerController import PlayerController

def main():
    controller = PlayerController()

    while True:
        print("\n1. Ajouter un Joueur\n2. Liste des Joueurs\n3. Exit")
        choice = input("Choisissez une option: ")

        if choice == '1':
            controller.create_player_controller()
        elif choice == '2':
            controller.players_list_controller()
        elif choice == '3':
            break
        else:
            print("Choix invalide. Reessayez.")

if __name__ == "__main__":
    main()