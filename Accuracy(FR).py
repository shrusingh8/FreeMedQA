import pandas as pd 
import openai 
import chardet
import csv
import time 

#read the csv file 
path = "/Users/shrus/OneDrive/Desktop/RP1/Answers(GPT-4 FR 100% Masking).csv"
df = pd.read_csv(path, encoding = 'ISO-8859-1')
true = 0
tc = 0

assessments = []
answers = pd.DataFrame(columns=['Answer'])

for index, row in df.iterrows(): 
            openai.api_key = "api_key"
            question = "Are the following two medical statements equivalent in their meaning? Please answer 'yes' or 'no', using just one word:" + " " + row['GPT-4 Answer'] + ";" + " " + row['Answer'] + " Answer, yes or no."
            response = openai.ChatCompletion.create(
                model = "gpt-4-turbo",
                messages = [{"role":"user", 'content': question}],
                temperature = 0
                )
            gpt_answer = response['choices'][0]['message']['content'].lower()
            if "yes" in gpt_answer and "no" not in gpt_answer:
                    tc += 1
                    true += 1
            elif "no" in gpt_answer and "yes" not in gpt_answer:
                    tc += 1
            else:
                print("Error anwering format: ", gpt_answer) 
            print(gpt_answer)
            if gpt_answer is not None:
                new_row =pd.DataFrame([{'Answer': gpt_answer}])
                answers = pd.concat([answers, new_row], ignore_index=True)
                with open("AccuracyAnswers(GPT-4 FR).csv", 'a', newline='', encoding='utf-8') as f:
                    new_row.to_csv(f, header=f.tell() == 0, index=False)
            time.sleep(2.0)

print (true)
percentage = (true/tc)*100
print(percentage)