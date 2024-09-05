import openai
import random
import pandas as pd
import time 
from tqdm import tqdm

qd = pd.DataFrame(columns=['GPT Assessment', "Actual Question"])
openai.api_key = "api_key"
r = "role"
u = "user"
c = "content"
a = "assistant"
path = "/Users/shrus/OneDrive/Desktop/RP1/All Questions (14965).csv"
df = pd.read_csv(path)
random_qs = []
random_qs_index = []
i = 0 
while i < 20:
    n = random.randint(0,len(df))
    random_qs_index.append(n)
    i+=1
for entry in random_qs_index:
    for index, row  in df.iterrows(): 
        if entry == index:
            random_qs.append(row['Question'])

for qs in random_qs:
    response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages = [{r:a, c:"You are a medical expert at determining if a medical question needs more context to be answered correctly and concisely. You only answer in one word"},
                {r:u, c: "Which of the following is not a category used to classify patients according to the Glasgow Coma Scale?"},
                {r:a, c: "yes"},
                {r:u, c: 'Are bipolar disorders underdiagnosed in patients with depressive episodes?'},
                {r:a, c: "no"},
                {r:u, c: "A 45-year-old construction worker presents to his primary care physician with a painful and swollen wrist joint. A joint aspiration shows crystals, which are shown in the accompanying picture. Which of the following is the most likely diagnosis?"},
                {r:a, c: "yes"},
                {r:u, c: "A 25-year-old G1P0000 presents to her obstetrician’s office for her first prenatal visit. She had a positive pregnancy test 6 weeks ago, and her last period was about two months ago, though at baseline her periods are irregular. Aside from some slight nausea in the mornings, she feels well. Which of the following measurements would provide the most accurate dating of this patient’s pregnancy?"},
                {r:a, c: "no"},
                {r:u, c: "A 37-year-old woman presents to the general medical clinic with a chief complaint of anxiety. She has been having severe anxiety and fatigue for the past seven months. She has difficulty concentrating and her work has suffered, and she has also developed diarrhea from the stress. She doesn't understand why she feels so anxious and is unable to attribute it to anything specific aspect of her life right now. You decide to begin pharmacotherapy. All of the following are suitable mechanisms of drugs that can treat this illness EXCEPT:"},
                {r:a, c: 'yes'},
                {r:u, c: 'The rate of blood lactate accumulation is determined by:'},
                {r:a, c: "no"}, 
                {r:u, c: "The main factors determining success in sport are:"},
                {r:a, c: "yes"},
                {r:u, c: "Male breast cancer is associated with mutations in ___."},
                {r:a, c: "no"}, 
                {r:u, c: 'Which of the following statements about fungi is NOT true?'},
                {r:a, c: "yes"},
                {r:u, c: "Is low serum chloride level a risk factor for cardiovascular mortality?"},
                {r:a, c: "no"},
                {r:u, c: qs}],
                temperature = 0)
    qj = response['choices'][0]['message']['content']
    print(qj)
    new_row = pd.DataFrame([{
                'GPT Assessment': qj,
                'Actual Question': qs
                }])
    qd = pd.concat([qd, new_row], ignore_index=True)
    with open("Question Decisions.csv", 'a', newline='', encoding='utf-8') as f:
        new_row.to_csv(f, header=f.tell() == 0, index=False)
