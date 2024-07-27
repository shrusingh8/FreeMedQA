import random
import re 
import pandas as pd
import time
import requests

url = "http://10.189.26.12:30080/model/llama3-70b/v1/chat/completions"
headers = {
    "apiKey": "api_key",  # your email (ALL LOWERCASE) should go here
    "accept": "application/json",
    "Content-Type": "application/json"
}

def mask_tokens(prompt):
    tokens = prompt.split()
    num_to_mask = int(round(1.0 * len(tokens)))  
    masked_tokens = tokens[:]
    token_masked = random.sample(range(len(tokens)), num_to_mask)
    for entry in token_masked:
        masked_tokens[entry] = "[mask]"
    return " ".join(masked_tokens)

def ML3answer(question):
    messages = [{"role": "user", "content": question}]
    data = {
        "model": "llama3-70b-chat",
        "messages": messages,
        "max_tokens": 50,
        "top_p": 1,
        "n": 1,
        "stream": False,
        "frequency_penalty": 0.0
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        answer_text = response.json()['choices'][0]['message']['content'].strip()
        match = re.search(r'\b[A-D]\b', answer_text)
        while match == None: 
            answer_text = ML3answer(question)
            match = re.search(r'\b[A-D]\b', answer_text)
        answer = match.group() 
        return answer

path = "/Users/shrus/OneDrive/Desktop/RP1/MD.csv"
df = pd.read_csv(path)

answers = pd.DataFrame(columns=['ML3 70B Answer', 'Answer'])

for index, row in df.iterrows():
        data = eval(row['data'])
        question = mask_tokens(data['Question'])
        options = "; ".join([f"{key}: {value}" for key, value in data["Options"].items()])
        question = F"Pick an option- A, B, C or D: " + question + " " + options + "I only want a single character response."
        answer = ML3answer(question)
        if answer is not None:
            new_row = pd.DataFrame([{'ML3 70B Answer': answer, 'Answer': data['Correct Option']}])
            answers = pd.concat([answers, new_row], ignore_index=True)
            with open("Answers(ML3 70B MCQ 100% Masking).csv", 'a', newline='') as f:
                new_row.to_csv(f, header=f.tell() == 0, index=False)
                time.sleep(1)
        time.sleep(0.2)