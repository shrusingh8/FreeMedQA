import openai
import random
import pandas as pd
import time 
from tqdm import tqdm

qd = pd.DataFrame(columns=['GPT Assessment', "Actual Question"])
openai.api_key = "api-key"
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
                {r:u, c: "'A 48-year-old man with a history of diabetes mellitus presents to his primary care physician with lethargy, joint pain, and impotence. Lab evaluation is notable for a ferritin of 1400 ug/L (nl <300 ug/L), increased total iron, increased transferrin saturation, and decreased total iron binding capacity. All of the following are true regarding this patient's condition EXCEPT:'"},
                {r:a, c: "yes"},
                {r:u, c: "A 25-year-old G1P0000 presents to her obstetrician’s office for her first prenatal visit. She had a positive pregnancy test 6 weeks ago, and her last period was about two months ago, though at baseline her periods are irregular. Aside from some slight nausea in the mornings, she feels well. Which of the following measurements would provide the most accurate dating of this patient’s pregnancy?"},
                {r:a, c: "no"},
                {r:u, c: "A 37-year-old woman presents to the general medical clinic with a chief complaint of anxiety. She has been having severe anxiety and fatigue for the past seven months. She has difficulty concentrating and her work has suffered, and she has also developed diarrhea from the stress. She doesn't understand why she feels so anxious and is unable to attribute it to anything specific aspect of her life right now. You decide to begin pharmacotherapy. All of the following are suitable mechanisms of drugs that can treat this illness EXCEPT:"},
                {r:a, c: 'yes'},
                {r:u, c: '"The rate of blood lactate accumulation is determined by:"'},
                {r:a, c: "no"}, 
                {r:u, c: "Which of the following is not a true statement?"},
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

'''questions = pd.DataFrame(columns=['Question', 'Answer Option', "Answer Statement", "Options"])
openai.api_key = "api-key"
r = "role"
u = "user"
c = "content"
a = "assistant"
path = "/Users/shrus/OneDrive/Desktop/RP1/All Questions (14965).csv"
df = pd.read_csv(path)

for index, row  in tqdm(df.iterrows(), total = len(df)): 
    response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages = [{r:a, c:"You are a medical expert at determining if a medical question needs more context to be answered correctly and concisely. You only answer in one word"},
                {r:u, c: "Which of the following is not a category used to classify patients according to the Glasgow Coma Scale?"},
                {r:a, c: "yes"},
                {r:u, c: 'Quality of life in lung cancer patients: does socioeconomic status matter?'},
                {r:a, c: "no"},
                {r:u, c: "'A 48-year-old man with a history of diabetes mellitus presents to his primary care physician with lethargy, joint pain, and impotence. Lab evaluation is notable for a ferritin of 1400 ug/L (nl <300 ug/L), increased total iron, increased transferrin saturation, and decreased total iron binding capacity. All of the following are true regarding this patient's condition EXCEPT:'"},
                {r:a, c: "yes"},
                {r:u, c: "A 25-year-old G1P0000 presents to her obstetrician’s office for her first prenatal visit. She had a positive pregnancy test 6 weeks ago, and her last period was about two months ago, though at baseline her periods are irregular. Aside from some slight nausea in the mornings, she feels well. Which of the following measurements would provide the most accurate dating of this patient’s pregnancy?"},
                {r:a, c: "no"},
                {r:u, c: "A 37-year-old woman presents to the general medical clinic with a chief complaint of anxiety. She has been having severe anxiety and fatigue for the past seven months. She has difficulty concentrating and her work has suffered, and she has also developed diarrhea from the stress. She doesn't understand why she feels so anxious and is unable to attribute it to anything specific aspect of her life right now. You decide to begin pharmacotherapy. All of the following are suitable mechanisms of drugs that can treat this illness EXCEPT:"},
                {r:a, c: 'yes'},
                {r:u, c: '"A 57-year-old female visits her primary care physician with 2+ pitting edema in her legs. She takes no medications and does not use alcohol, tobacco, or illicit drugs. 4.5 grams of protein are collected during 24-hour urine excretion. A kidney biopsy is obtained. Examination with light microscopy shows diffuse thickening of the glomerular basement membrane. Electron microscopy shows subepithelial spike and dome deposits. Which of the following is the most likely diagnosis:?'},
                {r:a, c: "no"}, 
                {r:u, c: "Which of the following is not a true statement?"},
                {r:a, c: "yes"},
                {r:u, c: 'Is human cytomegalovirus infection associated with hypertension?'},
                {r:a, c: "no"}, 
                {r:u, c: 'Which of the following statements about fungi is NOT true?'},
                {r:a, c: "yes"},
                {r:u, c: "Study X examined the relationship between coffee consumption and lung cancer. The authors of Study X retrospectively reviewed patients' reported coffee consumption and found that drinking greater than 6 cups of coffee per day was associated with an increased risk of developing lung cancer. However, Study X was criticized by the authors of Study Y. Study Y showed that increased coffee consumption was associated with smoking. What type of bias affected Study X, and what study design is geared to reduce the chance of that bias?"},
                {r:a, c: "no"},
                {r:u, c: qs}],
                temperature = 0)
    qj = response['choices'][0]['message']['content']
    if "yes" in qj.lower():
        new_row = pd.DataFrame([{
                'Question': row['Question'],
                'Answer Option': row['Answer Option'],
                "Answer Statement": row['Answer Statement'], 
                "Options": row['Options']
                }])
        questions = pd.concat([questions, new_row], ignore_index=True)
        with open("Questions That Need Reformatted Answers.csv", 'a', newline='', encoding='utf-8') as f:
            new_row.to_csv(f, header=f.tell() == 0, index=False)
    elif "no" in qj.lower():
        new_row = pd.DataFrame([{
                'Question': row['Question'],
                'Answer Option': row['Answer Option'],
                "Answer Statement": row['Answer Statement'], 
                "Options": row['Options']
                }])
        questions = pd.concat([questions, new_row], ignore_index=True)
        with open("Questions Ready To Be Converted Into FRQs.csv", 'a', newline='', encoding='utf-8') as f:
            new_row.to_csv(f, header=f.tell() == 0, index=False)
'''
