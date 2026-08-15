from prompts.base_prompt import BasePrompt

class ReflectionPrompt(BasePrompt):

    def build(self, user_prompt: str) -> str:
        """
        TODO:
        Ask the model to review
        and improve its own answer.

Explain Binary Search.
After generating the answer,
Review your answer.
Find mistakes.
Improve the explanation.
        """
        pass