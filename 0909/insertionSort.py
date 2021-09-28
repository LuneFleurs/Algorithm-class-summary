def insertionSort(a, n):
    for i in range (2, n): # 두 번째 원소 a[2]부터
        v = a[i]; 
        j = i;

        while a[j-1] > v :
            a[j] = a[j-1];
            j = j-1
        a[j] = v;
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
# N = 5000 -> 2.287
# N = 10000 -> 9.229
# N = 15000 -> 20.383

N = 5000
a = []

a.append(None)

for i in range(N):
    a.append(random.randint(1, N))

start_time = time.time()
insertionSort(a, N)
end_time = time.time() - start_time

print("선택 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))

checkSort(a, N)