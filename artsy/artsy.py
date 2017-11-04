import requests
import json

# Программа выводит в файл имена первых десяти художников с artsy.com
client_id = 'c106a77ee4dda462f463'
client_secret = '3aa6adfa54057aa5c4341152482a97ee'

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

j = json.loads(r.text)
token = j["token"]
headers = {"X-Xapp-Token": token}
template = 'https://api.artsy.net/api/artists/{}'
r = requests.get(template, headers=headers)
j = json.loads(r.text)
template = j['_links']['next']['href']
f = open('artists.txt', 'w')
for i in range (0,10):
    r = requests.get(template, headers=headers)
    j = json.loads(r.text)
    name = j['_embedded']['artists'][0]['name']
    template = j['_links']['next']['href']
    f.write(name + '\n')
f.close()
