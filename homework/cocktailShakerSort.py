# Python program for implementation of Cocktail Sort

def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n-1
    print ("정렬 과정 : ")
    while (swapped==True):


        swapped = False
        # 큰것부터 정렬
        for i in range (start, end):
            if (a[i] > a[i+1]) :
                a[i], a[i+1]= a[i+1], a[i]
                swapped=True

        printArr(a)
        print()
        
        if (swapped==False):
            break

        swapped = False
        end = end-1
        #작은것부터 정렬
        for i in range(end-1, start-1,-1):
            if (a[i] > a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True

        start = start+1

        printArr(a)
        print()

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


def printArr(a) :
    n = len(a)
    for i in range(n):
        print ("%d" %a[i], end = '')



import time


a = [6, 5, 4, 3, 2, 1]
N = len(a)

start_time = time.time()
cocktailSort(a)
end_time = time.time() - start_time

print("칵테일 쉐이커 정렬의 실행 시간 (N=%d) : %0.10f"%(N, end_time))

checkSort(a, N-1)

# print("정렬 후 배열 :")
# for i in range(N):
#     print ("%d" %a[i], end = ''),


