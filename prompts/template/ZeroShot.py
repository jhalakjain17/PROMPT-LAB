from prompts. BasePrompt import BasePrompt

class ZeroShotPrompt(BasePrompt):
    def build(self, user_prompt:str)->str:
        prompt_template=f"""
        TO DO:
        Explain{user_prompt}

"""
        return prompt_template