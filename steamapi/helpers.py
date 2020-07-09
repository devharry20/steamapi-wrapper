import requests


def _apicall(url):
    r = requests.get(url)
    return r.json()

def str_format(*steamids):
    return ', '.join([str(steamid) for steamid in steamids])
