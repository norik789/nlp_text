import textblob
import nltk
from textblob import TextBlob
text='привет, я красавчик Олег, любите меня нежно'
blob=TextBlob(text)
print( blob.tags)

