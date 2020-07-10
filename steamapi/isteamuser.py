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
