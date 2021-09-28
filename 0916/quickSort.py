def quickSort(a, l, r):
    #배열 a[]의 부분 배열 a[l:r]을 오름차순으로 정렬
    if r > l:
        #i = partition(a, l, r);
        # partition 함수 직접 구현
        v, i, j = a[r], l-1, r

        while True:
            i += 1
            while a[i] < v:
                i += 1
            j -= 1
            while a[j] > v:
                j -= 1
            if i >= j:
                break
            a[i], a[j] = a[j], a[i]
        a[i], a[r] = a[r], a[i]

        quickSort(a, l, i-1);
        quickSort(a, i+1, r);

    #print(a)

def partition (arr, low, high):
    # pivot (Element to be placed at right position)
    pivot = arr[high];  
 
    i = (low - 1)  # Index of smaller element and indicates the 
                   # right position of pivot found so far

    for j in range(low, high - 1):
        # If current element is smaller than the pivot
        if arr[j] < pivot:
            i += 1    # increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return (i + 1)


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
# N = 100,000 -> 0.264
# N = 200,000 -> 0.587
# N = 300,000 -> 0.930

N = 300000
a = []

a.append(-1)

for i in range(N):
    a.append(random.randint(1, N))

start_time = time.time()
quickSort(a, 1, N)
end_time = time.time() - start_time

print("선택 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))

checkSort(a, N)