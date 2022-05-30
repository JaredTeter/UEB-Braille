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
text = 'Have some more.'
braille_ascii = ''
opening_double_quote = True
opening_single_quote = True
print(f"\nUser input is: {text}\n")

for word in text.split():
    braille_ascii += ' '

    if 'but' == word.lower():
        braille_ascii += 'B'
        continue
    elif 'can' == word.lower():
        braille_ascii += 'C'
        continue
    elif 'do' == word.lower():
        braille_ascii += 'D'
        continue
    elif 'every' == word.lower():
        braille_ascii += 'E'
        continue
    elif 'from' == word.lower():
        braille_ascii += 'F'
        continue
    elif 'go' == word.lower():
        braille_ascii += 'G'
        continue
    elif 'have' == word.lower():
        braille_ascii += 'H'
        continue
    elif 'just' == word.lower():
        braille_ascii += 'J'
        continue
    elif 'knowledge' == word.lower():
        braille_ascii += 'K'
        continue
    elif 'like' == word.lower():
        braille_ascii += 'L'
        continue
    elif 'more' == word.lower():
        braille_ascii += 'M'
        continue
    elif 'not' == word.lower():
        braille_ascii += 'N'
        continue
    elif 'people' == word.lower():
        braille_ascii += 'P'
        continue
    elif 'quite' == word.lower():
        braille_ascii += 'Q'
        continue
    elif 'rather' == word.lower():
        braille_ascii += 'R'
        continue
    elif 'so' == word.lower():
        braille_ascii += 'S'
        continue
    elif 'that' == word.lower():
        braille_ascii += 'T'
        continue
    elif 'us' == word.lower():
        braille_ascii += 'U'
        continue
    elif 'very' == word.lower():
        braille_ascii += 'V'
        continue
    elif 'will' == word.lower():
        braille_ascii += 'W'
        continue
    elif 'it' == word.lower():
        braille_ascii += 'X'
        continue
    elif 'you' == word.lower():
        braille_ascii += 'Y'
        continue
    elif 'as' == word.lower():
        braille_ascii += 'Z'
        continue

    for index, char in enumerate(word):
        # print(char)

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
        if char.isupper():  # add upercase symbol
            braille_ascii += ','
        if 97 <= ord(char.lower()) <= 122:  # if character is a letter
            braille_ascii += char.upper()


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