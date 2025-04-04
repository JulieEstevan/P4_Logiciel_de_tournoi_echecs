class MenuView:

    @staticmethod
    def display_main_menu() -> None:

        print("\n--- Menu Principal ---\n")
        print("1. Joueurs")
        print("2. Tournois")
        print("3. Rapports")
        print("4. Quitter \n")

    @staticmethod
    def display_player_menu() -> None:

        print("\n--- Menu Joueurs ---\n")
        print("1. Ajouter un joueur")
        print("2. Liste des joueurs")
        print("3. Retour au menu principal\n")

    @staticmethod
    def display_tournament_menu() -> None:

        print("\n--- Menu Tournois ---\n")
        print("1. Créer un tournoi")
        print("2. Débuter un tournoi")
        print("3. Liste des tournois")
        print("4. Retour au menu principal\n")

    @staticmethod
    def display_report_menu() -> None:

        print("\n--- Menu Rapports ---\n")
        print("1. Afficher la liste des joueurs par ordre alphabétique")
        print("2. Afficher la liste des tournois")
        print("3. Afficher les informations détaillés d'un tournoi")
        print("4. Retour au menu principal\n")

    @staticmethod
    def display_report_submenu(tournament) -> None:

        print("\n--- Menu Tournoi detaille ---\n")
        print(f"Nom : {tournament.name}\nLieu : {tournament.location}\nDebut : {tournament.start_date}\nFin : {tournament.end_date}")

        print("\n--- Choisir les details du tournois a afficher ---\n")
        print("1. Afficher la liste des joueurs")
        print("2. Afficher la liste des tours et matchs")
        print("3. Retour au menu rapports\n")

    @staticmethod
    def display_invalid_choice() -> None:

        print("Choix invalide, essayez autre chose.")

    @staticmethod
    def display_goodbye() -> None:

        print("\nÀ bientôt")

    @staticmethod
    def get_user_choice() -> str:

        return input("Sélectionner une option: ")
    
    @staticmethod
    def display_message(message) -> str:

        print(message)