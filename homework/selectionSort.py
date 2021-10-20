def selectionSort(a):
    n = len(a)
    for i in range (n-1) :
        minIndex = i;
        #더미키가 포함된 리스트기 때문에 마지막 인덱스가 n이 되므로 j의 범위가 n+1까지
        for j in range (i+1, n) :
            if a[j] > a[minIndex] :
                minIndex = j

        a[i], a[minIndex] = a[minIndex], a[i]
        printArr(a)
        print()
    return a



def checkSort(a, n):
    isSorted = True
    for i in range(1, n-1):
        if a[i] < a[i+1]:
            isSorted = False
        if not isSorted:
            break

    if isSorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")


    
def printArr(a) :
    n = len(a)
    for i in range(n):
        print ("%d" %a[i], end = '')


import time


a = [3, 1, 2, 4, 5, 6]
N = len(a)

start_time = time.time()
selectionSort(a)
end_time = time.time() - start_time

print("선택 정렬의 실행 시간 (N=%d) : %0.10f"%(N, end_time))

checkSort(a, N)