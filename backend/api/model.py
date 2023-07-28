import json
import openai
import os
import shutil
import time

# Load API key, generate API key in https://beta.openai.com/account/api-keys
# Then use command echo "OPENAI_API_KEY=<your key>" > .env
# Then use command export $(xargs < .env) to export the key

async def GPTarot_request(prompt:str) -> str:
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    return str(response.choices[0].message.content)

def finalCardName(card_dict:dict) -> str:
    card_name = card_dict['name']
    if card_dict['isUpRight'] == True:
        card_name += ' (Bài xuôi)'
    else:
        card_name += ' (Bài ngược)'
    return card_name

async def generatePrompt(prompt_path:str) -> str:
    # f = open(prompt_path)
    # data = json.load(f)
    # f.close()
    data = {
        "name": "Bùi Quang Thắng",
        "dob": "05/06/2003",
        "question": "Mùa hè này tôi có việc thực tập hay không",
        "past-card": {
            "name" : "Chariot" ,
            "isUpRight" : False
        },
        "present-card": {
            "name" : "The Fool" ,
            "isUpRight" : True
        },
        "future-card": {
            "name" : "The Magician" ,
            "isUpRight" : True
        }
    }
    past_card = finalCardName(data['past-card'])
    present_card = finalCardName(data['present-card'])
    future_card = finalCardName(data['future-card'])
    act = 'Bạn hãy đóng vai trò như một Tarot Reader. Tên tôi là {}, sinh ngày {}. '.format(data['name'], data['dob'])
    card_info = f'Giả sử tôi có 3 lá bài Tarot là: {past_card}, {present_card}, {future_card}. '
    prompt = act + card_info + f"Hãy trả lời câu hỏi của tôi: {data['question']}? Trả lời bằng giọng văn ma mị và sâu sắc nhất có thể"
    answer = await GPTarot_request(prompt)
    return answer

"""
f = open('prompt.json')
data = json.load(f)
f.close()
past_card = finalCardName(data['past-card'])
present_card = finalCardName(data['present-card'])
future_card = finalCardName(data['future-card'])

act = 'Bạn hãy đóng vai trò như một Tarot Reader. Tên tôi là {}, sinh ngày {}. '.format(data['name'], data['dob'])
card_info = f'Giả sử tôi có 3 lá bài Tarot là: {past_card}, {present_card}, {future_card}. '
prompt = act + card_info + f"Hãy trả lời câu hỏi của tôi: {data['question']}? Hãy xưng hô cậu-tớ và trả lời bằng Tiêng Việt sâu sắc nhất có thể."
print("Prompt: ", prompt)
print("Answer: ")
start = time.time()
print(GPTarot_request(prompt))
time = time.time() - start
print("Processing Time: ", time)
"""