import sys

# 復号化表
CRYPT_DICT = {
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '10': ' ',
    '11': 'A',
    '12': 'B',
    '13': 'C',
    '14': 'D',
    '15': 'E',
    '16': 'F',
    '17': 'G',
    '18': 'H',
    '19': 'I',
    '20': 'J',
    '21': 'K',
    '22': 'L',
    '23': 'M',
    '24': 'N',
    '25': 'O',
    '26': 'P',
    '27': 'Q',
    '28': 'R',
    '29': 'S',
    '30': 'T',
    '31': 'U',
    '32': 'V',
    '33': 'W',
    '34': 'X',
    '35': 'Y',
    '36': 'Z',
    '37': ',',
    '38': '.',
    '39': '\n'
}

# 逆ポーランド記法計算
def decypto_text(text):
    result = []
    symbol = []
    for char in reversed(text.split()):
        if char in ['+', '-', '*', '/']:
            symbol.append(char)
        else:
            result.insert(0, char)
            if symbol:
                result.insert(0, symbol.pop())
    result = str(int(eval(''.join(result))))
    return result

before_txt = ""
for line in sys.stdin.readlines():
    txt = decypto_text(line)
    if txt in ['10', '37', '38', '39']:
        if before_txt != txt:
            print(CRYPT_DICT[txt], end='')
    else:
        print(CRYPT_DICT[txt], end='')
    before_txt = txt
print('\n', end='')
