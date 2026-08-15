from prompts.base_prompt import BasePrompt

class CritiquePrompt(BasePrompt):

    def build(self, user_prompt: str) -> str:
        """
        TODO:
        Ask the model to critique
        its own solution.

        Generate an explanation.

Then critique your own explanation.

Mention

- Missing information
- Improvements
- Final improved answer
        """

        
        pass