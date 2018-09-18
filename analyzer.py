import requests
from bs4 import BeautifulSoup
import scipy
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+') #for tokenizing

headlines = []
# For Hindu
r_hindu = requests.get("https://www.thehindu.com/")
soup_hindu = BeautifulSoup(r_hindu.content, 'html.parser')
hindu = soup_hindu.find_all("h2")
for item in hindu[:5]: # to read it better, till 5 because news headlines till 5
    headlines.append(item.text.strip())

# For TOI
r_toi = requests.get("https://timesofindia.indiatimes.com/")
soup_toi = BeautifulSoup(r_toi.content, 'html.parser')
toi = soup_toi.find_all("div", {"class": "top-story"}) 
toi2 = toi[0].find_all("li") 
for item in toi2:
    headlines.append(item.text.strip())

# For Indian Express
r_ie = requests.get("https://indianexpress.com/")
soup_ie = BeautifulSoup(r_ie.content, 'html.parser')
ie = soup_ie.find_all("div", {"class": "top-news"}) 
ie2 = ie[0].find_all("li") 
for item in ie2:
    headlines.append(item.text.strip())

#data visualiation starts here
sia = SIA()
results = []

for line in headlines:
    pol_score = sia.polarity_scores(line)
    pol_score['headline'] = line
    results.append(pol_score)

df = pd.DataFrame.from_records(results)
df['label'] = 0
df.loc[df['compound'] > 0.2, 'label'] = 1
df.loc[df['compound'] < -0.2, 'label'] = -1

#saving data to csv
df2 = df[['headline', 'label']]
df2.to_csv('indian_news_headlines.csv', mode='w', encoding='utf-8', index=False)

#plotting a graph
fig, ax = plt.subplots(figsize=(8, 8))

counts = df.label.value_counts(normalize=True) * 100

sns.barplot(x=counts.index, y=counts, ax=ax)

ax.set_xticklabels(['Negative', 'Neutral', 'Positive'])
ax.set_ylabel("Percentage")

# Positive or negative day title
if (list(df2[df2.label == -1]).count(-1)) < (list(df2[df2.label == 1]).count(1)):
    plt.title("Positive day")
else:
    plt.title("Negative day")

plt.show()

#counting positive-negative words
stop_words = stopwords.words('english')

def process_text(headlines):
    tokens = []
    for line in headlines:
        toks = tokenizer.tokenize(line)
        toks = [t.lower() for t in toks if t.lower() not in stop_words]
        tokens.extend(toks)
    
    return tokens

#positive words
pos_lines = list(df[df.label == 1].headline)

pos_tokens = process_text(pos_lines)
pos_freq = nltk.FreqDist(pos_tokens)

print("Positive words:")
print(pos_freq.most_common())

#negative words
neg_lines = list(df2[df2.label == -1].headline)

neg_tokens = process_text(neg_lines)
neg_freq = nltk.FreqDist(neg_tokens)

print("Negative words")
print(neg_freq.most_common())

