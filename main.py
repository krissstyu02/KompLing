import nltk
from nltk import download
download('stopwords')
nltk.download('punkt')
from nltk import sent_tokenize  # для разделения текста на предложения
from nltk import word_tokenize  #для разделения предложений на слова
from nltk.corpus import stopwords
file = open("DataSet.txt", "r", encoding="utf8")
text = file.readlines()
count = 1 # для нумерации предложений в тексте

st_words = set(stopwords.words('russian')) #русские стоп-слова

# каждую строчку текста разбиваем на предложения(слова), потом выводим
for el in text:
    sentences = sent_tokenize(el) #разбиваем строку на предложения
    for i in range(len(sentences)):
        print("Предложение номер " + " " + str(count) + ": " + str(sentences[i]))
        sent = sentences[i]
        count += 1
        words = word_tokenize(sent)
        without_stop_words = [word for word in words if not word in st_words]
        print("Слова из этого предложения: ", sep="")
        print( without_stop_words, sep=" ")
        print()

