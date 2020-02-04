# P You are given a string, each char must appear an even number of 
# times within the string. record it and see how many chars need to be deleted to get an even word.

#E 
# even_word('aaaa') == 0
# even_word('potato') == 2
# even_word('aabbbb') == 0
# even_word('aaabbbccc') == 3

# D 
# Working with dictionaries, and strings.

# A
#   create Dictionary(recorder)
#   loop over string, place in recorder
#   loop over recorder, modulo or subtract chars to find 
#     which gives you an even number of chars left in recorder
  
#C 
def even_word(string):
    recorder = {}
    wordDeleted = 0
    
    for char in string:
        if not recorder[char]:
            recorder[char] = 1
        if recorder[char]:
            recorder[char] += 1

    #  use while loop, while len(string ) % 2 == 1
    for letter in recorder:
        if recorder[letter] % 2 == 1:
            wordDeleted+=1
            # del recorder[letter]
    return wordDeleted


print(even_word('potato')) # == 2