from prompts.base_prompt import BasePrompt

class TreeOfThoughtPrompt(BasePrompt):

    def build(self, user_prompt: str) -> str:
        """
        TODO:
        Explore multiple solution paths.
        Consider multiple ways to explain Binary Search.

Approach 1
Mathematical explanation
Approach 2
Visual explanation
Approach 3
Java implementation

Choose the best explanation.
        """
        pass