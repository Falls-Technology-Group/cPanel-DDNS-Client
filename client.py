from time import sleep
import requests
from configparser import ConfigParser

settings_file_location = 'config.ini'

print("Welcome to the cPanel DDNS Updater Tool")

# Ask to Load Settings
config = ConfigParser()
config.read(settings_file_location)
try:
    if config.get('main', 'url') != "":
        load = input("Settings found... Would you like to load? (Y/y - Yes | N/n - No)")

    if load == "Y" or load == "y":
        print("Loading Settings...")
        url = config.get('main', 'url')
    elif load == "N" or load == "n":
        print("Skipping load.")
except:
    print("No settings file found. Skipping load.")

# Retrieve User Preferences if No Settings / Load Declined
if url == "":
    url = input("Input your DDNS URL from cPanel: ")

    # Ask User if they want to save
    save = input("Should we save this URL? (Y/y - Yes | N/n - No): ")
    if save == "Y" or save == "y":
        print("Saving before moving on.")
        config.read(settings_file_location)
        try:
            config.add_section('main')
        except:
            print("Setting Found - Updating")
        config.set('main', 'url', url)
        with open('config.ini', 'w') as f:
            config.write(f)

    elif save == "N" or save == "n":
        print("Moving on without saving.")

# Run Loop
while 0 == 0:
    response = requests.get(url)
    print(response.text)
    print("DDNS Updated. To Terminate, press CTRL + C")
    print("Refreshing in 5 Minutes")
    sleep(300)