import textblob
import nltk
from textblob import TextBlob
text='привет, я красавчик Олег, любите меня нежно.Я пою и играю на гитаре.'
blob=TextBlob(text)
tb_tags=blob.tags
tb_words=blob.words
tb_sent=blob.sentences
tb_ser=blob.serialized

print( tb_ser)

