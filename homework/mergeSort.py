def mergeSort(a, l, r):
    b = a
    #배열 a[]의 부분 배열 a[l:r]을 오름차순으로 정렬
    if r > l:
        mid = int ((r+l)/2)
        mergeSort(a, l, mid)
        mergeSort(a, mid+1, r)

        for i in range(mid+1, l, -1):
            b[i-1] = a[i-1]
        i-= 1

        for j in range(mid, r):
            b[r+mid-j] = a[j + 1]
        j+=1

        for k in range (l, r+1):
            if b[i] < b[j]:
                a[k] = b[i]
                i+=1
            else :
                a[k] = b[j]
                j -= 1



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
# O(nlogn) 의 결과를 확인할 수 있음
# N = 100,000 -> 0.628
# N = 200,000 -> 1.375
# N = 300,000 -> 2.093

N = 100000
a = []

a.append(-1)

for i in range(N):
    a.append(random.randint(1, N))

start_time = time.time()
mergeSort(a, 1, N)
end_time = time.time() - start_time

print("합병 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))

checkSort(a, N)