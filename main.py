import requests
import json
from datetime import datetime as dt
import pandas as pd

url = 'https://official-joke-api.appspot.com/random_joke'

joke_data = requests.get(url).text
joke_dict = json.loads(joke_data)

joke_id = joke_dict['id']
joke_type = joke_dict['type']
joke_setup = joke_dict['setup']
joke_punchline = joke_dict['punchline']
joke_datetime_extracted = dt.now()

joke_df = pd.DataFrame(columns=['id', 'type', 'setup', 'punchline', 'datetime_extracted'])
joke_df.loc[len(joke_df)] = [joke_id, joke_type, joke_setup, joke_punchline, joke_datetime_extracted]

print(joke_df)
#print(type(joke_df))
