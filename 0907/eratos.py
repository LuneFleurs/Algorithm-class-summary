def eratos(a, n) :
    a[1] = 0    # 첫번째 1은 소수가 아님
    i = 2
    while i <= n/2 :
        j = 2
        while i * j <= n :
            a[i*j - 1] = 0;
            j = j + 1 
        i = i + 1 
    return a

n = int(input('n = '))
a = list(range(n+1))
res = eratos(a, n)

for i in range (n+1):
    if res[i]:
        print(res[i], end = ' ')