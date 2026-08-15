from abc import ABC,abstractmethod
class BasePrompt(ABC):

    @abstractmethod 
    def build(self,user_prompt:str)->str:
        pass