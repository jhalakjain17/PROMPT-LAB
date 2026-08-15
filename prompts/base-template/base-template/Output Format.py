from prompts.base_prompt import BasePrompt

class OutputFormatPrompt(BasePrompt):

    def build(self, user_prompt: str) -> str:
        """
        TODO:
        Force JSON, XML,
        Markdown, Table, etc.


Explain Binary Search.
Return the answer in Markdown.
# Definition
# Algorithm
# Java Code
# Complexity
# Example

==== JSON Prompting  === 
Return the response as JSON.

{
  "definition":"",
  "algorithm":"",
  "java_code":"",
  "complexity":"",
  "advantages":[
  ],
  "disadvantages":[
  ]
}

=========== XML Prompting =========
Return the response in XML.
<BinarySearch>
    <Definition></Definition>
    <Algorithm></Algorithm>
    <JavaCode></JavaCode>
</BinarySearch>

Explain Binary Search.
Return the answer as a Markdown table.
        """
        pass