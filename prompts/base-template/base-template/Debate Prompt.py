from prompts.base_prompt import BasePrompt

class DebatePrompt(BasePrompt):

    def build(self, user_prompt: str) -> str:
        """
        TODO:
        Generate arguments from
        multiple viewpoints.

        Two Java experts discuss Binary Search.

Expert A explains advantages.

Expert B explains disadvantages.

Finally provide the balanced conclusion.
        """
        pass