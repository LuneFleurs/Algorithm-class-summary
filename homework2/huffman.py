class PQ:
    def __init__(self):
        self.heap = [0]*100
        self.info = [0]*100
        self.n = 0

    def insert(self, v, x):
        self.n += 1
        i = self.n
        while True:
            if i == 1: break
            if v >= self.heap[int(i/2)]: break
            self.heap[i] = self.heap[int(i/2)]
            self.info[i] = self.info[int(i/2)]
            i = int(i/2)
        self.heap[i] = v
        self.info[i] = x

    def remove(self):
        x = self.info[1]
        temp_v = self.heap[self.n]
        temp_x = self.info[self.n]
        self.n -= 1
        i = 1
        j = 2
        while j <= self.n:
            if (j < self.n) and (self.heap[j] > self.heap[j+1]):
                j += 1
            if temp_v <= self.heap[j]: break
            self.heap[i] = self.heap[j]
            self.info[i] = self.info[j]
            i = j
            j *= 2
        self.heap[i] = temp_v
        self.info[i] = temp_x
        return x

    def isEmpty(self):
        if self.n == 0: return True
        else: return False


def index(c):
    if ord(c) == 32: return 0
    else: return (ord(c)-64)


def makeHuffman(t, m):
    for i in range(m):
        count[index(t[i])] += 1
    
    # k, count, char
    for i in range(27) :
        if (count[i] != 0) :
            q_k.put(i)
            q_count.put(count[i])
            q_char.put(chr(i+64))

    for i in range(27):
        if count[i]:
            pq.insert(count[i], i)
    i = 27
    while not pq.isEmpty():
        t1 = pq.remove()
        t2 = pq.remove()
        dad[i] = 0
        dad[t1] = i
        dad[t2] = -i
        count[i] = count[t1] + count[t2]
        if not pq.isEmpty():
            pq.insert(count[i], i)
        i += 1
    
    # dad, code, length
    for k in range(27):
        i = x = 0
        j = 1
        if count[k]:
            q = dad[k]
            q_dad.put(q)
            while q:
                if q < 0:
                    x += j
                    q = -q
                q = dad[q]
                j += j
                i += 1
            
            q_code.put(x)
            q_len.put(i)

        code[k] = x
        length[k] = i


def encode(t, m):
    huffman_code = ''
    for j in range(m):
        i = length[index(t[j])]
        while i > 0:
            huffman_code += str((code[index(t[j])] >> i - 1) & 1)
            i -= 1
    return huffman_code


# count[k], dad[k]
def decode(dictionary, encodeText) :
    decoded_huffman = ''
    while encodeText:
        for k in dictionary:
            if encodeText.startswith(k):
                decoded_huffman += dictionary[k]
                encodeText = encodeText[len(k):]
    return decoded_huffman

import queue


text = 'VISION QUESTION ONION CAPTION GRADUATION EDUCATION'
# text = 'A SIMPLE STRING TO BE ENCODED USING A MINIMAL NUMBER OF BITS'

count = [0]*100
dad = [0]*100
length = [0]*27
code = [0]*27
M = len(text)
pq = PQ()

# 출력용 큐
q_k = queue.Queue()
q_char = queue.Queue()
q_count = queue.Queue()
q_dad = queue.Queue()
q_code = queue.Queue()
q_len = queue.Queue()

makeHuffman(text, M)

list_k = list(q_k.queue)
list_char = list(q_char.queue)
list_count = list(q_count.queue)
list_dad = list(q_dad.queue)
list_code = list(q_code.queue)
#print(list_code)
list_len = list(q_len.queue)
realSize = 0

for i in range(27) :
    if (count[i] != 0) :
        print ("k : " + str(q_k.get()) + "\tChar : " + str(q_char.get()) + "\tcount[k] : " + str(q_count.get()) + "\tdad[k] : " + str(q_dad.get()) + "\tcode[k] : " + str(q_code.get()) + "\tlength[k] : " + str(q_len.get()))
        realSize += 1

#print (realSize)

dictionary = {}
for i in range(realSize) :
    putZeroes = ''
    key = format(list_code[i], 'b')
    if len(key) < list_len[i] :
        for j in range (list_len[i] - len(key)):
            putZeroes += '0'
    key_len = putZeroes + key
    #print(key_len)
    val = list_char[i]
    dictionary['%s'%key_len] = '%s'%val

print("\ndictionary : ")
print(dictionary)

print()
print("original message : \n" + text)
print()
print("encoded message : \n" + encode(text, M))
print()
print("decoded message : \n" + decode(dictionary, encode(text, M)))