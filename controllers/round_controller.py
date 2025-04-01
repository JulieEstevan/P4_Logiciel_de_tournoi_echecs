from models.round_model import Round
from models.match_model import Match
from models.player_model import Player
from models.tournament_model import Tournament
from controllers.match_controller import MatchController
from datetime import datetime
from random import shuffle

class RoundController:
    
    @staticmethod
    def first_round(players: list, tournament):

        first_round = Round(name="Round 1")
        first_round.start_date = str(datetime.now())
        tournament.current_round = 1
        shuffle(players)
        tournament_players = []
        for player in players:
            player_model = Player(
                        player["last_name"],
                        player["first_name"],
                        player["birth_date"],
                        player["national_id"],
                    )
            tournament_players.append(player_model)
        for i in range(0, len(tournament_players), 2):
            player1 = tournament_players[i]
            player2 = tournament_players[i + 1]
            match = Match(
                f"{player1.first_name} {player1.last_name}", player1.points,
                f"{player2.first_name} {player2.last_name}", player2.points)
            tournament.pairs_already_played.append({
                "player1": player1.national_id,
                "player2": player2.national_id})
            MatchController.get_score(match, player1, player2)
            first_round.append_match(match.match_json())
        first_round.end_date = str(datetime.now())
        tournament.rounds.append(first_round.round_json())
        tournament.add_round(tournament)
        # trouver la solution pour append le round dans tournament.round