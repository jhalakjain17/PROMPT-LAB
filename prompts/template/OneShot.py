from prompts. BasePrompt import BasePrompt

class OneShotPrompt(BasePrompt):
    def build(self, user_prompt:str)->str:
        prompt_template=f"""
        TO DO:
        ad one  demontration ex. before the user prompt 
        question:
        explain learn search in java

        anser:
        linear search check each elemt ine by one until the target
         element is found

         question:
         explain{user_prompt}

"""
        return prompt_template