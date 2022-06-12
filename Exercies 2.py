#1
MORSE_CODE_DICT = { '.-': 'a', '-...':'b',
                    '-.-.':'c', '-..':'d', '.':'e',
                    '..-.':'f', '--.':'g', '....':'h',
                    '..':'i', '.---':'j', '-.-':'k',
                    '.-..':'l', '--':'m', '-.':'n',
                    '---':'o', '.--.':'p', '--.-':'q',
                    '.-.':'r', '...':'s', '-':'t',
                    '..-':'u', '...-':'v', '.--':'w',
                    '-..-':'x', '-.--':'y', '--..':'z', '/':' ', ' ': ''}
#morse_code = open("E:\שולחן עבודה\אליה py\morse-err1.txt","r")
morse_code = open("E:\שולחן עבודה\אליה py\morse3.txt","r")
str=morse_code.read()
str = str.split()
str2 = ''
try:
    for letter in str:
        str2 = str2 + MORSE_CODE_DICT[letter]
    print(str2)
except:
    print("Error in Morse Code")