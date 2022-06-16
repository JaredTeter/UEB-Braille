braille = [
    # 0-9
    [[' ', ' '], [' ', ' '], [' ', ' ']],  # white space
    [['·', 'O'], ['O', '·'], ['O', 'O']],  # the
    [['·', '·'], ['·', 'O'], ['·', '·']],  # contraction
    [['·', 'O'], ['·', 'O'], ['O', 'O']],  # number prefix
    [['O', 'O'], ['O', '·'], ['·', 'O']],  # ed
    [['O', 'O'], ['·', '·'], ['·', 'O']],  # sh
    [['O', 'O'], ['O', '·'], ['O', 'O']],  # and
    [['·', '·'], ['·', '·'], ['O', '·']],  # '
    [['O', '·'], ['O', 'O'], ['O', 'O']],  # of
    [['·', 'O'], ['O', 'O'], ['O', 'O']],  # with

    # 10-19
    [['O', '·'], ['·', '·'], ['·', 'O']],  # ch
    [['·', 'O'], ['·', '·'], ['O', 'O']],  # ing
    [['·', '·'], ['·', '·'], ['·', 'O']],  # uppercase prefix
    [['·', '·'], ['·', '·'], ['O', 'O']],  # -
    [['·', 'O'], ['·', '·'], ['·', 'O']],  # italic prefix
    [['·', 'O'], ['·', '·'], ['O', '·']],  # st
    [['·', '·'], ['·', 'O'], ['O', 'O']],  # " (closing quotation mark)
    [['·', '·'], ['O', '·'], ['·', '·']],  # ,
    [['·', '·'], ['O', '·'], ['O', '·']],  # ;
    [['·', '·'], ['O', 'O'], ['·', '·']],  # :

    # 20-29
    [['·', '·'], ['O', 'O'], ['·', 'O']],  # ·
    [['·', '·'], ['O', '·'], ['·', 'O']],  # en
    [['·', '·'], ['O', 'O'], ['O', '·']],  # !
    [['·', '·'], ['O', 'O'], ['O', 'O']],  # (or)
    [['·', '·'], ['O', '·'], ['O', 'O']],  # ? or " (opening quoatation mark)
    [['·', '·'], ['·', 'O'], ['O', '·']],  # in
    [['O', '·'], ['·', 'O'], ['·', 'O']],  # wh
    [['·', '·'], ['·', 'O'], ['·', 'O']],  # letter prefix
    [['O', '·'], ['O', '·'], ['·', 'O']],  # gh
    [['O', 'O'], ['O', 'O'], ['O', 'O']],  # for

    # 30-32
    [['·', 'O'], ['·', 'O'], ['O', '·']],  # ar
    [['O', 'O'], ['·', 'O'], ['·', 'O']],  # th
    [['·', 'O'], ['·', '·'], ['·', '·']],  # accent prefix

    # 33-58
    [['O', '·'], ['·', '·'], ['·', '·']],  # a
    [['O', '·'], ['O', '·'], ['·', '·']],  # b
    [['O', 'O'], ['·', '·'], ['·', '·']],  # c
    [['O', 'O'], ['·', 'O'], ['·', '·']],  # d
    [['O', '·'], ['·', 'O'], ['·', '·']],  # e
    [['O', 'O'], ['O', '·'], ['·', '·']],  # f
    [['O', 'O'], ['O', 'O'], ['·', '·']],  # g
    [['O', '·'], ['O', 'O'], ['·', '·']],  # h
    [['·', 'O'], ['O', '·'], ['·', '·']],  # i
    [['·', 'O'], ['O', 'O'], ['·', '·']],  # j
    [['O', '·'], ['·', '·'], ['O', '·']],  # k
    [['O', '·'], ['O', '·'], ['O', '·']],  # l
    [['O', 'O'], ['·', '·'], ['O', '·']],  # m
    [['O', 'O'], ['·', 'O'], ['O', '·']],  # n
    [['O', '·'], ['·', 'O'], ['O', '·']],  # o
    [['O', 'O'], ['O', '·'], ['O', '·']],  # p
    [['O', 'O'], ['O', 'O'], ['O', '·']],  # q
    [['O', '·'], ['O', 'O'], ['O', '·']],  # r
    [['·', 'O'], ['O', '·'], ['O', '·']],  # s
    [['·', 'O'], ['O', 'O'], ['O', '·']],  # t
    [['O', '·'], ['·', '·'], ['O', 'O']],  # u
    [['O', '·'], ['O', '·'], ['O', 'O']],  # v
    [['·', 'O'], ['O', 'O'], ['·', 'O']],  # w
    [['O', 'O'], ['·', '·'], ['O', 'O']],  # x
    [['O', 'O'], ['·', 'O'], ['O', 'O']],  # y
    [['O', '·'], ['·', 'O'], ['O', 'O']],  # z

    # 59-63
    [['·', 'O'], ['O', '·'], ['·', 'O']],  # ow
    [['O', '·'], ['O', 'O'], ['·', 'O']],  # ou
    [['O', 'O'], ['O', 'O'], ['·', 'O']],  # er
    [['·', 'O'], ['·', 'O'], ['·', '·']],  # contraction symbol
    [['·', 'O'], ['·', 'O'], ['·', 'O']],  # contraction symbol
]

