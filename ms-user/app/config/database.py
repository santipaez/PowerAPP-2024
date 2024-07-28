from dotenv import load_dotenv
from pathlib import Path
import os

basedir = os.path.abspath(Path(__file__).parents[1])
load_dotenv(os.path.join(basedir, '.env'))

USER_DB=os.environ.get('DB_USER')
PASS_DB=os.environ.get('DB_PASS')
URL_DB=os.environ.get('DB_URL')
NAME_DB=os.environ.get('DB_NAME')

FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}:5432/{NAME_DB}'