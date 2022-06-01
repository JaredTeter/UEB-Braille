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

# The quick brown fox jumps over the lazy dog
# text = input()
text = "The quick brown fox"
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
        if (my_word and (index == len(word) -1 ) or not (97 <= ord(char.lower()) <= 122)): # If my_word is not and we've reached the end or this character is not a letter
            if 'but' == my_word: # Alphabetic Wordsigns
                braille_ascii += 'B'
            elif 'can' == my_word:
                braille_ascii += 'C'
            elif 'do' == my_word:
                braille_ascii += 'D'
            elif 'every' == my_word:
                braille_ascii += 'E'
            elif 'from' == my_word:
                braille_ascii += 'F'
            elif 'go' == my_word:
                braille_ascii += 'G'
            elif 'have' == my_word:
                braille_ascii += 'H'
            elif 'just' == my_word:
                braille_ascii += 'J'
            elif 'knowledge' == my_word:
                braille_ascii += 'K'
            elif 'like' == my_word:
                braille_ascii += 'L'
            elif 'more' == my_word:
                braille_ascii += 'M'
            elif 'not' == my_word:
                braille_ascii += 'N'
            elif 'people' == my_word:
                braille_ascii += 'P'
            elif 'quite' == my_word:
                braille_ascii += 'Q'
            elif 'rather' == my_word:
                braille_ascii += 'R'
            elif 'so' == my_word:
                braille_ascii += 'S'
            elif 'that' == my_word:
                braille_ascii += 'T'
            elif 'us' == my_word:
                braille_ascii += 'U'
            elif 'very' == my_word:
                braille_ascii += 'V'
            elif 'will' == my_word:
                braille_ascii += 'W'
            elif 'it' == my_word:
                braille_ascii += 'X'
            elif 'you' == my_word:
                braille_ascii += 'Y'
            elif 'as' == my_word:
                braille_ascii += 'Z'
            elif 'about' == my_word: # Shortform Words
                braille_ascii += 'AB'
            elif 'above' == my_word:
                braille_ascii += 'ABV'
            elif 'according' == my_word:
                braille_ascii += 'AC'
            elif 'across' == my_word:
                braille_ascii += 'ACR'
            elif 'after' == my_word:
                braille_ascii += 'AF'
            elif 'afternoon' == my_word:
                braille_ascii += 'AFN'
            elif 'afterward' == my_word:
                braille_ascii += 'AFW'
            elif 'again' == my_word:
                braille_ascii += 'AG'
            elif 'against' == my_word:
                braille_ascii += 'AG/'
            elif 'almost' == my_word:
                braille_ascii += 'ALM'
            elif 'already' == my_word:
                braille_ascii += 'ALR'
            elif 'also' == my_word:
                braille_ascii += 'AL'
            elif 'although' == my_word:
                braille_ascii += 'AL?'
            elif 'altogether' == my_word:
                braille_ascii += 'ALT'
            elif 'always' == my_word:
                braille_ascii += 'ALW'
            elif 'because' == my_word:
                braille_ascii += '2C'
            elif 'before' == my_word:
                braille_ascii += '2F'
            elif 'behind' == my_word:
                braille_ascii += '2H'
            elif 'below' == my_word:
                braille_ascii += '2L'
            elif 'beneath' == my_word:
                braille_ascii += '2N'
            elif 'beside' == my_word:
                braille_ascii += '2S'
            elif 'between' == my_word:
                braille_ascii += '2T'
            elif 'beyond' == my_word:
                braille_ascii += '2Y'
            elif 'blind' == my_word:
                braille_ascii += 'BL'
            elif 'braille' == my_word:
                braille_ascii += 'BRL'
            elif 'children' == my_word:
                braille_ascii += '*N'
            elif 'conceive' == my_word:
                braille_ascii += '3CV'
            elif 'conceiving' == my_word:
                braille_ascii += '3CVG'
            elif 'could' == my_word:
                braille_ascii += 'CD'
            elif 'deceive' == my_word:
                braille_ascii += 'DCV'
            elif 'deceiving' == my_word:
                braille_ascii += 'DCVG'
            elif 'declare' == my_word:
                braille_ascii += 'DCL'
            elif 'declaring' == my_word:
                braille_ascii += 'DCLG'
            elif 'either' == my_word:
                braille_ascii += 'EI'
            elif 'first' == my_word:
                braille_ascii += 'F/'
            elif 'friend' == my_word:
                braille_ascii += 'FR'
            elif 'good' == my_word:
                braille_ascii += 'GD'
            elif 'great' == my_word:
                braille_ascii += 'GRT'
            elif 'herself' == my_word:
                braille_ascii += 'H]F'
            elif 'him' == my_word:
                braille_ascii += 'HM'
            elif 'himself' == my_word:
                braille_ascii += 'HMF'
            elif 'immediate' == my_word:
                braille_ascii += 'imm'
            elif 'its' == my_word:
                braille_ascii += 'XS'
            elif 'itself' == my_word:
                braille_ascii += 'XF'
            elif 'letter' == my_word:
                braille_ascii += 'lr'
            elif 'little' == my_word:
                braille_ascii += 'll'
            elif 'much' == my_word:
                braille_ascii += 'M*'
            elif 'must' == my_word:
                braille_ascii += 'M/'
            elif 'myself' == my_word:
                braille_ascii += 'MYF'
            elif 'necessary' == my_word:
                braille_ascii += 'NEC'
            elif 'neither' == my_word:
                braille_ascii += 'NEI'
            elif 'oneself' == my_word:
                braille_ascii += '"OF'
            elif 'ourselves' == my_word:
                braille_ascii += '\RVS'
            elif 'paid' == my_word:
                braille_ascii += 'PD'
            elif 'perceive' == my_word:
                braille_ascii += 'P]CV'
            elif 'perceiving' == my_word:
                braille_ascii += 'P]CVG'
            elif 'perhaps' == my_word:
                braille_ascii += 'P]H'
            elif 'quick' == my_word:
                braille_ascii += 'QK'
            elif 'receive' == my_word:
                braille_ascii += 'RCV'
            elif 'receiving' == my_word:
                braille_ascii += 'RCVG'
            elif 'rejoice' == my_word:
                braille_ascii += 'RJC'
            elif 'rejoiceing' == my_word:
                braille_ascii += 'RJCG'
            elif 'said' == my_word:
                braille_ascii += 'SD'
            elif 'should' == my_word:
                braille_ascii += '%D'
            elif 'such' == my_word:
                braille_ascii += 'S*'
            elif 'themselves' == my_word:
                braille_ascii += '!MVS'
            elif 'thyself' == my_word:
                braille_ascii += '?YF'
            elif 'today' == my_word:
                braille_ascii += 'TD'
            elif 'together' == my_word:
                braille_ascii += 'TGR'
            elif 'tomorrow' == my_word:
                braille_ascii += 'TM'
            elif 'tonight' == my_word:
                braille_ascii += 'TN'
            elif 'would' == my_word:
                braille_ascii += 'WD'
            elif 'your' == my_word:
                braille_ascii += 'YR'
            elif 'yourself' == my_word:
                braille_ascii += 'YRF'
            elif 'yourselves' == my_word:
                braille_ascii += 'YRVS'
            else:
                for char in my_word:
                    braille_ascii += char.upper()

        if char.isspace():
            braille_ascii += " "
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
                if opening_single_quote:
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
print('\n')

for word in braille_ascii.split():
    print('\n' + word)
    for x in range(3):
        for letter in word:
            cell = ord(letter) - 32
            print(braille[cell][x][0] + ' ' + braille[cell][x][1], end = "   ")
        print('')

print("\nEnd of the program\n")