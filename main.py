morse = {'A': '.-', 'B': '-...', 'C': '-.-.',
         'D': '-..', 'E': '.', 'F': '..-.',
         'G': '--.', 'H': '....', 'I': '..',
         'J': '.---', 'K': '-.-', 'L': '.-..',
         'M': '--', 'N': '-.', 'O': '---',
         'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-',
         'V': '...-', 'W': '.--', 'X': '-..-',
         'Y': '-.--', 'Z': '--..', ' ': '\t'}
rev_morse = {'.-': 'A', '-...': 'B', '-.-.': 'C',
             '-..': 'D', '.': 'E', '..-.': 'F',
             '--.': 'G', '....': 'H', '..': 'I',
             '.---': 'J', '-.-': 'K', '.-..': 'L',
             '--': 'M', '-.': 'N', '---': 'O',
             '.--.': 'P', '--.-': 'Q', '.-.': 'R',
             '...': 'S', '-': 'T', '..-': 'U',
             '...-': 'V', '.--': 'W', '-..-': 'X',
             '-.--': 'Y', '--..': 'Z', '\t': ' '}

n = input("Выберите, что хотите сделать: 1 - с английского на морзе, 2 - с морзе на английский, ! - остановить.")
while n != '!':
    if int(n) == 1:
        s = input()
        for i in s:
            print(morse[i], end=' ')
        print()
    elif int(n) == 2:
        s = input()
        k = s.split(sep=' ')
        for i in k:
            print(rev_morse[i], end='')
        print()
    n = input('Выберите, что хотите сделать:')
