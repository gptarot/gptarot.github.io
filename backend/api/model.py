import openai

async def GPTarot_request(prompt:str) -> str:
    """
    Define a function to choose the valid model and send a request

    Parameters:
        prompt (str): The prompt to send to the chat completion models.

    Returns:
        str: The response generated by the chat completion models.
    """
    model_lists = [
        "gpt-3.5-turbo",
        "gpt-3.5-turbo-0301",
        "gpt-3.5-turbo-0613",
    ]
    
    # Switch openAI chat completion model everytime it is invalid
    for model in model_lists:
        try:
            response = openai.ChatCompletion.create(model=model, messages=[{"role": "user", "content": prompt}])
            return str(response.choices[0].message.content), model
    
        except Exception as e:
            print(e, "\n==> Switching from model {} to model {}".format(model, model_lists[model_lists.index(model) + 1]))
            continue
        
    # If all models are invalid, raise an exception
    return 403, None


def finalCardName(card_dict:dict) -> str:
    """
    Define a function to get the final card name

    Parameters:
        card_dict (dict): A dictionary containing card information.

    Returns:
        str: The name of the card along with its orientation.
    """
    card_name = card_dict['name']
    if card_dict['isUpRight'] == True:
        card_name += ' (Bài xuôi)'
    else:
        card_name += ' (Bài ngược)'
    return card_name


async def generatePrompt(data:dict) -> str:
    """
    Define a function to generate a prompt

    Parameters:
        data (dict): A dictionary containing data for generating the prompt.

    Returns:
        str: The response generated by the GPTarot_request function.
    """
    past_card = finalCardName(data['past-card'])
    present_card = finalCardName(data['present-card'])
    future_card = finalCardName(data['future-card'])
    act = 'Bạn hãy đóng vai trò là Tarot Reader. Tên tôi là {}, sinh ngày {}. '.format(data['name'], data['dob'])
    card_info = f'Giả sử tôi rút được 3 lá bài Tarot là: {past_card}, {present_card}, {future_card}. '
    prompt = act + card_info + f"Hãy trả lời câu hỏi của tôi: {data['question']}? Trả lời bằng giọng văn huyền bí và sâu sắc nhất có thể"
    answer, model = await GPTarot_request(prompt)
    return str(answer), model