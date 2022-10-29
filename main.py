import nltk
from nltk import download
#download('stopwords')
#nltk.download('punkt')
from nltk import sent_tokenize  # для разделения текста на предложения
from nltk import word_tokenize  #для разделения предложений на слова
from nltk.corpus import stopwords

file = open("Dataset.txt", 'r', encoding='utf8')

def splitSentence(text):
    return sent_tokenize(text)


def splitWord(text):
    return word_tokenize(text)


def delStopWord(text):
    stop_words = set(stopwords.words('russian'))
    words = splitWord(text)
    without_stop_words = [word for word in words if not word in stop_words]
    return without_stop_words


def frequency(text):
    words = splitWord(text)
    d = dict.fromkeys(set(words), 0)
    d.pop(',')
    d.pop('.')
    for word in words:
        if word in d:
            d[word] += 1
    return d


text = file.readlines()
text = ' '.join(text)
text = text.split('\n')
text = ' '.join(text)
while True:

    print('''\nВыберите действие:
       1.Разделение входного текста на предложения
       2.Разделение входного текста на слова
       3.Удаление стоп-слов из текста
       4.Частота встречаемости слов
       5.Закончить выполнение программы''')
    n = int(input())
    if n == 5:
        break
    func = [splitSentence(text), splitWord(text), delStopWord(text), frequency(text)]
    res = func[n - 1]
    if n == 4:
        for key in res:
            print(key + ' - ' + str(res[key]) + ', ', end='')

    else:
        print(res)



