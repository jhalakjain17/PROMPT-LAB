from prompts.base_prompt import BasePrompt

class StepBackPrompt(BasePrompt):

    def build(self, user_prompt: str) -> str:
        """
        TODO:
        Ask the model to first explain
        the broader concept before solving.

        Step-Back Prompting
        ===========X===========
Before explaining Binary Search,
Explain
- What searching is.
- Why searching algorithms exist.
- Why efficiency matters.
Then explain Binary Search.
        """
        pass