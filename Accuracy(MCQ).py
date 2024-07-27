import pandas as pd 

#read the csv file 
path = '/Users/shrus/OneDrive/Desktop/RP1/Answers(GPT-3.5 MCQ 100% Masking T5).csv'
df = pd.read_csv(path, encoding = 'ISO-8859-1')

accuracy = []

#checking values 
c1 = "GPT-3.5 Answer"
c2 = "Answer"
for index, row in df.iterrows():
    same = row[c2] == row[c1]
    accuracy.append(same)

#gathering percentage 
tc = len(accuracy)
true = sum(accuracy)
accuracy_percentage = (true/tc)*100 
print(accuracy_percentage)
