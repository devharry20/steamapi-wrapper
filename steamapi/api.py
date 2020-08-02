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

    def get_user_group_list(self, steamid):
        user_groups = _apicall(f'https://api.steampowered.com/ISteamUser/GetUserGroupList/v1/?key={self.api_key}&steamid={steamid}')

        return user_groups
    
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


class IPlayerService:
    def __init__(self, **kwargs):
        self.api_key = kwargs.get('api_key')

    def get_recently_played_games(self, steamid, count=1000):
        recently_played = _apicall(f'http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key={self.api_key}&steamid={steamid}&count={count}')
        
        return recently_played

    def get_owned_games(self, steamid, args: list=None):
        if args is None:
            owned_games = _apicall(f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={self.api_key}&steamid={steamid}')
            return owned_games

        additional_args = [x for x in args if x in ['include_appinfo', 'include_played_free_games']]
        url_join = ''.join([f'&{x}=True' for x in additional_args])

        owned_games = _apicall(f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={self.api_key}&steamid={steamid}{url_join}')

        return owned_games

    def get_steam_level(self, steamid):
        steam_level = _apicall(f'https://api.steampowered.com/IPlayerService/GetSteamLevel/v1/?key={self.api_key}&steamid={steamid}')

        return steam_level

    def get_badges(self, steamid):
        badges = _apicall(f'https://api.steampowered.com/IPlayerService/GetBadges/v1/?key={self.api_key}&steamid={steamid}')

        return badges

    def get_community_badge_progress(self, steamid, badgeid):
        badge_progress = _apicall(f'https://api.steampowered.com/IPlayerService/GetCommunityBadgeProgress/v1/?key={self.api_key}&steamid={steamid}&badgeid={badgeid}')

        return badge_progress

    def is_playing_shared_game(self, steamid, appid):
        playing_shared_game = _apicall(f'http://api.steampowered.com/IPlayerService/IsPlayingSharedGame/v0001/?key={self.api_key}&steamid={steamid}&appid_playing={appid}')

        return playing_shared_game

    
class ISteamNews:
    def __init__(self, **kwargs):
        self.api_key = kwargs.get('api_key')

    def get_news_for_app(self, appid):
        news = _apicall(f'http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002?key={self.api_key}&appid={appid}')

        return news

    
class ICSGOServers_730:
    def __init__(self, **kwargs):   
        self.api_key = kwargs.get('api_key') 
    
    @property
    def get_game_servers_status(self):
        status = _apicall(f'https://api.steampowered.com/ICSGOServers_730/GetGameServersStatus/v1/?key={self.api_key}&appid=730')

        return status
