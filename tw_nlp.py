import textblob
import nltk
from textblob import TextBlob
from textblob import Blobber

text='привет, я красавчик Олег, любите меня нежно.Я пою и играю на гитаре.'
blob=TextBlob(text)
tb_tags=blob.tags
tb_words=blob.words
tb_sent=blob.sentences
tb_ser=blob.serialized
tb_st=blob.sentiment

print(tb_st)

