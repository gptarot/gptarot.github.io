import poe, os

async def GPTarot_request(prompt:str) -> str:
    client = poe.Client(os.environ["POE_TOKEN"])
    for result in client.send_message("chinchilla", prompt): # chinchilla is the name of the engine ChatGPT3.5-Turbo
        pass
    return result["text"]

def finalCardName(card_dict:dict) -> str:
    card_name = card_dict['name']
    if card_dict['isUpRight'] == True:
        card_name += ' (Bài xuôi)'
    else:
        card_name += ' (Bài ngược)'
    return card_name

async def generatePrompt(data:dict) -> str:
    past_card = finalCardName(data['past-card'])
    present_card = finalCardName(data['present-card'])
    future_card = finalCardName(data['future-card'])
    act = 'Bạn hãy đóng vai trò là Tarot Reader. Tên tôi là {}, sinh ngày {}. '.format(data['name'], data['dob'])
    card_info = f'Giả sử tôi rút được 3 lá bài Tarot là: {past_card}, {present_card}, {future_card}. '
    prompt = act + card_info + f"Hãy trả lời câu hỏi của tôi: {data['question']}? Trả lời bằng giọng văn huyền bí và sâu sắc nhất có thể"
    answer = await GPTarot_request(prompt)
    return answer
