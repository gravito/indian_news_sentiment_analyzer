# Indian News Sentiment Analyzer
This program first scraps news headlines from popular Indian news websites, and then, using Vader Sentiment analyzer, plots a graph on whether today is going to be a positive day or negative day. 

### LIBRARIES USED:
| Library | Used for |
| ------ | ------ |
| [Pandas](https://pandas.pydata.org/) | For creating dataframes |
| [Beautiful soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) | For parsing HTML data |
| [matplotlib](https://matplotlib.org/) | For plotting graph |
| [Seaborn](https://seaborn.pydata.org/) | For plotting graph |
| [NLTK](https://www.nltk.org/) | For processing Text data |
| [nltk.sentiment.vader](https://github.com/cjhutto/vaderSentiment) | Part of NLTK, the vader sentiment analyzer is the main engine for analyzing news headlines |
| [nltk.corpus](https://gist.github.com/sebleier/554280) | Part of NLTK, to remove frequently occured words like "is", "the" etc. |
| [nltk.tokenize](https://www.nltk.org/api/nltk.tokenize.html) | Part of NLTK, to tokenize headlines |


### INPUT FORMAT:

Data scraping of headlines is done from three most popular indian news websites:
* [The Hindu](https://www.thehindu.com/)
* [Times of India](https://timesofindia.indiatimes.com/)
* [Indian Express](https://indianexpress.com/)

As of now, the websites are hardcoded in the code. So simply run the python file. It might ask for download of nltk packages, which can be done manually on python terminal by following command:
``` 
import nltk
nltk.download("stopwords")
```
In future versions, will use a CSV file, and maybe use RSS feed to get even more data!


### OUTPUT FORMAT:
It will first generate a plot based on frequency of positive or negative words encountered. It will then generate a CSV file, which keeps track of the headlines and the associated label. Furthermore, it will print most frequently encountered positive and negative words.

### ASSUMPTIONS:
```
df.loc[df['compound'] > 0.2, 'label'] = 1
df.loc[df['compound'] < -0.2, 'label'] = -1
```

The above piece of code is assigning positive label for any news headlines with >0.2 score and vice versa. This creates a lot of neutral words which are hung in between. Feel free to edit this for varying results.

### REFERENCES:
Due to paucity of time, did some cut copy paste, find and replace, the engineer's style ;). Very useful references:
* https://www.learndatasci.com/tutorials/sentiment-analysis-reddit-headlines-pythons-nltk/
* https://www.dataquest.io/blog/web-scraping-tutorial-python/


