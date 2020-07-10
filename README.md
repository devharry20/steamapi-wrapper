# About
steamapi-wrapper is a simple api wrapper I made to make accessing several steam web api endpoints easier. This will most likely be updated whenever I need new endpoints to be reached.

# Installation
Clone or download the repository
```https://github.com/devharry20/steamapi-wrapper```

# Usage

### For official documentation and api usage visit:
https://partner.steamgames.com/doc/webapi/ISteamUser  
https://partner.steamgames.com/doc/webapi/ISteamUserStats

### ISteamUser
```py
from steamapi.isteamuser import ISteamUser

API_KEY = 'api_key'

isteamuser = ISteamUser(api_key=API_KEY)

isteamuser.get_friend_list(steam_id)
isteamuser.get_player_bans(steam_id)
isteamuser.get_player_summaries(steam_id)
isteamuser.resolve_vanity_url('xxxxxxxxx')
```

### ISteamUserStats
```py
from steamapi.isteamuserstats import ISteamUserStats

API_KEY = 'api_key'

isteamuserstats = ISteamUserStats(api_key=API_KEY)

isteamuserstats.get_global_chievement_percentages_for_app(app_id)
isteamuserstats.get_global_stats_for_game(app_id, count, stats, startdate, enddate)
isteamuserstats.get_number_of_current_players(app_id)
isteamuserstats.get_player_achievements(steam_id, app_id)
isteamuserstats.get_schema_for_game(app_id)
isteamuserstats.get_user_stats_for_game(steam_id, app_id)
```

### Please Note
If you are using the exact same setup as the repository, you may need to add the following into your caller file in order to find the api file
```py
import sys
sys.path.append('../')
from steamapi.api import ISteamUser, ISteamUserStats
```
