from .snatcher import Snatcher  # Importing the parent class from the other file
import pandas as pd

class PlayersAPI(Snatcher):

    def __init__(self):
        super().__init__()

    def get_player(self, player_id):
        """Fetch player data by player_id."""

        endpoint = f"player/{player_id}/landing"
        return self.get_data(endpoint)

    def get_season_stats(self, season, game_type, limit=-1):
        """
        :param season:
        :param game_type: 2 - regular, 3 - playoff
        :param limit: default -1 to select all, otherwise select top x
        :return:
        """
        endpoint = f"skater/summary?isAggregate=false&isGame=false&limit=-1&cayenneExp=gameTypeId={game_type}%20and%20seasonId={season}"
        result = self.get_data(endpoint, base=False)
        data = pd.DataFrame(result['data'])

        return data

    def get_skater_season_summary(self, season):
        endpoint = f"skater/summary?limit=-1&cayenneExp=seasonId={season}"
        return self.get_data(endpoint, base=False)

    # def get_player_season_stats(self, player_id, season):
    #     """
    #
    #     :param player_id:
    #     :param season: string or int 20222023
    #     :return:
    #     """
    #     """Fetch player data by player_id."""
    #
    #     endpoint = f"people/{player_id}/stats?stats=statsSingleSeasonPlayoffs&season={season}"
    #     return self.get_data(endpoint)

    def get_players_df(self, player_ids):
        """

        :param player_ids: list of player ids
        :return: returns data frame
        """
        pass