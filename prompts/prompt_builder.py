from prompts.prompt_registry import PROMPT_REGISTRY

class PromptBuilder:

    @staticmethod
    def build(prompt_type,user_prompt):
        prompt=PROMPT_REGISTRY.get(prompt_type)

        if prompt is None:
            raise ValueError("prompt type  not found")
        return prompt.build(user_prompt)