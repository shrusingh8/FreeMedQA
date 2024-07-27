from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering
import torch 
import random
import pandas as pd
import time 
import requests 

answers = pd.DataFrame(columns=['ML3 70B Answer', 'Answer','Question'])
url = "http://10.189.26.12:30080/model/llama3-70b/v1/chat/completions"
headers = {
    "apiKey": "api_key", # your email ( ALL LOWERCASE ) should go here
    "accept": "application/json",
    "Content-Type": "application/json"
}

def mask_tokens(prompt):
    tokens = prompt.split()
    masked_tokens = tokens[:]
    num_to_mask =int(round((1.0*len(tokens)))) 
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
        print(answer_text)
        return answer_text
    else: 
        print(response.text)

path = "/Users/shrus/OneDrive/Desktop/RP1/MD.csv"
df = pd.read_csv(path, encoding = 'utf-8')

for index, row  in df.iterrows():
                data = eval(row['data'])
                question = mask_tokens(data['Question'])
                options = "; ".join([f"{key}: {value}" for key, value in data["Options"].items()])
                question1 =  question + " " + options + "is: "
                question2 = F"Please answer this question concisely: " + question + " " 
                answer = ML3answer(question2)
                if answer is not None:
                    new_row = pd.DataFrame([{'ML3 70B Answer': answer, 'Answer': data['Correct Answer'], 'Question': question1}])
                    answers = pd.concat([answers, new_row], ignore_index=True)
                    with open("Answers(ML3 70B FR 100% Masking).csv", 'a', newline='', encoding = "utf-8") as f:
                        new_row.to_csv(f, header=f.tell() == 0, index=False)
    