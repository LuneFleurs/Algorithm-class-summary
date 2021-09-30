class node:
    def __init__ (self, key = None) :
        self.key = key
    

class Dict:
    def __init__ (self) :
        Dict.a = []

    def search(self, search_key) :
        i = 0
        n = len(Dict.a)

        while i < n and Dict.a[i].key != search_key:
            i += 1
        if i == n:
            return -1
        else :
            return i
    
    def insert(self, v) :
        Dict.a.append(node(v))

import random, time

# N 의 값에 5000 1000 15000 넣어 비교
# O(n) 의 결과를 확인할 수 있음 O(n)을 n번 반복
# 알고리즘 문제로 n^2 정도로 나옴
# TODO 어떻게 하면 n으로 줄일 수 있을지 생각해볼것
# N = 3,000 -> 0.473
# N = 6,000 -> 3.654
# N = 9,000 -> 7.110

N = 9000
a = []

key = list(range (1, N+1))
s_key = list(range(1, N+1))

random.shuffle(key)

d = Dict()

for i in range(N) :
    d.insert (key[i])

start_time = time.time()

for i in range(N) :
    result = d.search(s_key[i])
    if result == -1 or key[result] != s_key[i]:
        print ('탐색 오류')
        
end_time = time.time() - start_time

print("순차 탐색의 실행 시간 (N=%d) : %0.3f"%(N, end_time))
