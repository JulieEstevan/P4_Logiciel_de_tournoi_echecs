from models.tournament_model import Tournament
from models.player_model import Player
from views.tournament_view import TournamentView
from controllers.round_controller import RoundController
class TournamentController:

    @staticmethod
    def create_tournament() -> None:

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
        added_players: set = set() # To avoid duplicates
        while True:
            choice = TournamentView.choice_for_players_to_add()
            if choice.lower() == "t":
                # Check if the user have enter players
                if not added_players:
                    TournamentView.display_message("Aucun joueur selectionné, veuillez selectionner des joueurs avant de terminer la selection")
                # Force the user to enter a minimum of players based on the number of rounds
                elif len(added_players) < int(number_of_rounds) + 1:
                    TournamentView.display_message(f"Le nombre de joueurs est insuffisant pour ce tournoi. Nombre de joueurs minimum requis = {int(number_of_rounds) + 1}")
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
                            TournamentView.display_message(f"Le joueur {player.last_name} {player.first_name} a été ajouté au tournoi.")
                        else:
                            TournamentView.display_message(f"Le joueur {player.last_name} {player.first_name} a déjà été ajouté au tournoi.")
                    else:
                        TournamentView.display_message(f"Le numéro {index + 1} est invalide. Veuillez entrer un numéro valide.")
            except ValueError:
                TournamentView.display_message("Veuillez entrer un numéro, ou des numéros séparés par des virgules.")

        # Finalize the creation of the tournament        
        Tournament.save_tournament(tournament.tournament_json())
        TournamentView.display_message(f"Le tournoi {name} a été créé avec succès.")

    @staticmethod
    def select_tournament():

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
            if not tournament_model.end_date:
                available_tournaments.append(tournament_model)
        if available_tournaments == []:
            TournamentView.display_message("Aucun tournoi disponible.")
            return
        TournamentView.display_tournament_list_by_index(available_tournaments)
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
    def play_tournament(tournament):

        tournament_players = tournament.players
        RoundController.first_round(tournament_players, tournament)