# import tools
from nltk.tokenize import word_tokenize, PunktSentenceTokenizer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, RegexpParser
# regex
import re

# function to tokenize by word and sentence
def word_sentence_tokenize(text):
  
  # initialize PunktSentenceTokenizer
  sentence_tokenizer = PunktSentenceTokenizer(text)
  
  # sentence tokenize text
  sentence_tokenized = sentence_tokenizer.tokenize(text)
  
  # creates a list to hold word tokenized sentences
  word_tokenized = list()
  
  # for-loop through each tokenized sentence in sentence_tokenized
  for tokenized_sentence in sentence_tokenized:
    # word tokenize each sentence and append to word_tokenized
    word_tokenized.append(word_tokenize(tokenized_sentence))
    
  return word_tokenized

# opening 'Tale of Two Cities' by Charles Dickens
with open(r".\tale2.txt") as ttc:
    text = ttc.read().lower()

# convert line breaks to spaces using re library
text = re.sub('\n', ' ', text)
# print(text)

# tokenize by word and sentence using word_sentence_tokenize function
word_tokenized_text = word_sentence_tokenize(text)
#print(word_tokenized_text)

# empty list for part of speech tagging
pos_tagged_text = list()

# for-loop through each word tokenized sentence here
for tagged_sentence in word_tokenized_text:
  # part-of-speech tag each sentence and append to list of pos-tagged sentences here
  pos_tagged_text.append(pos_tag(tagged_sentence))
# print(pos_tagged_text)

# initialization of WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# list comprehension lemmatize words in the list of POS tagged tokens.
lemmatized = [lemmatizer.lemmatize(token, pos_tag(token)) for token in word_tokenized_text]
print("lemmatized data:", lemmatized)

# writing my progess
#with open('notlemmatized.txt', 'w') as f:
    f.write(str(pos_tagged_text))
