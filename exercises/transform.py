input_file = '/home/anton/hexlet-git/exercises/input_file.txt'

output_file = '/home/anton/hexlet-git/exercises/output_file.txt'

rules = {
    'word_min_len': 5,
    'censored_words': ['explain', 'implementation'],
    'capital_letters': ['s', 'p'],
}


def word_min_len(text):
    text = text.split()
    text_word_min_len = []
    for i in text:
        if len(i) < int(rules.get('word_min_len')):
            continue
        else:
            text_word_min_len.append(i)
    if text_word_min_len != []:
        text = ' '.join(text_word_min_len)
        print(text)
        return text  + '\n'
    else:
        pass

def censored_words(text):
    if text != '':
        text = text.split()
        text_censored_words = []
        for i in text:
            if i in rules.get('censored_words'):
                continue
            else:
                text_censored_words.append(i)
        if text_censored_words != []:
            text = ' '.join(text_censored_words)
            print(text)
            return text + '\n'
        else:
            return ''

def capital_letters(text):
    if text != '':
        text = text.split()
        text_capital_letters = []
        for word in text:
            if word[0] in rules.get('capital_letters'):
                text_capital_letters.append(word.capitalize())
            else:
                text_capital_letters.append(word)
        if text_capital_letters != []:
            text = ' '.join(text_capital_letters)
            print(text)
            return text + '\n'
    else:
        return ''


input_file = open(input_file, "r")
output_file = open(output_file, "w")

for i in input_file:
    output_file.writelines(capital_letters(censored_words(word_min_len(i))))


input_file.close()
output_file.close()


'''

i = open(input_file, "r")

o = open(output_file, "w")


print(i.read())

o.write(i.read())

print(o.read())



def transform(input_file, output_file, rules):

    input_file = open(input_file, "r")
    output_file = open(output_file, "w")

    input_file = input_file.read()


    def word_min_len(text):
        text = text.split()
        text_word_min_len = []
        for i in text:
            if len(i) < int(rules.get('word_min_len')):
                continue
            else:
                text_word_min_len.append(i)
        text = ' '.join(text_word_min_len)
        return text
         
    def censored_words(text):
        text = text.split()
        text_censored_words = []
        for i in text:
            if i in rules.get('censored_words'):
                continue
            else:
                text_censored_words.append(i)
        text = ' '.join(text_censored_words)
        return text
    

    def capital_letters(text):
        text = text.split()
        text_capital_letters = []
        for word in text:
            if word[0] in rules.get('capital_letters'):
                text_capital_letters.append(word.capitalize())
            else:
                text_capital_letters.append(word)
        text = ' '.join(text_capital_letters)
        return text
        
    #print(word_min_len(censored_words(capital_letters(input_file))))  
          
    #output_file = word_min_len(censored_words(capital_letters(input_file)))
    #print(output_file)

    output_file.write(word_min_len(censored_words(capital_letters(input_file))))

    print(input_file.read())

    #word_min_len(output_file)
    #censored_words(output_file)
    #capital_letters(output_file)


transform(input_file, output_file, rules)

#print(output_file)
'''


'''
Реализуйте функцию transform(input_file, output_file, rules), которая принимает на вход путь до текстового файла, 
путь по которому нужно записать результат и обрабатывает текст согласно словарю rules следующим образом:

word_min_len - отфильтровывает слова меньше минимальной длины
censored_words - список слов, которые нужно удалить из текста
capital_letters - список букв, которые нужно привести к заглавным, если слово на них начинается

The Python language was not named after a long snake but after the British comedy show Monty Python Flying Circus

rules = {
    'word_min_len': 3,
    'censored_words': ['language', 'show'],
    'capital_letters': ['l', 'a'],
}
 
transform('python.txt', 'out.txt', rules=rules)
print(open('out.txt').read())
 
# => The Python was not named After Long snake but After the British comedy Monty Python Flying Circus

Подсказки
Используйте потоковую обработку
Каждое правило трансформера можно описать отдельной функцией и в итоговой собрать пайплайн обработки


def transform(input_file, output_file, rules):

    input_file = open(input_file, "r")
    output_file = open(output_file, "w")

    def word_min_len(text):
        text = text.split()
        text_word_min_len = []
        for i in text:
            if len(i) < int(rules.get('word_min_len')):
                continue
            else:
                text_word_min_len.append(i)
        text = ' '.join(text_word_min_len)
        return text
         
    def censored_words(text):
        text = text.split()
        text_censored_words = []
        for i in text:
            if i in rules.get('censored_words'):
                continue
            else:
                text_censored_words.append(i)
        text = ' '.join(text_censored_words)
        return text
    

    def capital_letters(text):
        text = text.split()
        text_capital_letters = []
        for word in text:
            if word[0] in rules.get('capital_letters'):
                text_capital_letters.append(word.capitalize())
            else:
                text_capital_letters.append(word)
        text = ' '.join(text_capital_letters)
        return text
        
    #print(word_min_len(censored_words(capital_letters(input_file))))  
          
    output_file = word_min_len(censored_words(capital_letters(input_file)))

'''