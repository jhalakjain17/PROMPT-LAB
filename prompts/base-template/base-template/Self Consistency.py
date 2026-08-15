from prompts.base_prompt import BasePrompt

class SelfConsistencyPrompt(BasePrompt):

    def build(self, user_prompt: str) -> str:
        """
        TODO:
        Generate multiple reasoning paths
        and select the most consistent answer.

        Generate three independent explanations of Binary Search.

Compare them.

Return the most accurate explanation.
        """
        pass