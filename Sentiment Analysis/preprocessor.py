import nltk
import re
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("vader_lexicon")
nltk.download("punkt")
nltk.download("punkt_tab")
sia = SentimentIntensityAnalyzer()
stop_words = stopwords.words('english')
lemmatizer = WordNetLemmatizer()
def process_review(review):
   
    # Convert review into lower case form
    review_lower = review.lower()
    
    #Remove punctation & numbers
    review_no_puncs_nums = re.sub(r'[^a-z\s]',r'', review_lower)
    
    #Convert text into Tokens
    tokens = word_tokenize(review_no_puncs_nums)
    
    #Remove stop words in tokens
    tokens_no_stopwords = [token for token in tokens if token not in stop_words]

    # lemmatization
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens_no_stopwords]

    #Put back the words to form a sentence
    return ' '.join(lemmatized_tokens)

print(process_review("The Product was damaged and not good at all!!!"))