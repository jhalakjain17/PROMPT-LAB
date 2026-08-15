from prompts.base_prompt import BasePrompt

class DelimiterPrompt(BasePrompt):

    def build(self, user_prompt: str) -> str:
        """
        TODO:
        Wrap user input
        using delimiters.


        Use the following user request.

<<<

Explain Binary Search in Java with an example.

>>>

Answer only using the content inside the delimiters.
        """
        pass