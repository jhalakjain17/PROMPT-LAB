'''
this groq service ,this interface will groq llm via api and will responisble for all type of communication b/w cliient and groq server.
'''

from groq import Groq

from config import GROOQ_API_KEY,MODEL_NAME

class GorqService:
    def __init__(self):
      self.client=Groq(api_key=GROOQ_API_KEY)

    def generate_response(self,prompt,temperature,tokens,role='user'):
        response = self.client.chat.completions.create(
         
            model=MODEL_NAME,
            messages=[
                {
                    'role':role,
                    'content':prompt
                }
            ],
            max_tokens=int(tokens),#STR ->INT
            temperature=float(temperature)
        )    
        return response.choices[0].message.content