operation = int(input("codirovanie: 1, decodirovanie: 2 "))
kluch = str(input("Kluch: "))
alfa = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
def add_none_dict(sentence, alfa):
    sentence = sentence.upper()
    for i in sentence:
        if i not in alfa:
            alfa += i
    return alfa


def kluch_num(kluch, alfa = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"):
    num = []
    kluch = kluch.upper()
    for i in kluch:
        num.append(alfa.index(i))
    return num

def shifr(sentence, kluch, alfa = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"):
    sentence = sentence.upper()
    kluch = kluch_num(kluch)
    alfa = add_none_dict(sentence, alfa)
    
    i = 0

    kluch_new = []
    d = 0
    
    while d < len(sentence):
        kluch_new.append(kluch[i])
        i+=1
        d +=1
        if i == len(kluch):
            i = 0

    rez_num = []

    for i in range(len(sentence)):
        rez_num.append(alfa.index(sentence[i])+kluch_new[i]+1)
    rez = ""
    
    for i in range(len(rez_num)):
        rez+= str(alfa[rez_num[i] % len(alfa)])
    return rez
def decode(code, kluch, alfa = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"):
    num_key = kluch_num(kluch)
    alfa = add_none_dict(code, alfa)
    code = kluch_num(code)
    i = 0
    kluch_new = []
    d = 0
    while d < len(code):
        kluch_new.append(num_key[i])
        i+=1
        d +=1
        if i == len(kluch):
            i = 0
    res =""
    for i in range(len(code)):
        w = code[i] - kluch_new[i] - 1
        if w < 0:
            w += len(alfa)
            res += alfa[w]
        else:
            res += alfa[w]
    return res
if operation == 1:
    sentences = str(input("Sentence "))
    print(shifr(sentences, kluch))
if operation == 2:
    code = str(input("Code "))
    print(decode(code, kluch))
