# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 02:49:15 2024

@author: prath
"""

import os
import openai

# Securely set your API key
openai.api_key = "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"

# Specify the model you want to use
model_name = "gpt-3.5-turbo"  # Replace with the desired model name
'''
# Set up the prompt and completion parameters (optional)
prompt = "Write a poem about a sunflower."
temperature = 0.7  # Adjust as needed
max_tokens = 150  # Adjust as needed

# Call the completions endpoint
response = openai.ChatCompletion.create(
   model=model_name,
   messages=[{"role": "system", "content": prompt}],
   max_tokens=max_tokens,
   n=1,
   stop=None,
   temperature=temperature,
)

# Print the completion
print(response.choices[0].message.content.strip())
'''

def ToxicRemoverList(texts):
    prompt = "change the following prompts by removing all vulgar elements while maintaining the context of each statement and returning each in a list format :"
    
    for t in texts:
        prompt += "\"" + t + "\", "
    prompt = prompt[:-2]
    
    
    temperature = 0.7  # Adjust as needed
    max_tokens = 150  # Adjust as needed
    response = openai.ChatCompletion.create(
       model=model_name,
       messages=[{"role": "system", "content": prompt}],
       max_tokens=max_tokens,
       n=1,
       stop=None,
       temperature=temperature,
    )
    text = response.choices[0].message.content.strip()
    output = text[(text.find("\"") + 1):].split('\n')
    return output
    

def ToxicRemover(text):
    prompt = "change the following prompt by removing all vulgar elements while maintaining the context of the statement: \"{0}\"".format(text)
    temperature = 0.7  # Adjust as needed
    max_tokens = 150  # Adjust as needed

    # Call the completions endpoint
    response = openai.ChatCompletion.create(
       model=model_name,
       messages=[{"role": "system", "content": prompt}],
       max_tokens=max_tokens,
       n=1,
       stop=None,
       temperature=temperature,
    )
    text = response.choices[0].message.content.strip()
    
    return text[(text.find("\"") + 1):]
    