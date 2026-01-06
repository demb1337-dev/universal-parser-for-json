# open source code for my portfolio, created by demb1337
import requests
import json

# asking user to enter url
url = input("Enter your json url to parse: ")
responce = requests.get(url) # getting responce from url/server
if responce.status_code == 200: # checking if we can reach url/server
    with open("parsed.json", "w", encoding="utf-8") as p: # parsing and saving to parsed.json (if you doesn't have this file program will create it automaticly)
        json.dump(responce.json(), p, indent=4)
    print("Done!")
else: # printing the error if we can't reach json
    print(f'Status code: {responce.status_code} i cannot parse json!')
