import os
# import collections
# import string

dictionary = ['cat', 'cut', 'cot', 'cow', 'coy', 'coz', 'rods',  'cup', 'nut', 'golf', 'dog', 'loaf', 'six', 'head',
              'cog', 'col', 'cobs', 'roy', 'bag', 'cops', 'cop', 'keg', 'peg', 'pig', 'bug', 'fix', 'big', 'leg', 'fit',
              'day', 'jet', 'job', 'fin', 'ray', 'bin', 'dig', 'bun', 'ban', 'rag', 'yet', 'lead', 'fig', 'kid', 'kit',
              'beg', 'goad', 'fog', 'max', 'hen', 'pen', 'fan', 'ben', 'boy', 'rat', 'cod', 'min', 'pay', 'hay', 'way',
              'lib', 'lid', 'lip', 'wax', 'jog', 'few', 'law', 'low', 'one', 'old', 'odd', 'lay', 'lie', 'wolf', 'meet',
              'code', 'get', 'god', 'too', 'tee', 'tea', 'boo', 'ruby', 'fad', 'hey', 'load', 'can', 'den', 'ask', 'let',
              'led', 'oil', 'our', 'sew', 'ore', 'pug', 'nix', 'soy', 'saw', 'say', 'pie', 'log', 'mad', 'may', 'meat',
              'win', 'won', 'zip', 'car', 'mud', 'mug', 'far', 'mid', 'fat', 'pin', 'ham', 'bed', 'pid', 'pit', 'pun',
              'pan', 'nod', 'rod', 'fed', 'yet', 'zoo', 'mat', 'mum', 'new', 'now', 'box', 'rubs', 'mop', 'mob', 'sum',
              'two', 'tug', 'rode', 'man', 'rust', 'must', 'lust', 'sat', 'sky', 'log', 'ski', 'she', 'was', 'war',
              'ton', 'vet', 'tin', 'sin', 'tom', 'web', 'who', 'nun', 'nan', 'why', 'wet', 'robs']


#check if word is in dictionary
def does_word_exsist(word):
    # dictionary.lowercase - every string
    if word in dictionary:
        print ('word is in dictionary')
        return True
    else:
        print ('word is not in dict')
        return False


def chain_maker(first_word, last_word):
    #check lenght of words and presence in dic)t , so only same length words are being used
    if not len(first_word) != len(last_word) and does_word_exsist(first_word) and does_word_exsist(last_word):
        # iteration of first word
        iter = [i for i in first_word]
        # variable to store difference
        number = 0
        for j in last_word:
            if j in iter:
                iter += 1
        return 1+len(first_word) - number
    else:
        return ('chain not possible')


print(chain_maker('cat', 'dog'))
print(chain_maker('lead', 'gold'))
print(chain_maker('ruby', 'code'))