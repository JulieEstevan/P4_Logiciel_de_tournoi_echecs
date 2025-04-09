class MenuView:
    """
    Displays menus information and messages for interact with the user and giving them specific info.

    ...

    Attributes
    ----------
    None
    
    Methods
    -------
    display_main_menu()
        Displays the main menu and its options to the user.
    display_player_menu()
        Displays the player menu and its options to the user.
    display_tournament_menu()
        Displays the tournament menu and its options to the user.
    display_report_menu()
        Displays the report menu and its options to the user.
    display_report_submenu(tournament : Tournament)
        Displays the report submenu and its options to the user.
    display_invalid_choice()
        Displays an error message for invalid entry to the user.
    display_goodbye()
        Displays a goodbye message to the user.
    get_user_choice()
        Asks the user for a choice.
    display_message(message : str)
        Displays a customizable message to the user.
    """

    @staticmethod
    def display_main_menu() -> None:
        """
        Displays the main menu and its options to the user.

        Returns
        -------
        None
        """

        print("\n--- Menu Principal ---\n")
        print("1. Joueurs")
        print("2. Tournois")
        print("3. Rapports")
        print("4. Quitter \n")

    @staticmethod
    def display_player_menu() -> None:
        """
        Displays the player menu and its options to the user.
        
        Returns
        -------
        None
        """

        print("\n--- Menu Joueurs ---\n")
        print("1. Ajouter un joueur")
        print("2. Liste des joueurs")
        print("3. Retour au menu principal\n")

    @staticmethod
    def display_tournament_menu() -> None:
        """
        Displays the tournament menu and its options to the user.
        
        Returns
        -------
        None
        """

        print("\n--- Menu Tournois ---\n")
        print("1. Créer un tournoi")
        print("2. Débuter un tournoi")
        print("3. Liste des tournois")
        print("4. Retour au menu principal\n")

    @staticmethod
    def display_report_menu() -> None:
        """
        Displays the report menu and its options to the user.
        
        Returns
        -------
        None
        """

        print("\n--- Menu Rapports ---\n")
        print("1. Afficher la liste des joueurs par ordre alphabétique")
        print("2. Afficher la liste des tournois")
        print("3. Afficher les informations détaillées d'un tournoi")
        print("4. Retour au menu principal\n")

    @staticmethod
    def display_report_submenu(tournament) -> None:
        """
        Displays the report submenu and its options to the user.

        Parameters
        ----------
        tournament : Tournament
            A specific tournament.
        
        Returns
        -------
        None
        """

        print("\n--- Menu Tournoi détaillé ---\n")
        print(f"Nom : {tournament.name}\nLieu : {tournament.location}\nDébut : {tournament.start_date}\nFin : {tournament.end_date}")

        print("\n--- Choisir les détails du tournoi à afficher ---\n")
        print("1. Afficher la liste des joueurs")
        print("2. Afficher la liste des tours et matchs")
        print("3. Retour au menu rapports\n")

    @staticmethod
    def display_invalid_choice() -> None:
        """
        Displays an error message for invalid entry to the user.

        Returns
        -------
        None
        """

        print("Choix invalide, essayez autre chose.")

    @staticmethod
    def display_goodbye() -> None:
        """
        Displays a goodbye message to the user.

        Returns
        -------
        None
        """

        print("\nÀ bientôt")

    @staticmethod
    def get_user_choice() -> str:
        """
        Asks the user for a choice.

        Returns
        -------
        input : str
            User's choice
        """

        return input("Sélectionner une option: ")
    
    @staticmethod
    def display_message(message) -> str:
        """
        Displays a customizable message to the user.

        Parameters
        ----------
        message : str
            A message to display.

        Returns
        -------
        None
        """

        print(message)