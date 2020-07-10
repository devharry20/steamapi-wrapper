from helpers import _apicall, str_format


class ISteamUser:
    def __init__(self, **kwargs):
        self.api_key = kwargs.get('api_key')


    def get_friend_list(self, steamid):
        friend_list = _apicall(f'https://api.steampowered.com/ISteamUser/GetFriendList/v1/?key={self.api_key}&steamid={steamid}')

        return friend_list

    def get_player_bans(self, *steamids):
        steamids = str_format(steamids)

        player_bans = _apicall(f'http://api.steampowered.com/ISteamUser/GetPlayerBans/v1/?key={self.api_key}&steamids={steamids}')

        return player_bans

    def get_player_summaries(self, *steamids):
        steamids = str_format(steamids)

        player_summaries = _apicall(f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={self.api_key}&steamids={steamids}')

        return player_summaries

    def resolve_vanity_url(self, vanity):
        resolved_player = _apicall(f'https://api.steampowered.com/ISteamUser/ResolveVanityURL/v1/?key={self.api_key}&vanityurl={vanity}')

        return resolved_player

class ISteamUserStats:
    def __init__(self, **kwargs):
        self.api_key = kwargs.get('api_key')

    def get_global_achievement_percentages_for_app(self, gameid):
        app_percentages = _apicall(f'https://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v2/?key={self.api_key}&gameid={gameid}')

        return app_percentages

    def get_global_stats_for_game(self, appid, count, name, startdate, enddate):
        global_stats = _apicall(f'https://api.steampowered.com/ISteamUserStats/GetGlobalStatsForGame/v1/?key={self.api_key}&appid={appid}&count={count}&name[0]={name}&startdate={startdate}&enddate={enddate}')

        return global_stats

    def get_number_of_current_players(self, appid):
        current_players = _apicall(f'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?key={self.api_key}&appid={appid}')

        return current_players

    def get_player_achievements(self, steamid, appid):
        player_achievements = _apicall(f'https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v1/?key={self.api_key}&steamid={steamid}&appid={appid}&l=en')

        return player_achievements

    def get_schema_for_game(self, appid):
        game_schema = _apicall(f'https://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/?key={self.api_key}&appid={appid}&l=en')

        return game_schema

    def get_user_stats_for_game(self, steamid, appid):
        user_stats = _apicall(f'https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v2/?key={self.api_key}&steamid={steamid}&appid={appid}')

        return user_stats

