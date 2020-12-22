import requests
import json
from lyrics_api import *

class colors:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

while True:
    print()
    print(colors.HEADER + colors.BOLD + "Welcome to the LyricCent explorer." + colors.ENDC)
    print()
    print(colors.WARNING + "Menu Options" + colors.ENDC)
    print("1 - Search for the lyrics of a song.")
    print("0 - Exit")
    print()

    choice = input(colors.BOLD + "> " + colors.ENDC)
    
    print()

    if choice == '0':
        break
    if choice == '1':
        print(colors.BOLD + "What's the name of the artist?" + colors.ENDC)
        artist_name = input(colors.BOLD + "> " + colors.ENDC)
        print(colors.BOLD + "What's the name of the track?" + colors.ENDC)
        track_name = input(colors.BOLD + "> " + colors.ENDC)
        print()
        api_call = base_url + lyrics_matcher + format_url + artist_search_parameter + artist_name + track_search_parameter + track_name + api_key
        # Call the API
        request = requests.get(api_call)
        data = request.json()
        data = data['message']['body']
        print(colors.BOLD + colors.OKGREEN  + artist_name.title() + " - " + track_name.title() + colors.ENDC)
        print()
        print(data['lyrics']['lyrics_body'])

    print()
    print("Again? (Y/N)")
    again = input("> ")
    if again == 'n' or again == 'N':
        break
