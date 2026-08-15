from prompts.base_prompt import BasePrompt

class FewShotPrompt(BasePrompt):

    def build(self, user_prompt: str) -> str:
        """
        TODO:
        Add multiple examples before the user prompt.
        Example 1

Question:
Explain Array.

Answer:
An Array stores elements of the same data type.

--------------------------------

Example 2

Question:
Explain Linear Search.

Answer:
Linear Search checks every element sequentially.

--------------------------------

Example 3

Question:
Explain Bubble Sort.

Answer:
Bubble Sort repeatedly swaps adjacent elements.

--------------------------------

Now answer:

Question:
Explain Binary Search in Java with an example.
        """
        pass