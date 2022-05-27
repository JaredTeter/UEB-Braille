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
text = 'It works'
braille_ascii = ''
opening_double_quote = True
opening_single_quote = True
print(f"\nUser input is: {text}\n")

for index, word in enumerate(text):
    # print(word)

    if word.isspace():
        braille_ascii += " "
    if 33 <= ord(word) <= 47 or 58 <= ord(word) <= 64:  # if character is a symbol
        if word == '!':
            braille_ascii += '6'
        elif word == '"':
            if opening_double_quote:
                braille_ascii += '8'
                opening_double_quote = False
            else:
                braille_ascii += '0'
                opening_double_quote = True
        elif word == '#':
            braille_ascii += '#'
        elif word == '$':
            braille_ascii += '@S'
        elif word == '%':
            braille_ascii += '.0'
        elif word == '&':
            braille_ascii += '@&'
        elif word == "'":
            if opening_single_quote:
                braille_ascii += ',8'
                opening_single_quote = False
            else:
                braille_ascii += ',0'
                opening_single_quote = False
        elif word == '(':
            braille_ascii += '"<'
        elif word == ')':
            braille_ascii += '">'
        elif word == '*':
            braille_ascii += '"9'
        elif word == '+':
            braille_ascii += '"6'
        elif word == ',':
            braille_ascii += '1'
        elif word == '-':
            braille_ascii += '-'
        elif word == '.':
            braille_ascii += '4'
        elif word == '/':
            braille_ascii += '_/'
        elif word == ':':
            braille_ascii += '3'
        elif word == ';':
            braille_ascii += '2'
        elif word == '>':
            braille_ascii += '">'
        elif word == '=':
            braille_ascii += '"7'
        elif word == '<':
            braille_ascii += '"<'
        elif word == '?':
            braille_ascii += '8'
        elif word == '@':
            braille_ascii += '@A'
    if word.isupper():  # add upercase symbol
        braille_ascii += ','
    if 97 <= ord(word.lower()) <= 122:  # if character is a letter
        braille_ascii += word.upper()
    if word.isnumeric():  # if character is a number
        if index == 0 or (index > 0 and not text[index - 1].isnumeric()):
            braille_ascii += '#'
        if word == '0':
            braille_ascii += 'J'
        else:
            braille_ascii += chr(ord(word) + 16)


for i in braille_ascii.split():
    print(i)
print('\n')

for t in braille_ascii:
    print(t)
    cell = ord(t) - 32
    print(braille[cell][0][0] + ' ' + braille[cell][0][1])
    print(braille[cell][1][0] + ' ' + braille[cell][1][1])
    print(braille[cell][2][0] + ' ' + braille[cell][2][1])
    print('\n')

print("\nEnd of the program\n")