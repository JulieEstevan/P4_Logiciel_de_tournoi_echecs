class MenuView:

    @staticmethod
    def display_main_menu() -> None:

        print("\n--- Menu principal ---\n")
        print("1. Joueurs")
        print("2. Tournois")
        print("3. Rapports")
        print("4. Quitter \n")

    @staticmethod
    def display_player_menu() -> None:

        print("\n--- Menu joueurs ---\n")
        print("1. Ajouter un joueur")
        print("2. Liste des joueurs")
        print("3. Retour au menu principal\n")

    @staticmethod
    def display_tournament_menu() -> None:

        print("\n--- Menu Tournoi ---\n")
        print("1. Créer un tournoi")
        print("2. Débuter un tournoi")
        print("3. Liste des tournois")
        print("4. Retour au menu principal\n")

    @staticmethod
    def display_invalid_choice() -> None:

        print("Choix invalide, essayez autre chose.")

    @staticmethod
    def display_goodbye() -> None:

        print("\nÀ bientôt")

    @staticmethod
    def get_user_choice() -> str:

        return input("Sélectionner une option: ")