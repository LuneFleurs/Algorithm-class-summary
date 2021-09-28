def binarySearch(a, key, left, right):
    # a[mid] = key 인 인덱스 mid를 반환
    if(left <= right) :
        mid = (left + right) // 2;

        if (key == a[mid]) :
            return mid
        elif (key < a[mid]) :
            print("key : ", key, " left : ", left, " mid : ", mid, " right : ", right)
            return binarySearch(a, key, left, mid-1)
        elif (key > a[mid]) :
            print("key : ", key, " left : ", left, " mid : ", mid, " right : ", right)
            return binarySearch(a, key, mid+1, right)
    else :
        return -1

arr = list(range(100))

print (binarySearch(arr, 64, 0, len(arr)))