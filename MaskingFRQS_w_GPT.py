from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering
import torch 
import openai
import random
import pandas as pd
import time 
openai.api_key = "api_key"
answers = pd.DataFrame(columns=['GPT-4 Answer', 'Answer', "Question"])


def mask_tokens(prompt):
    tokens = prompt.split()
    masked_tokens = tokens[:]
    num_to_mask =int(round((1.0*len(tokens)))) 
    token_masked = random.sample(range(len(tokens)), num_to_mask)
    for entry in token_masked: 
            masked_tokens[entry] = "[mask]"
    return " ".join(masked_tokens)

def gpt_answer(question):
    response = openai.ChatCompletion.create(
                model="gpt-4-turbo",
                messages=[{"role": "user", 'content': question}], 
                temperature = 0
            )
    return response['choices'][0]['message']['content']

path = "/Users/shrus/OneDrive/Desktop/RP1/MD.csv"
df = pd.read_csv(path)

for index, row  in df.iterrows():
            data = eval(row['data']) 
            question = mask_tokens(data['Question'])
            options = "; ".join([f"{key}: {value}" for key, value in data["Options"].items()])
            question1 = data['Question'] + " " + options
            question2 = question + " " + " Please answer the question concisely."
            answer = gpt_answer(question2)
            if answer: 
                new_row = pd.DataFrame([{
                'GPT-4 Answer': answer,
                'Answer': data['Correct Answer'],
                "Question": question1
                }])
            answers = pd.concat([answers, new_row], ignore_index=True)
            with open("Answers(GPT-4 FR 100% Masking).csv", 'a', newline='', encoding='utf-8') as f:
                new_row.to_csv(f, header=f.tell() == 0, index=False)
            time.sleep(2.0)