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
        first_round.start_date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        tournament.current_round = 1
        shuffle(tournament.players)
        tournament_players = tournament.players
        matches = []
        MatchView.displayer_message(f"\n------ Matches du {first_round.name} ------\n")
        for i in range(0, len(tournament_players), 2):
            player1 = tournament_players[i]
            player2 = tournament_players[i + 1]
            match = Match(
                f"{player1["first_name"]} {player1["last_name"]}", player1["points"], player1["national_id"],
                f"{player2["first_name"]} {player2["last_name"]}", player2["points"], player2["national_id"])
            MatchView.display_matches(match, first_round)
            matches.append(match)
            tournament.pairs_already_played.append({
                "player1": player1["national_id"],
                "player2": player2["national_id"]})
            tournament.update_pairs_already_played(tournament)
        for match in matches:
            MatchController.get_score(match)
            first_round.append_match(match.match_json())
            tournament.update_player_score(match.player1[1], match.player1[2], tournament)
            tournament.update_player_score(match.player2[1], match.player2[2], tournament)
        first_round.end_date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        tournament.rounds.append(first_round.round_json())
        tournament.add_round(tournament)
    
    @staticmethod
    def generate_round(tournament):

        tournament.current_round += 1
        round = Round(f"Round {tournament.current_round}")
        round.start_date = str(datetime.now())
        tournament_players = tournament.get_ranking(tournament.players)
        matches = []
        players_already_paired = []

        MatchView.displayer_message(f"\n------ Matches du {round.name} ------\n")
        for player1 in tournament_players:
            if player1 in players_already_paired:
                continue
            for player2 in tournament_players:
                if player2 == player1 or player2 in players_already_paired:
                    continue
                if ({
                        "player1": player1["national_id"],
                        "player2": player2["national_id"]} not in tournament.pairs_already_played and {
                        "player1": player2["national_id"],
                        "player2": player1["national_id"]} not in tournament.pairs_already_played):
                    
                    match = Match(
                        f"{player1["first_name"]} {player1["last_name"]}", player1['points'], player1["national_id"],
                        f"{player2["first_name"]} {player2["last_name"]}", player2["points"], player2["national_id"])
                    matches.append(match)
                    MatchView.display_matches(match, round)
                    tournament.pairs_already_played.append({
                        "player1": player1["national_id"],
                        "player2": player2["national_id"]})
                    tournament.update_pairs_already_played(tournament)
                    players_already_paired.append(player1)
                    players_already_paired.append(player2)
                    break
        for match in matches:
            MatchController.get_score(match) #get_score a modifier
            round.append_match(match.match_json())
            tournament.update_player_score(match.player1[1], match.player1[2], tournament)
            tournament.update_player_score(match.player2[1], match.player2[2], tournament)
        round.end_date = str(datetime.now())
        tournament.rounds.append(round.round_json())
        tournament.add_round(tournament)

        # generer les pairs