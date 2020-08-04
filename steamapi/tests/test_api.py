import unittest
import sys
import time

sys.path.append('..')
from api import ISteamUser, ISteamUserStats, IPlayerService, ISteamApps, ISteamNews, ICSGOServers_730,

STEAM_ID = 12345678910
APP_ID = 730
API_KEY = '' # https://steamcommunity.com/dev/apikey


isteamuser = ISteamUser(api_key=API_KEY)
isteamuserstats = ISteamUserStats(api_key=API_KEY)
iplayerservice = IPlayerService(api_key=API_KEY)
isteamapps = ISteamApps()
isteamnews = ISteamNews(api_key=API_KEY)
icsgoservers = ICSGOServers_730(api_key=API_KEY)


class ISteamUser_Test(unittest.TestCase):
    def test_get_friend_list(self):
        r = isteamuser.get_friend_list(STEAM_ID)

        self.assertIsInstance(r, dict)
        time.sleep(2)
    
    def test_get_player_bans(self):
        r = isteamuser.get_player_bans(STEAM_ID)

        self.assertIsInstance(r, dict)
        time.sleep(2)

    def test_get_player_summaries(self):
        r = isteamuser.get_player_summaries(STEAM_ID)

        self.assertIsInstance(r, dict)
        time.sleep(2)

    def test_get_user_group_list(self):
        r = isteamuser.get_user_group_list(STEAM_ID)

        self.assertIsInstance(r, dict)
        time.sleep(2)
        
    def test_resolve_vanity_url(self):
        r = isteamuser.resolve_vanity_url('xxxxxxxxx')

        self.assertIsInstance(r, dict)
        time.sleep(2)


class ISteamUserStats_Test(unittest.TestCase):
    def test_get_global_achievement_percentages_for_app(self):
        r = isteamuserstats.get_global_achievement_percentages_for_app(APP_ID)

        self.assertIsInstance(r, dict)
        time.sleep(2)
    
    def test_get_global_stats_for_game(self):
        r = isteamuserstats.get_global_stats_for_game(APP_ID, 1, 'all', 51271, 52171)

        self.assertIsInstance(r, dict)
        time.sleep(2)

    def test_get_number_of_current_players(self):
        r = isteamuserstats.get_number_of_current_players(APP_ID)

        self.assertIsInstance(r, dict)
        time.sleep(2)

    def test_get_player_achievements(self):
        r = isteamuserstats.get_player_achievements(STEAM_ID, APP_ID)

        self.assertIsInstance(r, dict)
        time.sleep(2)

    def test_get_schema_for_game(self):
        r = isteamuserstats.get_schema_for_game(APP_ID)

        self.assertIsInstance(r, dict)
        time.sleep(2)

    def test_get_user_stats_for_game(self):
        r = isteamuserstats.get_user_stats_for_game(STEAM_ID, APP_ID)

        self.assertIsInstance(r, dict)
        time.sleep(2)


class IPlayerService_Test(unittest.TestCase):
    def test_get_recently_played_games(self):
        r = iplayerservice.get_recently_played_games(STEAM_ID)

        self.assertIsInstance(r, dict)
        time.sleep(2)

    def test_get_owned_games(self):
        r = iplayerservice.get_owned_games(STEAM_ID, ['include_appinfo', 'include_played_free_games'])

        self.assertIsInstance(r, dict)
        time.sleep(2)

    def test_get_steam_level(self):
        r = iplayerservice.get_steam_level(STEAM_ID)

        self.assertIsInstance(r, dict)
        time.sleep(2)

    def test_get_badges(self):
        r = iplayerservice.get_badges(STEAM_ID)

        self.assertIsInstance(r, dict)
        time.sleep(2)

    def test_get_community_badge_progress(self):
        r = iplayerservice.get_community_badge_progress(STEAM_ID, 1)

        self.assertIsInstance(r, dict)
        time.sleep(2)

    def test_is_playing_shared_game(self):
        r = iplayerservice.is_playing_shared_game(STEAM_ID, APP_ID)

        self.assertIsInstance(r, dict)
        time.sleep(2)


class ISteamApps_Test(unittest.TestCase):
    def test_get_app_list(self):
        r = isteamapps.get_app_list()

        self.assertIsInstance(r, dict)
        time.sleep(2)

    def test_get_server_at_address(self):
        r = isteamapps.get_server_at_address('0.0.0.0')

        self.assertIsInstance(r, dict)
        time.sleep(2)

    def test_up_to_date_check(self):
        r = isteamapps.up_to_date_check(APP_ID, '1.5')

        self.assertIsInstance(r, dict)
        time.sleep(2)

        
class ISteamNews_Test(unittest.TestCase):
    def test_get_news_for_app(self):
        r = isteamnews.get_news_for_app(APP_ID)

        self.assertIsInstance(r, dict)
        time.sleep(2)


class ICSGOServers_730_Test(unittest.TestCase):    
    def test_get_game_servers_status(self):
        r = icsgoservers.get_game_servers_status

        self.assertIsInstance(r, dict)
        time.sleep(2)
        
        
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ISteamUser_Test))
    suite.addTest(unittest.makeSuite(ISteamUserStats_Test))
    suite.addTest(unittest.makeSuite(IPlayerService_Test))
    suite.addTest(unittest.makeSuite(ISteamApps_Test))
    suite.addTest(unittest.makeSuite(ISteamNews_Test))
    suite.addTest(unittest.makeSuite(ICSGOServers_730_Test))

    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(len(result.errors) + len(result.failures))
