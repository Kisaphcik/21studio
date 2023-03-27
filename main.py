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
while b != '=':
    print(bisearch(b))
    b = input()
