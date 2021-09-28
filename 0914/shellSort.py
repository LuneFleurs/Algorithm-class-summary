def shellSort(a, n):
    h = 1
    while 3*h + 1 < n :
        while h > 0:
            for i in range (h+1, n):
                v = a[i]
                j = i
                while j > h and a[j-h] > v :
                    a[j] = a[j-h]
                    j = j-h
            a[j] = v
            h = h//3
        h = h * 3 + 1

    return a

def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if a[i] > a[i+1]:
            isSorted = False
        if not isSorted:
            break

    if isSorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")



import random, time

# N 의 값에 5000 1000 15000 넣어 비교
# O(n^2) 의 결과를 확인할 수 있음
# N = 5000 -> 0.924
# N = 10000 -> 3.911
# N = 15000 -> 8.782

N = 15000
a = []

a.append(None)

for i in range(N):
    a.append(random.randint(1, N))

start_time = time.time()
shellSort(a, N)
end_time = time.time() - start_time

print("선택 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))

checkSort(a, N)