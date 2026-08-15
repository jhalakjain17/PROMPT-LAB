from prompts.base_prompt import BasePrompt

class RolePrompt(BasePrompt):

    def build(self, user_prompt: str) -> str:
        """
        TODO:
        Assign a role such as Teacher, Doctor,
        Software Engineer, Lawyer, etc.

        You are an experienced Java Trainer with 20 years of teaching experience.

Explain Binary Search in Java with an example suitable for beginners.

= 5. Persona Prompting ====

You are James Gosling, the creator of Java.

Explain Binary Search in Java with an example.
        """
        pass