wordsigns = [
    ['but', 'B'], ['can', 'C'], ['do', 'D'], ['every', 'E'], ['from', 'F'], ['go', 'G'], ['have', 'H'], ['just', 'J'], ['knowledge', 'K'], ['like', 'L'], 
    ['more', 'M'], ['not', 'N'], ['people', 'P'], ['quite', 'Q'], ['rather', 'R'], ['so', 'S'], ['that', 'T'], ['us', 'U'], ['very', 'V'], ['will', 'W'], 
    ['it', 'X'], ['you', 'Y'], ['as', 'Z']
]

shortform_words = [
    ['about', 'AB'], ['above', 'ABV'], ['according', 'AC'], ['across', 'ACR'], ['after', 'AF'], ['afternoon', 'AFN'], ['afterward', 'AFW'], ['again', 'AG'], ['against', 'AG/'],
    ['almost', 'ALM'], ['already', 'ALR'], ['also', 'AL'], ['although', 'AL?'], ['altogether', 'ALT'],['always', 'ALW'], ['because', '2C'], ['before', '2F'], ['behind', '2H'],
    ['below', '2L'], ['beneath', '2N'], ['beside', '2S'], ['between', '2T'], ['beyond', '2Y'], ['blind', 'BL'], ['braille', 'BRL'], ['children', '*N'], ['conceive', '3CV'],
    ['conceiving', '3CVG'], ['could', 'CD'], ['deceive', 'DCV'], ['deceiving', 'DCVG'], ['declare', 'DCL'], ['declaring', 'DCLG'], ['either', 'EI'], ['first', 'F/'], ['friend', 'FR'],
    ['good', 'GD'], ['great', 'GRT'], ['herself', 'H]F'], ['him', 'HM'], ['himself', 'HMF'], ['immediate', 'imm'], ['its', 'XS'], ['itself', 'XF'], ['letter', 'lr'], ['little', 'll'],
    ['much', 'M*'], ['must', 'M/'], ['myself', 'MYF'], ['necessary', 'NEC'], ['neither', 'NEI'], ['oneself', '"OF'], ['ourselves', '\RVS'], ['paid', 'PD'], ['perceive', 'P]CV'],
    ['perceiving', 'P]CVG'], ['perhaps', 'P]H'], ['quick', 'QK'], ['receive', 'RCV'], ['receiving', 'RCVG'], ['rejoice', 'RJC'], ['rejoiceing', 'RJCG'], ['said', 'SD'], ['should', '%D'],
    ['such', 'S*'], ['themselves', '!MVS'], ['thyself', '?YF'], ['today', 'TD'], ['together', 'TGR'], ['tomorrow', 'TM'], ['tonight', 'TN'], ['would', 'WD'], ['your', 'YR'], ['yourself', 'YRF'],
    ['yourselves', 'YRVS']
]

initial_letter_contractions = [
    ['day', '"D'], ['ever', '"E'], ['father', '"F'], ['here', '"G'], ['know', '"K'], ['lord', '"L'], ['mother', '"M'], ['name', '"N'], ['one', '"O'],
    ['part', '"P'], ['question', '"Q'], ['right', '"R'], ['some', '"S'], ['time', '"T'], ['under', '"U'], ['work', '"W'], ['young', '"Y'],
    ['there', '"!'],  ['character', '"*'], ['through', '"?'], ['where', '":'], ['ought', '"' + chr(92)],  ['upon', '^U'], ['word', '^W'],
    ['these', '^!'], ['those', '^?'], ['whose', '^:'],  ['cannot', '_C'], ['had', '_H'], ['many', '_M'], ['spirit', '_S'], ['world', '_W'],
    ['their', '_!']
]

strong_wordsigns = [
    ['child', '*'], ['shall', '%'], ['this', '?'], ['which', ':'], ['out', chr(92)], ['still', '/']
]

strong_groupsigns = [
    ['ch', '*'], ['sh', '%'], ['th', '?'], ['wh', ':'], ['ou', chr(92)], ['st', '/'], ['gh', '<'], ['ed', '$'], ['er', ']'], ['ow', '['],
    ['ar', '>'], ['ing', '+'],
]

strong_contractions = [
    ['and', '&'], ['for', '='], ['of', '('], ['the', '!'], ['with', ')']
]

final_letter_groupsigns = [
    ['ound', '.D'], ['ance', '.E'], ['sion', '.N'], ['less', '.S'], ['ount', '.T'], ['ence', ';E'], ['ong', ';G'], ['ful', ';L'], ['tion', ';T'],
    ['ness', ';S'], ['ment', ';T'], ['ity', ';Y']
]

lower_groupsigns_in_word = [ # cannot be used at the end or beginning of a word
    ['ea', '1'], ['bb', '2'], ['cc', '3'], ['ff', '6'], ['gg', '7']
]

lower_groupsigns_begin = [
    ['be', '2'], ['con', '3'], ['dis', '4'], ['en', '5'], ['in', '9'] # Need to deal with these separately because of the different rules within this group
]

