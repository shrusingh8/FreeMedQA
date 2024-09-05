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
while i < 21:
    n = random.randint(0,len(df))
    random_qs_index.append(n)
    i+=1
for entry in random_qs_index:
    for index, row  in df.iterrows(): 
        if entry == index:
            random_qs.append(row['Question'])

for qs in random_qs:
    response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages = [{r:a, c:"You are a medical expert at determining if a medical question needs more context to be answered correctly and concisely. Your judgement is based solely off of the context of the question and not by the phrasing. You only answer in one word"},
                {r:u, c: "Which of the following is not a category used to classify patients according to the Glasgow Coma Scale?"},
                {r:a, c: "yes"},
                {r:u, c: 'A 68-year old woman presents with recurring headaches and pain while combing her hair. Her past medical history is significant for hypertension, glaucoma and chronic deep vein thrombosis in her right leg. Current medication includes rivaroxaban, latanoprost, and benazepril. Her vitals include: blood pressure 130/82 mm Hg, pulse 74/min, respiratory rate 14/min, temperature 36.6℃ (97.9℉). Physical examination reveals neck stiffness and difficulty standing up due to pain in the lower limbs. Strength is 5 out of 5 in the upper and lower extremities bilaterally. Which of the following is the next best step in the management of this patient?'},
                {r:a, c: "no"},
                {r:u, c: "A 45-year-old construction worker presents to his primary care physician with a painful and swollen wrist joint. A joint aspiration shows crystals, which are shown in the accompanying picture. Which of the following is the most likely diagnosis?"},
                {r:a, c: "yes"},
                {r:u, c: "A patient suffering from Graves' disease is given thiocyanate by his physician. Thiocyanate helps in the treatment of Graves' disease by:"},
                {r:a, c: "no"},
                {r:u, c: "A 37-year-old woman presents to the general medical clinic with a chief complaint of anxiety. She has been having severe anxiety and fatigue for the past seven months. She has difficulty concentrating and her work has suffered, and she has also developed diarrhea from the stress. She doesn't understand why she feels so anxious and is unable to attribute it to anything specific aspect of her life right now. You decide to begin pharmacotherapy. All of the following are suitable mechanisms of drugs that can treat this illness EXCEPT:"},
                {r:a, c: 'yes'},
                {r:u, c: 'A 21-year-old woman presents with palpitations and anxiety. She had a recent outpatient ECG that was suggestive of supraventricular tachycardia, but her previous physician failed to find any underlying disease. No other significant past medical history. Her vital signs include blood pressure 102/65 mm Hg, pulse 120/min, respiratory rate 17/min, and temperature 36.5℃ (97.7℉). Electrophysiological studies reveal an atrioventricular nodal reentrant tachycardia. The patient refuses an ablation procedure so it is decided to perform synchronized cardioversion with consequent ongoing management with verapamil. Which of the following ECG features should be monitored in this patient during treatment?'},
                {r:a, c: "no"}, 
                {r:u, c: "The main factors determining success in sport are:"},
                {r:a, c: "yes"},
                {r:u, c: "A group of scientists is conducting an experiment on the human cells involved in the immune response. They genetically modify B cells so they do not express the cluster of differentiation 21 (CD21) on their cell surfaces. The pathogenesis of which of the following organisms would most likely be affected by this genetic modification?"},
                {r:a, c: "no"}, 
                {r:u, c: 'A 13-month-old female infant is brought to the pediatrician by her stepfather for irritability. He states that his daughter was crying through the night last night, but she didn’t want to eat and was inconsolable. This morning, she felt warm. The father also notes that she had dark, strong smelling urine on the last diaper change. The patient’s temperature is 101°F (38.3°C), blood pressure is 100/72 mmHg, pulse is 128/min, and respirations are 31/min with an oxygen saturation of 98% on room air. A urinalysis is obtained by catheterization, with results shown below: Urine: Protein: Negative, Glucose: Negative, White blood cell (WBC) count: 25/hpf, Bacteria: Many, Leukocyte esterase: Positive, Nitrites: Positive; In addition to antibiotics, which of the following should be part of the management of this patient’s condition?'},
                {r:a, c: "yes"},
                {r:u, c: "A 74-year-old woman with a past medical history of hypertension, peripheral artery disease, and migraine headaches presents to the emergency department with a two hour history of severe abdominal pain. The patient cannot recall any similar episodes, although she notes occasional abdominal discomfort after eating. She describes the pain as sharp periumbilcal pain. She denies recent illness, fever, chills, nausea, vomiting, or diarrhea. Her last normal bowel movement was yesterday evening. Her temperature is 37.1°C (98.8°F), pulse is 110/min, blood pressure is 140/80 mmHg, and respirations are 20/min. On exam, the patient is grimacing and appears to be in significant discomfort. Heart and lung exams are within normal limits. The patient’s abdomen is soft and non-distended with diffuse periumbilical pain on palpation. There is no rebound tenderness or guarding, and bowel sounds are present. The rest of the exam is unremarkable. Labs in the emergency room show: Serum: Na+: 144 mEq/L, Cl-: 105 mEq/L, K+: 3.7 mEq/L, HCO3-: 20 mEq/L, BUN: 15 mg/dL, Glucose: 99 mg/dL, Creatinine: 1.2 mg/dL, Ca2+: 10.7 mg/dL, Phosphorus: 5.2 mg/dL, Lactate: 7.0 mmol/L, Amylase: 240 U/L, Hemoglobin: 13.4 g/dL, Hematocrit: 35%, Leukocyte count: 12,100 cells/mm^3 with normal differential, Platelet count: 405,000/mm^3; What is the next best step in diagnosis?"},
                {r:a, c: "no"},
                {r:u, c: qs}],
                temperature = 0)
    qj = response['choices'][0]['message']['content']
    print("GPT Response: " + qj)
    print()
    print ("Question: " + qs)
    print()
    
    new_row = pd.DataFrame([{
                    'GPT Assessment': qj,
                    'Actual Question': qs
                    }])
    qd = pd.concat([qd, new_row], ignore_index=True)
    with open("Question Decisions.csv", 'a', newline='', encoding='utf-8') as f:
        new_row.to_csv(f, header=f.tell() == 0, index=False)
