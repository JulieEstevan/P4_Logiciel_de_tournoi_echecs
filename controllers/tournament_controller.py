from models.tournament_model import Tournament
from models.player_model import Player
from views.tournament_view import TournamentView
from views.player_view import PlayerView
from controllers.player_controller import PlayerController
from datetime import datetime
class TournamentController:

    @staticmethod
    def create_tournament():

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
                TournamentView.display_message(
                    "Entrée invalide. Veuillez entrer des numéros séparés par des virgules.")
                
        Tournament.save_tournament(tournament.tournament_json())
        TournamentView.display_message(f"Le tournoi {name} a été créé avec succès.")