import requests
import time

username = open("username.txt", "r").read().strip()
counter = 0
delay = float(open("delay.txt", "r").read())
while True:
    time.sleep(delay)
    response = requests.get(f"https://github.com/{username}")
        # if you have the github-profile-views-counter, you can replace the whole link with it
    counter += 1
    print(f"Request #{counter} - Status Code: {response.status_code}")
