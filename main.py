'''
this is main app
'''

import sys
from agents.chat_agent import invoke_agent

def main():
    prompt= input('enter your question:')
    result=invoke_agent(prompt)
    print('========= response from agent==========')
    print(result)


if __name__=='__main__':
    sys.exit(main())
    
