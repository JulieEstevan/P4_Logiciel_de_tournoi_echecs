from models.player_model import Player
from views.player_view import PlayerView
from views.round_view import RoundView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController

class ReportController:

    @staticmethod
    def display_players_report():

        PlayerController.display_players_list()

    @staticmethod
    def display_tournaments_report():

        TournamentController.display_tournaments_list()

    @staticmethod
    def display_tournament_players_report(tournament):

        players_list = []
        for player in tournament.players:
            player_model = Player(
                    player["last_name"],
                    player["first_name"],
                    player["birth_date"],
                    player["national_id"],
                )
            player_model.points = player["points"]
            players_list.append(
                {"Nom" : player_model.last_name,
                 "Prenom" : player_model.first_name,
                 "Score" : f"{player_model.points} p",
                 "Date de naissance" : player_model.birth_date,
                 "ID" : player_model.national_id}
            )
        players_list = sorted(players_list, key=str)
        PlayerView.players_list(players_list)

    @staticmethod
    def display_tournament_rounds_and_matches(tournament):

        for round in tournament.rounds:
            RoundView.display_rounds(round)

            for match in round["matches"]:
                RoundView.display_round_matches(match)