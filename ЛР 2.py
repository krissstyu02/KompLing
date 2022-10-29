from pymorphy2 import MorphAnalyzer
from nltk import sent_tokenize  # для разделения текста на предложения
from nltk import word_tokenize

morph = MorphAnalyzer()
dictPos = {
    'NOUN': 'существительное',
    'ADJF': 'полное прилагательное',
    'ADJS': 'краткое прилагательное',
    'COMP': 'компаратив',
    'VERB': 'глагол (личная форма)',
    'INFN': 'глагол (инфинитив)',
    'PRTF': 'полное причастие',
    'PRTS': 'краткое причастие',
    'GRND': 'деепричастие',
    'NUMR': 'числительное',
    'ADVB': 'наречие',
    'NPRO': 'местоимение-существительное',
    'PRED': 'предикатив',
    'PREP': 'предлог',
    'CONJ': 'союз',
    'PRCL': 'частица',
    'INTJ': 'междометие',
    None: 'не определено'
}
dictAspect = {
    'perf': 'совершенный',
    'impf': 'несовершенный',
    None: 'не определено'
}
dictCase = {
    'nomn': 'именительный',
    'gent': 'родительный',
    'datv': 'дательный',
    'accs': 'винительный',
    'ablt': 'творительный',
    'loct': 'предложный',
    'voct': 'звательный',
    'gen2': 'второй родительный (частичный)',
    'acc2': 'второй винительный',
    'loc2': 'второй предложный (местный)',
    None: 'не определено'
}
dictGender = {
    'masc': 'мужской',
    'femn': 'женский',
    'neut': 'средний',
    'ms-f': 'общий',
    None: 'не определено'
}
dictMood = {
    'indc': 'изъявительное',
    'impr': 'повелительное',
    None: 'не определено'
}
dictNumber = {
    'sing': 'единственное',
    'plur': 'множественное',
    None: 'не определено'
}
dictPerson = {
    '1per': 1,
    '2per': 2,
    '3per': 3,
    None: 'не определено'
}
dictTense = {
    'pres': 'настоящее',
    'past': 'прошедшее',
    'futr': 'будущее',
    None: 'не определено'
}


def morphAnalyzer(text):
    p = morph.parse(text)[0]
    print(" Анализ слова ",text)
    print("Нормальная форма слова:", p.normal_form)
    print('Часть речи:', dictPos[p.tag.POS])
    print('Наклонение:', dictMood[p.tag.mood])
    print('Падеж:', dictCase[p.tag.case])
    print('Число:', dictNumber[p.tag.number])
    print('Вид:', dictAspect[p.tag.aspect])
    print('Род: ', dictGender[p.tag.gender])
    print('Лицо:', dictPerson[p.tag.person])
    print('Время:', dictTense[p.tag.tense])


def morphInflect(text):
    print("Выберите дейстивие:")
    print('''\t1. Склонение
\t2. Лексема слова ''')
    act = int(input())
    if act == 1:
        print("Как просклонять наше слово")
        case = input("Выберите падеж(Введите что-то из списка: nomn(именительный),gent(родительный), datv(дательный),accs(винительный),ablt(творительный),loct(предложный),voct(звательный))   ")
        number = input("Выберите число(Введите из списка: sing(единтсвенное), plur(множественное))   ")
        gender = input("Выберите род?(Введите из списка: masc(мужской), femn(женский), neut(средний))   ")
        a = {case, number, gender}
        p = morph.parse(text)[0]
        if p.inflect(a) != None:
            print(p.inflect(a).word)
        else:
            print("None")

    elif act == 2:
        p = morph.parse(text)[0]
        for i in p.lexeme:
            print(i.word, end='; ')
        print()


def morphNumber(text):
    n = int(input("Введите число  "))
    p = morph.parse(text)[0]
    print(str(n) + " " + str(p.make_agree_with_number(n).word))


def menu():
    print(" Выберите пункт из  меню: ")
    print('''\t1. Морфологический анализ
\t2. Просклонять слово
\t3. Согласование слова с числительным
\t4. Выйти''')
    actions = int(input())
    if actions != 4:

        if actions == 1:
            name_file = "Dataset"
            g = open(name_file + ".txt", "r", encoding='utf-8')
            words = []  # массив слов
            text = g.readlines()

            for el in text:
                sentences = sent_tokenize(el)
                for i in range(len(sentences)):
                    sent = sentences[i]
                    words += word_tokenize(sent)
            for i in range(15):
               if words[i] != ',' and words[i] != '.':
                  print(str(morphAnalyzer(words[i])) + "\n")

        elif actions == 2:
            word = input("Введите слово: ")
            print(str(morphInflect(word)) + "\n")

        elif actions == 3:
            word = input("Введите слово: ")
            print(str(morphNumber(word)) + "\n")

        print("\n")
        menu()

    else:
        return
menu()
