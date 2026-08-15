from prompts.base_prompt import BasePrompt

class IterativeRefinementPrompt(BasePrompt):

    def build(self, user_prompt: str) -> str:
        """
        TODO:
        Ask the model to improve
        its previous response.

Explain Binary Search
Generate an explanation.
Improve it.
Improve it again.
Return the best version.
        """
        pass