from models.tournament_model import Tournament
from models.player_model import Player
from views.tournament_view import TournamentView
from controllers.round_controller import RoundController
from datetime import datetime


class TournamentController:
    """
    Manages all operations related to tournaments.

    ...

    Attributes
    ----------
    None

    Methods
    -------
    create_tournament()
        Creates a tournament with its basic info and its players list.
    select_tournament()
        Return a specific tournament based on user's choice.
    play_tournament(tournament)
        Launch a specific tournament, from its start to its end,
        with the ability to quit it and resume it where it stopped.
    display_tournaments_list()
        Displays the list of all the tournaments in the tournaments table.
    """

    @staticmethod
    def create_tournament() -> None:
        """
        Creates a tournament with its basic info and its players list.

        Returns
        -------
        None
        """

        # Request tournament information
        name, location, number_of_rounds = TournamentView.request_tournament_info()
        tournament = Tournament(name, location, int(number_of_rounds))

        # Add players to the tournament
        TournamentView.display_message("\n--- Ajout des joueurs au tournoi ---")
        available_players = []
        for player in Player.load_players():
            player_model = Player(
                    player["last_name"],
                    player["first_name"],
                    player["birth_date"],
                    player["national_id"],
                )
            available_players.append(player_model)
        if available_players == []:
            TournamentView.display_message("Aucun joueur disponible pour ce tournoi.")
            return
        # Display players with numbers for selection
        TournamentView.display_players_list_by_index(available_players)

        # Loop to allow selection of multiple players
        added_players: set = set()  # To avoid duplicates
        while True:
            choice = TournamentView.choice_for_players_to_add()
            if choice.lower() == "t":
                # Check if the user have enter players
                if not added_players:
                    TournamentView.display_message(
                        "\nAucun joueur sélectionné, veuillez sélectionner des joueurs avant"
                        " de terminer la sélection")
                # Force the user to enter a minimum of players based on the number of rounds
                elif len(added_players) < int(number_of_rounds) + 1:
                    TournamentView.display_message(
                        "\nLe nombre de joueurs est insuffisant pour ce tournoi."
                        f"Nombre de joueurs minimum requis = {int(number_of_rounds) + 1}")
                elif len(added_players) % 2 != 0:
                    TournamentView.display_message(
                        "\nCe gestionnaire de tournoi ne peut gérer qu'un nombre pairs de joueurs.")
                else:
                    break

            try:
                # Split the string by commas and convert each part to an index
                indices = [int(num.strip()) - 1 for num in choice.split(",")]
                for index in indices:
                    if 0 <= index < len(available_players):
                        player: Player = available_players[index]
                        if player not in added_players:
                            tournament.add_player(player.player_json())
                            added_players.add(player)
                            TournamentView.display_message(
                                f"Le joueur {player.last_name} {player.first_name} a été ajouté au tournoi.\n")
                        else:
                            TournamentView.display_message(
                                f"Le joueur {player.last_name} {player.first_name} a déjà été ajouté au tournoi.\n")
                    else:
                        TournamentView.display_message(
                            f"Le numéro {index + 1} est invalide. Veuillez entrer un numéro valide.")
            except ValueError:
                TournamentView.display_message(
                    "\nVeuillez entrer un numéro, ou des numéros séparés par des virgules.\n")

        # Finalize the creation of the tournament
        Tournament.save_tournament(tournament.tournament_json())
        TournamentView.display_message(f"\nLe tournoi -- {name} -- a été créé avec succès.")

    @staticmethod
    def select_tournament() -> Tournament:
        """
        Return a specific tournament based on user's choice.

        Returns
        -------
        available_tournaments[index] : Tournament
            A tournament selected by the user.
        """

        # Load available tournaments and its data
        TournamentView.display_message("\n--- Choix du tournoi ---")
        available_tournaments = []
        for tournament in Tournament.load_tournaments():
            tournament_model = Tournament(
                tournament["name"],
                tournament["location"],
                tournament["number_of_rounds"]
            )
            for player in tournament["players"]:
                tournament_model.add_player(player)
            for round in tournament["rounds"]:
                tournament_model.rounds.append(round)
            tournament_model.current_round = tournament["current_round"]
            tournament_model.start_date = tournament["start_date"]
            tournament_model.end_date = tournament["end_date"]
            available_tournaments.append(tournament_model)

        # Verifies its theres tournaments available, and if so displays them for the user to choose
        if available_tournaments == []:
            TournamentView.display_message("Aucun tournoi disponible.")
            return
        TournamentView.display_tournament_list_by_index(available_tournaments)

        # Loop until the user choose a tournament from the list
        while True:
            choice = TournamentView.choice_for_tournament_to_start()
            if choice.lower() == "retour":
                return None
            try:
                index = int(choice) - 1
                if 0 <= index < len(available_tournaments):
                    return available_tournaments[index]
                else:
                    TournamentView.display_message(
                        "Choix invalide. Veuillez entrer un numéro valide.")
            except ValueError:
                TournamentView.display_message(
                    "Entrée invalide. Veuillez entrer un numéro.")

    @staticmethod
    def play_tournament(tournament) -> None:
        """
        Launch a specific tournament, from its start to its end,
        with the ability to quit it and resume it where it stopped.

        Parameters
        ----------
        tournament : Tournament
            Represent a specific tournament.

        Returns
        -------
        None
        """

        # Warns the user from potential miss match if the ratio number of players / numbers of round isn't optimal
        if len(tournament.players) != 2**(tournament.number_of_rounds - 1):
            TournamentView.display_message(
                "\nCe gestionnaire de tournoi fonctionne sous le système de ronde Suisse optimale."
                "\nIci le rapport entre le nombre de joueurs et le nombre de rounds n'est pas optimal."
                "\nCeci peut entraîner certains joueurs à ne pas effectuer de match lors du dernier tour.")

        # Check if the tournament already started, if not starts it
        if tournament.start_date is None:
            tournament.start_date = datetime.now().strftime("%d/%m/%Y")
            tournament.current_round = 1
            tournament.start_tournament(tournament)
            TournamentView.display_message("\n--- Debut du tournoi ---")
        else:
            TournamentView.display_message("\n !! Ce tournoi a déjà débuté. Reprise du tournoi. !! ")

        # Verifies if the tournament is at its first round, if yes starts the first round
        if tournament.current_round == 1:
            RoundController.first_round(tournament)

        # Loop to creates and plays the rounds until it reaches the tournament's number of round
        while tournament.current_round < tournament.number_of_rounds + 1:
            RoundController.generate_round(tournament)

        # Ends the tournament and displays a short summary of it
        tournament.end_date = datetime.now().strftime("%d/%m/%Y")
        tournament.description = TournamentView.requested_tournament_description()
        tournament.end_tournament(tournament)
        tournament.players = tournament.get_ranking(tournament.players)
        TournamentView.tournament_summary(tournament)
        TournamentView.display_message(f"\nLe tournoi -- {tournament.name} -- est terminé.")

    @staticmethod
    def display_tournaments_list() -> None:
        """
        Displays the list of all the tournaments in the tournaments table.

        Returns
        -------
        None
        """

        tournaments_list = Tournament.load_tournaments()
        if not tournaments_list:
            TournamentView.display_message("Aucun tournoi disponible.")
        else:
            TournamentView.tournaments_list(tournaments_list)
