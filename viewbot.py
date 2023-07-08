import requests

username = open("username.txt", "r").read()
counter = 0

while True:
    response = requests.get("https://camo.githubusercontent.com/c466c0d2b17918394de41a0d1398e322d166ec356e5e72a7e91b0c455cf3c1a8/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d4a75737441503161796572")
    counter += 1
    print(f"Request #{counter} - Status Code: {response.status_code}")
