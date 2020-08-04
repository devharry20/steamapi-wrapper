## About
steamapi-wrapper is a simple api wrapper I made to make accessing several steam web api endpoints easier. This will most likely be updated whenever I need new endpoints to be reached. Here are the current supported api endpoints:

* [ISteamUser](https://partner.steamgames.com/doc/webapi/ISteamUser  )
* [ISteamUserStats](https://partner.steamgames.com/doc/webapi/ISteamUserStats  )
* [IPlayerService](https://partner.steamgames.com/doc/webapi/IPlayerService  )
* [ISteamNews](https://partner.steamgames.com/doc/webapi/ISteamNews)
* ICSGOServers_730

## Install
Clone or download the repository
```https://github.com/devharry20/steamapi-wrapper```

## Authorisation
You are required to provide an api key to access most endpoints. Get your key from https://steamcommunity.com/dev/apikey

## Usage
### ISteamUser
```py
from steamapi.api import ISteamUser

isteamuser = ISteamUser(api_key=apikey)

isteamuser.get_friend_list(steamid)
isteamuser.get_player_bans(steamid)
isteamuser.get_player_summaries(steamid)
isteamuser.get_user_group_list(steamid)
isteamuser.resolve_vanity_url('vanityid')
```

### ISteamUserStats
```py
from steamapi.api import ISteamUserStats

isteamuserstats = ISteamUserStats(api_key=apikey)

isteamuserstats.get_global_chievement_percentages_for_app(appid)
isteamuserstats.get_global_stats_for_game(appid, count, stats, startdate, enddate)
isteamuserstats.get_number_of_current_players(APP_ID)
isteamuserstats.get_player_achievements(steamid, appid)
isteamuserstats.get_schema_for_game(appid)
isteamuserstats.get_user_stats_for_game(steamid, appid)
```

### IPlayerService
```py
from steamapi.api import IPlayerService

iplayerservice = IPlayerService(api_key=apikey)

iplayerservice.get_recently_played_games(steamid, count)
iplayerservice.get_owned_games(steamid, args) # args -> list containing "include_appinfo", "include_played_free_games" or both (not required)
iplayerservice.get_steam_level(steamid)
iplayerservice.get_badges(steamid)
iplayerservice.get_community_badge_progress(steamid, badgeid)
iplayerservice.is_playing_shared_game(steamid, appid)
```

### ISteamNews
```py
from steamapi.api import ISteamNews

isteamnews = ISteamNews(api_key=apikey)

isteamnews.get_news_for_app(appid)
```

### Please Note
If you are using the exact same setup as the repository, you may need to add the following into your caller file in order to find the api file
```py
import sys
sys.path.append('..')
from steamapi.api import ...
```
