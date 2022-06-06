""""
Copyright © bastientherond 2022 - https://github.com/bastientherond

Version: 1.0
"""

import sys
import disnake

import json
import os 

if not os.path.isfile("config/config.json"):
    sys.exit("Le fichier de config n'est pas crée/trouvée.\nMerci de vérifier l'intégrité du fichier dans le dossier config !")
else:
    with open("config/config.json") as config_file:
        config = json.load(config_file)
