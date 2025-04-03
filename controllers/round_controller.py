from models.round_model import Round
from models.match_model import Match
from models.player_model import Player
from models.tournament_model import Tournament
from views.match_view import MatchView
from controllers.match_controller import MatchController
from datetime import datetime
from random import shuffle
from tinydb import Query

class RoundController:
    
    @staticmethod
    def first_round(tournament):

        first_round = Round(name="Round 1")
        first_round.start_date = str(datetime.now())
        tournament.current_round = 1
        shuffle(tournament.players)
        tournament_players = []
        for player in tournament.players:
            player_model = Player(
                        player["last_name"],
                        player["first_name"],
                        player["birth_date"],
                        player["national_id"],
                    )
            tournament_players.append(player_model)
            matches = []
        MatchView.displayer_message(f"\n------ Matches du {first_round.name} ------\n")
        for i in range(0, len(tournament_players), 2):
            player1 = tournament_players[i]
            player2 = tournament_players[i + 1]
            match = Match(
                f"{player1.first_name} {player1.last_name}", player1.points, player1.national_id,
                f"{player2.first_name} {player2.last_name}", player2.points, player2.national_id)
            MatchView.display_matches(match, first_round)
            matches.append(match)
            tournament.pairs_already_played.append({
                "player1": player1.national_id,
                "player2": player2.national_id})
        for match in matches:
            MatchController.get_score(match, player1, player2)
            first_round.append_match(match.match_json())
            tournament.update_player_score(match.player1[1], match.player1[2])
            tournament.update_player_score(match.player2[1], match.player2[2])
        first_round.end_date = str(datetime.now())
        tournament.rounds.append(first_round.round_json())
        tournament.add_round(tournament)
    
    @staticmethod
    def generate_round(tournament):

        round = Round(f"Round {tournament.current_round}")
        round.start_date = str(datetime.now())
        tournament_players = tournament.get_ranking(tournament.players)
        for player in tournament_players:
            print(player["first_name"], player["points"])