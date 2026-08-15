'''

this my chat agent

'''
from services.groq_service import GorqService
from config import MODEL_TEMPERATURE

def invoke_agent(prompt:str)->str:
    print('================== i am  chat agent======================')
    print(f'your prompt:{prompt}')
    groq = GorqService()
    response= groq.generate_response(prompt, MODEL_TEMPERATURE)
    return response