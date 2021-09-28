def selectionSort(a, n):
    for i in range (1, n) :
        minIndex = i;
        #더미키가 포함된 리스트기 때문에 마지막 인덱스가 n이 되므로 j의 범위가 n+1까지
        for j in range (i+1, n+1) :
            if a[j] < a[minIndex] :
                minIndex = j

        a[i], a[minIndex] = a[minIndex], a[i]
        #temp = a[i];
        #a[i] = a[minIndex]
        #a[minIndex] = temp

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
selectionSort(a, N)
end_time = time.time() - start_time

print("선택 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))

checkSort(a, N)