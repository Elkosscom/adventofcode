import requests
uri = f'http://adventofcode.com/{year}/day/{day}/input'
response = requests.get(uri, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})