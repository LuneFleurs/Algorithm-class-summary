maxb = 14

class bitskey:
    def __init__(self, x):
        self.x = x

    def get(self):
        return self.x

    def bits(self, k, j):
        return (self.x >> k) & ~(~0 << j)

class node:
    def __init__(self,key): 
        self.key = key
        self.b = None
        self.left = None
        self.right = None

class Dict:
    itemMin = bitskey(0)
    head = node(itemMin)
    head.b = maxb
    head.left = head.right = head

    def search(self, v) :
        v = bitskey(v)
        p = self.head
        x = self.head.left

        while p.b > x.b:
            p = x
            if self.bits(v, x.b, 1) :
                x = x.right
            else :
                x = x.left
        
        if  v.get() != x.key.get() :
            return self.itemMin
        
        return x.key

    def insert (self, v) :
        v = bitskey(v)
        i = maxb
        p = self.head
        t = self.head.left

        while p.b > t.b:
            p = t

            if self.bits(v, t.b, 1) :
                t= t.right
            else :
                t = t.left
        
        if v.get() == t.key.get() :
            return
        
        while self.bits(t.key, i, 1) == self.bits(v, i, 1) :
            i -= 1
        
        p = self.head
        x = self.head.left

        while p.b > x.b and x.b > i :
            p = x
            if self.bits(v, x.b, 1) :
                x = x.right
            else :
                x= x.left
        
        t = node(self.itemMin)
        t.key = v
        t.b = i

        if self.bits(v, t.b, 1) :
            t.left = x
            t.right = t
        else : 
            t.left = t
            t.right = x

        if self.bits(v, p.b, 1) :
            p.right = t
        else :
            p.left = t
    
    def bits(self, item, bit, cmp) :
        if item.bits(bit, 1) == cmp :
            return 1
        else : 
            return 0

    def check(self, search_key):
        x = p = self.head.right
        while (x != self.z):
            if x.color == 0:
                str_color = 'black'
            else:
                str_color = 'red'
            print('key : ', x.key, ', parents: ', p.key, ', color : ', str_color)
            p = x
            if x.key > search_key:
                x = x.left
            else:
                x = x.right


import random, time

# Auto input
N = 10000

key = list(range(1, N+1))
s_key = list(range(1, N+1))
random.shuffle(key)

d = Dict()

for i in range(N):
    d. insert(key[i])


# # Manual input
# N = 7
# d = Dict()

# # 직접 input 1, 19, 5, 18, 3, 26, 9
# key = int(input('키 : '))
# while key != 999:
#     d.insert(key)
#     d.check(key)
#     key = int(input('키 : '))

# s_key = list(range(1, 8))
# random.shuffle(key)

start_time = time.time()

for i in range(N) :
    result = d.search(s_key[i])
    if result.get() == -1 or result.get() != s_key[i]:
        print("탐색 오류")
    
end_time = time.time() - start_time
print('패트리샤 트리의 실행 시간 (N = %d) : %0.3f' %(N, end_time))
print('탐색 완료')