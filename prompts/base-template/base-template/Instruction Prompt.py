from prompts.base_prompt import BasePrompt

class InstructionPrompt(BasePrompt):

    def build(self, user_prompt: str) -> str:
        """
        TODO:
        Convert the input into
        an instruction-following prompt.


        6. Instruction Prompting
        Follow these instructions carefully.

1. Explain Binary Search.
2. Show Java code.
3. Explain every line.
4. Give Time Complexity.
5. Give Space Complexity.
6. Mention advantages.
7. Mention disadvantages.
        """
        pass