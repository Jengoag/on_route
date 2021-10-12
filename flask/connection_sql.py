import os
from dotenv import load_dotenv
load_dotenv()

user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")

from sqlalchemy import create_engine

postgres_url = f'postgresql+psycopg2://{user}:{password}@127.0.0.1:5432' #### puerto

engine = create_engine(f'{postgres_url}/routes')
db = engine.connect()

