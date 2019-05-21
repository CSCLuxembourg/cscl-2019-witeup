

# before executing this script:
#  $ wget https://raw.githubusercontent.com/cscluxembourg/vestatech/master/challenges/the-missing-piece/rotors.png
#  $ pipx install Stegano
#  $ stegano-lsb reveal -i rotors.png > message
#  $ base64 -d message > rotor

import pickle
import requests
from base64 import b64decode

# Load the Enigma engine
r = requests.get('https://raw.githubusercontent.com/cscluxembourg/vestatech/master/challenges/the-missing-piece/engine')
obj = b64decode(r.content)
engine = pickle.loads(obj)
# A rotor is missing!
print(engine)
# A gentle help is in the doc of the object:
# print(engine.__doc__)


# Load the rotor
rotor_obj = open("rotor", "rb")
rotor = pickle.load(rotor_obj)
rotor_obj.close()

engine.rotor2 = rotor
message = engine.encipher("LegPnldhbNvMebuidswFlndvul")
print("FLAG:")
print(message)



