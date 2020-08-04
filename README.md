# About
steamapi-wrapper is a simple api wrapper I made to make accessing several steam web api endpoints easier. This will most likely be updated whenever I need new endpoints to be reached. Here are the current supported api endpoints:

* [ISteamUser](https://partner.steamgames.com/doc/webapi/ISteamUser  )
* [ISteamUserStats](https://partner.steamgames.com/doc/webapi/ISteamUserStats  )
* [IPlayerService](https://partner.steamgames.com/doc/webapi/IPlayerService  )
* [ISteamNews](https://partner.steamgames.com/doc/webapi/ISteamNews)
* ICSGOServers_730

# Installation
Clone or download the repository
```https://github.com/devharry20/steamapi-wrapper```

# Api Key
You will need an api key to acces several of the endpoints. Get your key from https://steamcommunity.com/dev/apikey

# Usage
### ISteamUser
```py
from steamapi.api import ISteamUser

isteamuser = ISteamUser(api_key=API_KEY)

isteamuser.get_friend_list(STEAM_ID)
isteamuser.get_player_bans(STEAM_ID)
isteamuser.get_player_summaries(STEAM_ID)
isteamuser.get_user_group_list(STEAM_ID)
isteamuser.resolve_vanity_url('VANITY_ID')
```

### ISteamUserStats
```py
from steamapi.api import ISteamUserStats

isteamuserstats = ISteamUserStats(api_key=API_KEY)

isteamuserstats.get_global_chievement_percentages_for_app(APP_ID)
isteamuserstats.get_global_stats_for_game(APP_ID, COUNT, STATS, STARTDATE, ENDDATE)
isteamuserstats.get_number_of_current_players(APP_ID)
isteamuserstats.get_player_achievements(STEAM_ID, APP_ID)
isteamuserstats.get_schema_for_game(APP_ID)
isteamuserstats.get_user_stats_for_game(STEAM_ID, APP_ID)
```

### IPlayerService
```py
from steamapi.api import IPlayerService

iplayerservice = IPlayerService(api_key=API_KEY)

iplayerservice.get_recently_played_games(STEAM_ID, COUNT)
iplayerservice.get_owned_games(STEAM_ID, ARGS) # args -> list containing "include_appinfo", "include_played_free_games" or both (not required)
iplayerservice.get_steam_level(STEAM_ID)
iplayerservice.get_badges(STEAM_ID)
iplayerservice.get_community_badge_progress(STEAM_ID, BADGE_ID)
iplayerservice.is_playing_shared_game(STEAM_ID, APP_ID)
```

### ISteamNews
```py
from steamapi.api import ISteamNews

isteamnews = ISteamNews(api_key=API_KEY)

isteamnews.get_news_for_app(APP_ID)
```

### Please Note
If you are using the exact same setup as the repository, you may need to add the following into your caller file in order to find the api file
```py
import sys
sys.path.append('..')
from steamapi.api import ...
```
