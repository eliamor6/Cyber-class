import string
MORSE_CODE_DICT = { '.-': 'a', '-...':'b',
                    '-.-.':'c', '-..':'d', '.':'e',
                    '..-.':'f', '--.':'g', '....':'h',
                    '..':'i', '.---':'j', '-.-':'k',
                    '.-..':'l', '--':'m', '-.':'n',
                    '---':'o', '.--.':'p', '--.-':'q',
                    '.-.':'r', '...':'s', '-':'t',
                    '..-':'u', '...-':'v', '.--':'w',
                    '-..-':'x', '-.--':'y', '--..':'z', '/':' ', ' ': ''}
morse_code = open("E:\שולחן עבודה\אליה py\morse3.txt","r")
str=morse_code.read()
str = str.split()
str2 = ''
for letter in str:
    str2 = str2 + MORSE_CODE_DICT[letter]
letter_count = dict((key, 0) for key in string.ascii_lowercase)
print(letter_count)
for letter in letter_count:
    letter_count[letter] = str2.count(letter)
combo = {''.join(sorted(k for k in letter_count.keys() if letter_count[k] == v)): v for v in set(letter_count.values())}
print(combo)
for info in reversed(list(combo)):
    if combo[info] != 0:
        print(info , "-" , combo[info])