
import json
# #
# d = {
#     "name":"alex",
#     "role": "police",
#     "blood": 76,
#     "weapon": "AK47"
# }
#
# alive_players = ["alex","jack","rain"]
#
#
# f= open("game.json","w")
# json.dump(d,f)
# #json.dump(alive_players,f)

#
# f = open("game.json","r")
#
# d= json.load(f)
#
# print(d["weapon"])

import datetime

print(json.dumps(datetime.datetime.now()))