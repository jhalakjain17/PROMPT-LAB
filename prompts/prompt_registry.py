from prompts.template.ZeroShot import ZeroShotPrompt
from prompts.template.OneShot import OneShotPrompt

PROMPT_REGISTRY={

    "zero_shot":ZeroShotPrompt(),
    "one_shot":OneShotPrompt()

}