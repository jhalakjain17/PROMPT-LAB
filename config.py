'''
this file loads the environment variable from .env and injects
 it os path variable
'''
import os 
from dotenv import load_dotenv

load_dotenv()


print('=============injecting the env varible ============')

GROOQ_API_KEY=os.getenv('GROOQ_API_KEY')
MODEL_NAME=os.getenv('MODEL_NAME')
MAX_TOKEN_ALLOWED=os.getenv('MAX_TOKEN_ALLOWED')
MODEL_TEMPERATURE=os.getenv('MODEL_TEMPERATURE')