from textblob import TextBlob, Word
 
# SPELL CHECKER
# -------------------------------------------
def spell_check(org_word):
    spl_char_list = ['@','/','\\','.','.','#','!','?','{','}','(',')','[',']','+','-',':',';','"','\'']
    spl_char = set(spl_char_list)
    p = []
    word = ''
    if org_word[-1] in spl_char:
        p = org_word[-1]
        word = org_word[:len(org_word)-1]
        word = ''.join(word)
    else:
        word = org_word

    sentence = Word(word)
    alternatives = sentence.spellcheck()
    if alternatives[0][1] == 1.0:
        result = alternatives[0][0]
        if p:
            result_list = list(result)
            result_list.append(p)
            result = ''.join(result_list)
        return result
    elif word == alternatives[0][0]:
        if p:
            result_list = list(word)
            result_list.append(p)
            result = ''.join(result_list)
        return result
    else:
        altnatives_list = []
        i = 1
        print('mispelled word:',word)
        for words in alternatives[:5]:
            print(i, words[0])
            i+=1
            altnatives_list.append(words[0])
        chosen_word = int(input('Choose desired word index:'))
        result = altnatives_list[chosen_word-1]
        if p:
            result_list = list(result)
            result_list.append(p)
            result = ''.join(result_list)
        return result

# MAIN
# -----------------------------------------------
word_sentence = 'Dhe Featheres knoek aach ither!'
l = word_sentence.split()
corrected_sentence = spell_check(l[0])
for word in l[1:]:
    corrected_sentence += ' '+ spell_check(word)

print('-----------OUTPUT------------')
print()
print(corrected_sentence)
