import unittest
import sys
import time

sys.path.append('..')
from isteamuser import ISteamUser

STEAM_ID = 12345678910
API_KEY = ''

isteamuser = ISteamUser(api_key=API_KEY)


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
        r = isteamuser.resolve_vanity_url('xxxxxxxxx')

        self.assertIsInstance(r, dict)
        time.sleep(2)




if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ISteamUser_Test))

    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(len(result.errors) + len(result.failures))