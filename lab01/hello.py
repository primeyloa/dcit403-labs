import os
from dotenv import load_dotenv
from litellm import completion
 
load_dotenv()
MODEL = os.getenv("LLM_MODEL")
 
resp = completion(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "In one sentence, what is an intelligent agent?"},
    ],
    temperature=0,
)
print(resp.choices[0].message.content)
print(resp.usage)