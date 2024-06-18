from dotenv import load_dotenv
from pathlib import Path
import os

basedir = os.path.abspath(Path(__file__).parents[2])
load_dotenv(os.path.join(basedir, '.env'))

USER_DB=os.environ.get('USER_DB')
PASS_DB=os.environ.get('PASS_DB')
URL_DB=os.environ.get('URL_DB')
NAME_DB=os.environ.get('NAME_DB')


FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}:5432/{NAME_DB}'