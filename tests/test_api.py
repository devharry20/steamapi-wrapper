import unittest
import sys
import time

sys.path.append('../')
from steamapi.api import ISteamUser, ISteamUserStats

STEAM_ID = 76561198235120724
API_KEY = ''

isteamuser = ISteamUser(api_key=API_KEY)
isteamuserstats = ISteamUserStats(api_key=API_KEY)


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

    def test_resolve_vanity_url(self):
        r = isteamuser.resolve_vanity_url('massivebellend')

        self.assertIsInstance(r, dict)
        time.sleep(2)


class ISteamUserStats_Test(unittest.TestCase):
    def get_global_achievement_percentages_for_app(self):
        r = isteamuserstats.get_global_achievement_percentages_for_app(730)

        self.assertIsInstance(r, dict)
        time.sleep(2)
    
    def get_global_stats_for_game(self):
        r = isteamuserstats.get_global_stats_for_game(730, 1, 'any', 51726, 52637)

        self.assertIsInstance(r, dict)
        time.sleep(2)

    def test_get_number_of_current_players(self):
        r = isteamuserstats.get_number_of_current_players(730)

        self.assertIsInstance(r, dict)
        time.sleep(2)

    def test_get_player_achievements(self):
        r = isteamuserstats.get_player_achievements(STEAM_ID, 730)

        self.assertIsInstance(r, dict)
        time.sleep(2)

    def test_get_schema_for_game(self):
        r = isteamuserstats.get_schema_for_game(730)

        self.assertIsInstance(r, dict)
        time.sleep(2)

    def test_get_user_stats_for_game(self):
        r = isteamuserstats.get_user_stats_for_game(STEAM_ID, 730)

        self.assertIsInstance(r, dict)
        time.sleep(2)



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ISteamUser_Test))
    suite.addTest(unittest.makeSuite(ISteamUserStats_Test))

    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(len(result.errors) + len(result.failures))



