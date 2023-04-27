
#cleaning text :convert letter into lowerc remove punctuation)
import string
from collections import Counter
import matplotlib.pyplot as plt
import nltk
from nltk import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
text=open('read.txt', encoding='utf-8').read()
low_case=text.lower()
cleaned_text=low_case.translate(str.maketrans('','',string.punctuation))
#tokenizing is having each word in a list
toxenized_words=word_tokenize(cleaned_text,'english')
#stop words
#nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = (stopwords.words('english'))
final_words=[]
# Lemmatization - From plural to single + Base form of a word (example better-> good)

for word in final_words:
    word = WordNetLemmatizer().lemmatize(word)
    final_words.append(word)
# Initialize the Porter Stemmer
stemmer = PorterStemmer()
# Stem each word in the text using the Porter Stemmer
for word in final_words:
    stemmed_words = [stemmer.stem(word) for word in final_words]
    final_words.append(word)

for i in toxenized_words:
    if i not in stop_words:
        final_words.append(i)

#nlp emotions algo: check if word in emtion.txt / open emo file/ loop each line and clear it/ 
# extract word and emo using split/if word present add emo to emo_list /finally count each emotion in emo_list
emotion_list=[]

#clearing text
with open('emotions.txt','r')as file:
    for line in file:
        cleared_line=line.replace('\n','').replace(',','').replace("'",'').strip()
        #word before : is stored in variable word and word after : is stored in variable emotion
        word , emotion= cleared_line.split(':')
        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
w=Counter(emotion_list)
def sentiment_analyse(sentiment_text):
    score=SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg=score['neg']
    pos=score['pos']
    print(score)
    if neg>pos:
        print("negative sentiment :(")
    elif neg<pos:
        print("positive sentiment :)")
    else :
        print('neutral sentiment:|')


sentiment_analyse(cleaned_text)
fig, ax1=plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.xlabel('emotions')
plt.ylabel('emotion intensity')
plt.title('Sentiment Analysis')
plt.savefig('graphe.png')
plt.show()