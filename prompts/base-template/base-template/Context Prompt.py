from prompts.base_prompt import BasePrompt

class ContextPrompt(BasePrompt):

    def build(self, user_prompt: str) -> str:
        """
        TODO:
        Attach external context
        before the user prompt.

        Context Prompting
        Context

The students already know

- Arrays
- Loops
- Methods

Now explain Binary Search in Java with an example.
        """
        pass