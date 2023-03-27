import pymorphy2

morph = pymorphy2.MorphAnalyzer()
num = [i for i in range(0, 101)]
print(num[len(num) // 2])


def bisearch(dif):
    global num
    if len(num) > 1:
        if dif == '<':
            num = num[0:len(num) // 2]
            return num[len(num) // 2]
        elif dif == '>':
            num = num[(len(num) // 2) + 1:]
            return num[len(num) // 2]
    else:
        print(num[0])


b = input()
c = 1
while b != '=':
    c += 1
    print(bisearch(b))
    b = input()
word = morph.parse('попытку')[0]
print(f'Я угадала за {c} {word.make_agree_with_number(c).word}, ваше число - {num[len(num) // 2]}')