lower_wordsigns = [
    ['be', '2'], ['enough', '5'], ['were', '7'], ['his', '8'], ['in', '9'], ['was', '0']
]


# The quick brown fox jumps over the lazy dog
# text = input()
text = "This will be enough. It was in his house."
braille_ascii = ''
opening_double_quote = True
opening_single_quote = True
print(f"\nUser input is: {text}\n")

for word in text.split():
    braille_ascii += ' '
    my_word = ''

    for index, char in enumerate(word):
        # print(char)
        if char.isupper():  # add upercase symbol
            braille_ascii += ','
        if 97 <= ord(char.lower()) <= 122:  # if character is a letter
            my_word += char.lower()
        # If my_word is not empty and we've reached the end or this character is not a letter
        if (my_word and (index == len(word) - 1) or not (97 <= ord(char.lower()) <= 122)):
            #count = len(my_word)
            for i in wordsigns:
                if i[0] == my_word:
                    braille_ascii += i[1]
                    my_word = ''
                    break
            if 97 <= ord(char.lower()) <= 122:
                for i in lower_wordsigns:
                    if i[0] == my_word:
                        braille_ascii += i[1]
                        my_word = ''
                        break
            for i in shortform_words:
                if i[0] == my_word:
                    braille_ascii += i[1]
                    my_word = ''
                    break
            for i in strong_wordsigns:
                if i[0] == my_word:
                    braille_ascii += i[1]
                    my_word = ''
                    break
            count = 0
            restart = False
            while count < len(my_word):
                for i in initial_letter_contractions:
                    if my_word.find(i[0], count) == count:
                        braille_ascii += i[1]
                        count += len(i[0])
                        restart = True
                        break
                if restart == True:
                    restart = False
                    continue
                for i in strong_contractions:
                    if my_word.find(i[0], count) == count:
                        braille_ascii += i[1]
                        count += len(i[0])
                        restart = True
                        break
                if restart == True:
                    restart = False
                    continue
                for i in final_letter_groupsigns:
                    if my_word.find(i[0], count) == count:
                        braille_ascii += i[1]
                        count += len(i[0])
                        restart = True
                        break
                if restart == True:
                    restart = False
                    continue
                for i in strong_groupsigns:
                    if my_word.find(i[0], count) == count:
                        braille_ascii += i[1]
                        count += len(i[0])
                        restart = True
                        break
                if restart == True:
                    restart = False
                    continue
                if 0 < count < (len(my_word) -2):
                    for i in lower_groupsigns_in_word:
                        if my_word.find(i[0], count) == count:
                            braille_ascii += i[1]
                            count += len(i[0])
                            restart = True
                            break
                if restart == True:
                    restart = False
                    continue
                if count < len(my_word):
                    braille_ascii += my_word[count].upper()
                count += 1
            my_word = ''

        #if char.isspace():
            #braille_ascii += " "
        if 33 <= ord(char) <= 47 or 58 <= ord(char) <= 64:  # if character is a symbol
            if char == '!':
                braille_ascii += '6'
            elif char == '"':
                if opening_double_quote:
                    braille_ascii += '8'
                    opening_double_quote = False
                else:
                    braille_ascii += '0'
                    opening_double_quote = True
            elif char == '#':
                braille_ascii += '#'
            elif char == '$':
                braille_ascii += '@S'
            elif char == '%':
                braille_ascii += '.0'
            elif char == '&':
                braille_ascii += '@&'
            elif char == "'":
                if index != 0 and 97 <= ord(word[index - 1].lower()) <= 122:
                    braille_ascii += "'"
                elif opening_single_quote:
                    braille_ascii += ',8'
                    opening_single_quote = False
                else:
                    braille_ascii += ',0'
                    opening_single_quote = True
            elif char == '(':
                braille_ascii += '"<'
            elif char == ')':
                braille_ascii += '">'
            elif char == '*':
                braille_ascii += '"9'
            elif char == '+':
                braille_ascii += '"6'
            elif char == ',':
                braille_ascii += '1'
            elif char == '-':
                braille_ascii += '-'
            elif char == '.':
                braille_ascii += '4'
            elif char == '/':
                braille_ascii += '_/'
            elif char == ':':
                braille_ascii += '3'
            elif char == ';':
                braille_ascii += '2'
            elif char == '>':
                braille_ascii += '">'
            elif char == '=':
                braille_ascii += '"7'
            elif char == '<':
                braille_ascii += '"<'
            elif char == '?':
                braille_ascii += '8'
            elif char == '@':
                braille_ascii += '@A'
        if char.isnumeric():  # if character is a number
            if index == 0 or (index > 0 and not word[index - 1].isnumeric()):
                braille_ascii += '#'
            if char == '0':
                braille_ascii += 'J'
            else:
                braille_ascii += chr(ord(char) + 16)


for i in braille_ascii.split():
    print(i)

for word in braille_ascii.split():
    print('\n' + word)
    for x in range(3):
        for letter in word:
            cell = ord(letter) - 32
            print(braille[cell][x][0] + ' ' + braille[cell][x][1], end="   ")
        print('')

print("\nEnd of the program\n")