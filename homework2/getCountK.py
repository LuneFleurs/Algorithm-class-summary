def index(c):
    if ord(c) == 32: return 0
    else: return (ord(c)-64)

def getCountK(t, m):
    for i in range(m):
        count[index(t[i])] += 1

    # count[k] 출력용
    print("1. count[k] 출력")
    print("@ = space")
    for i in range(27) :
        # 없는거 출력하면 너무 길어서 일부만 출력
        if (count[i] != 0) :
            print(chr(i+64), end = ' : ')
            print(count[i])


#text = 'THIS IS TEST TEXT'
text = 'A SIMPLE STRING TO BE ENCODED USING A MINIMAL NUMBER OF BITS'
count = [0]*100

getCountK(text, len(text))