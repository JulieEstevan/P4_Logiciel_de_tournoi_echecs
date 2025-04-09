from views.menu_view import MenuView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.report_controller import ReportController
from utils.clear import clear_terminal

class MenuController:
    """
    Manages all the operations related to the menu navigation for the user.

    ...

    Attributes
    ----------
    None

    Methods
    -------
    player_menu()
        Make an action from the player menu depending on user choice.
    tournament_menu()
        Make an action from the tournament menu depending on user choice.
    report_menu()
        Make an action from the report menu depending on user choice.
    report_submenu()
        Make an action from the report submenu depending on user choice.
    main_menu()
        Make an action from the main menu depending on user choice.
    """

    def __init__(self) -> None:
        """
        Initializes the link between the MenuView and itself.

        Returns
        -------
        None
        """
        
        self.view = MenuView()

    def player_menu(self) -> None:
        """
        Make an action from the player menu depending on user choice.

        Returns
        -------
        None
        """

        controller = PlayerController()

        while True:
            self.view.display_player_menu()
            choice = self.view.get_user_choice()

            if choice == "1":
                clear_terminal()
                controller.add_player()
            elif choice == "2":
                clear_terminal()
                controller.display_players_list()
            elif choice == "3":
                clear_terminal()
                break
            else:
                self.view.display_invalid_choice()

    def tournament_menu(self) -> None:
        """
        Make an action from the tournament menu depending on user choice.

        Returns
        -------
        None
        """

        controller = TournamentController()

        while True:
            self.view.display_tournament_menu()
            choice = self.view.get_user_choice()

            if choice == "1":
                clear_terminal()
                controller.create_tournament()
            elif choice == "2":
                clear_terminal()
                tournament = controller.select_tournament()
                if tournament:
                    if tournament and not tournament.end_date:
                        controller.play_tournament(tournament)
                    else:
                        self.view.display_message("Ce tournoi est deja termine")
            elif choice == "3":
                clear_terminal()
                controller.display_tournaments_list()
            elif choice == "4":
                clear_terminal()
                break
            else:
                self.view.display_invalid_choice()

    def report_menu(self) -> None:
        """
        Make an action from the report menu depending on user choice.

        Returns
        -------
        None
        """

        controller = ReportController()

        while True:
            self.view.display_report_menu()
            choice = self.view.get_user_choice()

            if choice == "1":
                clear_terminal()
                controller.display_players_report()
            elif choice == "2":
                clear_terminal()
                controller.display_tournaments_report()
            elif choice == "3":
                clear_terminal()
                tournament = TournamentController.select_tournament()
                if tournament:
                    if not tournament.start_date:
                        self.view.display_message("Ce tournoi n'a pas commence")
                    elif not tournament.end_date:
                        self.view.display_message("Ce tournois n'est pas termine")
                    else:
                        self.report_submenu(tournament)
            elif choice == "4":
                clear_terminal()
                break
            else:
                self.view.display_invalid_choice()

    def report_submenu(self, tournament) -> None:
        """
        Make an action from the report submenu depending on user choice.

        Parameters
        ----------
        tournament : Tournament
            Represent a specific tournament

        Returns
        -------
        None
        """

        controller = ReportController()

        while True:
            self.view.display_report_submenu(tournament)
            choice = self.view.get_user_choice()

            if choice == "1":
                clear_terminal()
                controller.display_tournament_players_report(tournament)
            elif choice == "2":
                clear_terminal()
                controller.display_tournament_rounds_and_matches(tournament)
            elif choice == "3":
                clear_terminal()
                break
            else:
                self.view.display_invalid_choice()
            
    def main_menu(self) -> None:
        """
        Make an action from the main menu depending on user choice.

        Returns
        -------
        None
        """

        clear_terminal()

        while True:
            self.view.display_main_menu()
            choice = self.view.get_user_choice()

            if choice == "1":
                clear_terminal()
                self.player_menu()
            elif choice == "2":
                clear_terminal()
                self.tournament_menu()
            elif choice == "3":
                clear_terminal()
                self.report_menu()
            elif choice == "4":
                self.view.display_goodbye()
                break
            else:
                self.view.display_invalid_choice()