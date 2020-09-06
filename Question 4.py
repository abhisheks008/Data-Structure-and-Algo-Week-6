def censor(text, word):
    word_list = text.split()
    count = 0
    index = 0
    for i in word_list:
        if i == word:
            word_list[index] = 'THE'
        index += 1
    result =' '.join(word_list)
    return result
    
if __name__== '__main__':
extract = input()
cen = "the"
print(censor(extract, cen))
