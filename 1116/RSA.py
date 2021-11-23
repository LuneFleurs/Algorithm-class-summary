def encipher (p, n, pk) :
    c = ''
    i = 0
    while i < len(p) :
        m = ''
        for j in range (4) :
            m += p[i+j]

        i += 4
        a = int(m)
        t = a

        for k in range (pk) :
            b = t % n
            t = a * b
        
        if b < 10 :
            c += '000' + str(b)
        elif b < 100 :
            c += '00' + str(b)
        elif b < 1000 :
            c += '0' + str(b)
        else :
            c += str(b)
    
    return c

def decipher(ciphertext, n, sk) :
    plainText = ''
    i = 0
    while i < len(ciphertext) :
        m = ''
        for j in range (4) :
            m += ciphertext[i+j]

        i += 4
        a = int(m)
        t = a

        for k in range (sk) :
            b = t % n
            t = a * b
        
        if b < 10 :
            plainText += '000' + str(b)
        elif b < 100 :
            plainText += '00' + str(b)
        elif b < 1000 :
            plainText += '0' + str(b)
        else :
            plainText += str(b)

    return plainText

def encode(p) :
    m = ''
    for i in range (len(p)) :
        a = ord(p[i])
        if a == 32 :
            a = 64
        
        a -= 64

        if a == 0:
            m += '00'
        elif a < 10:
            m += '0' + str(a)
        else :
            m += str(a)
    
    return m

plainText = 'SAVE PRIVATE RYAN '
N = 3713
S = 97  # 비밀키
P = 37  # 공개키
plainMessage = encode(plainText)
print ('평문 : ', plainMessage)
cipherMessage = encipher(plainMessage, N, P)
print ('암호문 : ', cipherMessage)
decipherMessage = decipher(cipherMessage, N, S)
print('복호화 후 : ', decipherMessage)