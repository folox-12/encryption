operation = int(input("1 - code, 2 - decode: "))
alpha = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
key = str(input("KEY: "))
def key_up(key, alpha = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"):
    number_of_stolbec=[]
    key =key.upper()
    key1 = sorted(key)
    for i in range(len(key)):
        number_of_stolbec.append(key1.index(key[i]))
    return number_of_stolbec

def len_sen(sentences, key):
    while len(sentences) % len(key) != 0:
        sentences += "_"
    sentences = sentences.replace(' ', '_')
    return sentences
def show_table(sentences, key):
    sentences = create_tab(sentences, key)
    string = ""
    for i in range(len(key)):
        string += str(i + 1)
    print(string)
    for i in range(len(sentences)):
        print(sentences[i])
    key1 = key
    key1 = key_up(key1)
    for i in range(len(key1)):
        key1[i] += 1
    print("-" * 301)
    print(key)
    return key1
def create_tab(sentences, key):
    sentences = len_sen(sentences, key)
    stolbec =''
    c =[]
    for i in range(0, len(sentences), len(key)):
        stolbec = stolbec + sentences[i:len(key) + i]
        c.append(stolbec)
        stolbec =""
    return c
def create_sent(sentences, key):
    sentences = len_sen(sentences, key)
    stolbec =''
    c =[]
    stolb = int(len(sentences)/len(key))
    for i in range(0, len(sentences), stolb):
        stolbec = stolbec + sentences[i:stolb + i]
        c.append(stolbec)
        stolbec =""
    return c
def result2(sentences, key):
    dict = list(zip(key, sentences))
    dict = sorted(dict)
    dict_new =[]
    for i in range(len(dict)):
        dict_new.append(dict[i][1])
    dict =dict_new
    res =''
    for i in range(len(dict[0])):
        for j in range(len(key)):
            res += dict[j][i]
    return res.upper()
def result(c, key, sentences, alpha = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЭЮЯ"):
    res =""
    key1 =key_up(key)
    a = int(len(sentences) / len(key))
    for j in key1:
        for i in range(a):
            res += c[i][j]
    return res.upper()
if operation ==1:
    sentences = str(input("Sentences: "))
    print(result(create_tab(sentences, key), key, len_sen(sentences, key)))
    print("-" * 30)
    print(show_table(sentences, key))
elif operation == 2:
    code = str(input("code: "))
    print(result2(create_sent(code, key), key_up(key)))
