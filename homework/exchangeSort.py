# 0번째 인덱스부터 
def exchangeSort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(i+1, n):
            if(a[i] < a[j]):
                a[i], a[j]=a[j], a[i]
            
        printArr(a)
        print()
    return a

# # 마지막 인덱스부터 
# def exchangeSort(a):
#     n=len(a)
#     for i in range(n-1, 0, -1):
#         for j in range(i, -1, -1):
#             if(a[i] > a[j]):
#                 a[i], a[j]=a[j], a[i]
            
#         printArr(a)
#         print()
#     return a

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

a = [3, 1, 2, 4, 6, 5]
N = len(a)

start_time = time.time()
exchangeSort(a)
end_time = time.time() - start_time

print("교환 정렬의 실행 시간 (N=%d) : %0.10f"%(N, end_time))

checkSort(a, N)