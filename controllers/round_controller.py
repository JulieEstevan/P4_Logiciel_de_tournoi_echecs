from models.round_model import Round
from models.match_model import Match
from views.match_view import MatchView
from views.round_view import RoundView
from controllers.match_controller import MatchController
from datetime import datetime
from random import shuffle


class RoundController:
    """
    Manages all operations related to the rounds.

    ...

    Attributes
    ----------
    None

    Methods
    -------
    first_round(tournament)
        Creates the first round and its matches by shuffling players list and picking pairs randomly.
    geerate_rounds(tournament)
        Creates a round and its matches by ranking the players by score and picking only new pairs.
    """

    @staticmethod
    def first_round(tournament) -> None:
        """
        Creates the first round and its matches by shuffling players list and picking pairs randomly.

        Parameters
        ----------
        tournament : Tournament
            Represent a specific tournament.

        Returns
        -------
        None
        """

        # Starts the first round
        first_round = Round(name="Round 1")
        first_round.start_date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        shuffle(tournament.players)
        tournament_players = tournament.players
        matches = []

        # Creates all the matches for first round
        MatchView.display_message(f"\n------ Matches du {first_round.name} ------\n")
        for i in range(0, len(tournament_players), 2):
            player1 = tournament_players[i]
            player2 = tournament_players[i + 1]
            match = Match(
                f"{player1["first_name"]} {player1["last_name"]}", player1["points"], player1["national_id"],
                f"{player2["first_name"]} {player2["last_name"]}", player2["points"], player2["national_id"])
            MatchView.display_matches(match)
            matches.append(match)
            tournament.pairs_already_played.append({
                "player1": player1["national_id"],
                "player2": player2["national_id"]})
            tournament.update_pairs_already_played(tournament)

        # Plays all the matches and updates player's score
        for match in matches:
            MatchController.get_score(match)
            first_round.append_match(match.match_json())
            tournament.update_players_score(match.player1[1], match.player1[2], tournament)
            tournament.update_players_score(match.player2[1], match.player2[2], tournament)

        # Ends the first round
        first_round.end_date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        tournament.rounds.append(first_round.round_json())
        tournament.current_round += 1
        tournament.add_round(tournament)

    @staticmethod
    def generate_round(tournament) -> None:
        """
        Creates a round and its matches by ranking the players by score and picking only new pairs.

        Parameters
        ----------
        tournament : Tournament
            Represent a specific tournament.

        Returns
        -------
        None
        """

        # Starts the round
        round = Round(f"Round {tournament.current_round}")
        round.start_date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        tournament_players = tournament.get_ranking(tournament.players)
        matches = []
        players_already_paired = []

        # Displays the players ranking to keep tracks
        MatchView().display_message("Classement actuel :")
        RoundView.display_ranking(tournament_players)

        # Creates all the matches for the round
        MatchView.display_message(f"\n------ Matches du {round.name} ------\n")
        for player1 in tournament_players:
            # Finds two players that has not been paired for this round
            if player1 in players_already_paired:
                continue
            for player2 in tournament_players:
                if player2 == player1 or player2 in players_already_paired:
                    continue
                # Verifies that this pair hasn't been already played in the tournament
                if ({
                        "player1": player1["national_id"],
                        "player2": player2["national_id"]} not in tournament.pairs_already_played and {
                        "player1": player2["national_id"],
                        "player2": player1["national_id"]} not in tournament.pairs_already_played):
                    # Creates the match
                    match = Match(
                        f"{player1["first_name"]} {player1["last_name"]}", player1['points'], player1["national_id"],
                        f"{player2["first_name"]} {player2["last_name"]}", player2["points"], player2["national_id"])
                    matches.append(match)
                    MatchView.display_matches(match)
                    tournament.pairs_already_played.append({
                        "player1": player1["national_id"],
                        "player2": player2["national_id"]})
                    tournament.update_pairs_already_played(tournament)
                    players_already_paired.append(player1)
                    players_already_paired.append(player2)
                    break

        # Plays all the matches and updates player's score
        for match in matches:
            MatchController.get_score(match)
            round.append_match(match.match_json())
            tournament.update_players_score(match.player1[1], match.player1[2], tournament)
            tournament.update_players_score(match.player2[1], match.player2[2], tournament)

        # Ends the round
        round.end_date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        tournament.rounds.append(round.round_json())
        tournament.current_round += 1
        tournament.add_round(tournament)
