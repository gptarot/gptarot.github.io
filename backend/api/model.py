import openai, poe, os

# Define a function to send request to POE
async def POE_request(prompt:str) -> str:
    poe_client = poe.Client(os.environ.get('POE_TOKEN'))
    for chunk in poe_client.send_message("chinchilla", prompt, timeout=120):
        pass
    del poe_client
    return (chunk["text"])

# Define a function to choose the valid model and send
async def GPTarot_request(prompt:str) -> str:
    model_lists = [
        "gpt-3.5-turbo",
        "gpt-3.5-turbo-0301",
        "gpt-3.5-turbo-0613",
        "poe-gpt-3.5-turbo",
    ]
    
    # Switch openAI chat completion model everytime it is invalid
    for model in model_lists:
        try:
            if model_lists.index(model) != 3:
                response = openai.ChatCompletion.create(model=model, messages=[{"role": "user", "content": prompt}])
                return str(response.choices[0].message.content)
            
            elif model_lists.index(model) == 3:
                response = await POE_request(prompt)
                return response
    
        except Exception as e:
            print(e, "\n==> Switching from model {} to model {}".format(model, model_lists[model_lists.index(model) + 1]))
            continue
        
    # If all models are invalid, raise an exception
    return 403

# Define a function to get the final card name
def finalCardName(card_dict:dict) -> str:
    card_name = card_dict['name']
    if card_dict['isUpRight'] == True:
        card_name += ' (Bài xuôi)'
    else:
        card_name += ' (Bài ngược)'
    return card_name

# Define a function to generate prompt
async def generatePrompt(data:dict) -> str:
    past_card = finalCardName(data['past-card'])
    present_card = finalCardName(data['present-card'])
    future_card = finalCardName(data['future-card'])
    act = 'Bạn hãy đóng vai trò là Tarot Reader. Tên tôi là {}, sinh ngày {}. '.format(data['name'], data['dob'])
    card_info = f'Giả sử tôi rút được 3 lá bài Tarot là: {past_card}, {present_card}, {future_card}. '
    prompt = act + card_info + f"Hãy trả lời câu hỏi của tôi: {data['question']}? Trả lời bằng giọng văn huyền bí và sâu sắc nhất có thể"
    answer = await GPTarot_request(prompt)
    return str(answer)