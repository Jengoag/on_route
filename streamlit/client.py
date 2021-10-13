import googlemaps
from datetime import datetime

import os
from dotenv import load_dotenv
load_dotenv()

gkey = os.getenv("GKEY")

gmaps = googlemaps.Client(key=gkey)








