from prompts.base_prompt import BasePrompt

class ChainOfThoughtPrompt(BasePrompt):

    def build(self, user_prompt: str) -> str:
        """
        TODO:
        Encourage the model to reason step by step.

        Context

The students already know

- Arrays
- Loops
- Methods

Now explain Binary Search in Java with an example.
        """
        pass