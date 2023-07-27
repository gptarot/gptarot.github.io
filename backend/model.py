import json
import openai
import os
import shutil
import time

# Load API key, generate API key in https://beta.openai.com/account/api-keys
# Then use command echo "OPENAI_API_KEY=<your key>" > .env
# Then use command export $(xargs < .env) to export the key
openai.api_key = os.getenv("OPENAI_API_KEY")

#Example Continuous Completion
""" 
{"role": "system", "content": "Assistant is an intelligent chatbot designed to help users answer their tax related questions. "},
{"role": "user", "content": "When do I need to file my taxes by?"},
{"role": "assistant", "content": "In 2023, you will need to file your taxes by April 18th. The date falls after the usual April 15th deadline because April 15th falls on a Saturday in 2023. For more details, see https://www.irs.gov/filing/individuals/when-to-file."},
{"role": "user", "content": "How can I check the status of my tax refund?"},
{"role": "assistant", "content": "You can check the status of your tax refund by visiting https://www.irs.gov/refunds"},
{"role": "user", "content": <question>},
"""

def GPTarot_request(question:str) -> str:
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": question}])
    return str(response.choices[0].message.content)

question = "Act as a Tarot Reader. Suppose that I have 3 cards: Queen of Pentacles, The Lovers, The Emperor. Answer my question: What is my future?"
start = time.time()
print(GPTarot_request(question))
time = time.time() - start
print("Time: ", time)