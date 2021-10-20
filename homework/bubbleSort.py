def bubbleSort(a, n):
    for i in range (n, 1, -1):
        for j in range (0, i-1, 1):
            if a[j] < a[j+1] :
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
            
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

a = [6, 5, 4, 3, 2, 1]
N = len(a)

start_time = time.time()
bubbleSort(a, N)
end_time = time.time() - start_time

print("버블 정렬의 실행 시간 (N=%d) : %0.10f"%(N, end_time))

checkSort(a, N)