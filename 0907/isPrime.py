def isPrime(a):
    i = 2
    while i <= a/2 :
        if a % i == 0 :
            return False
        i = i + 1
    return True

a = int(input('a = '))

print('최대공약수 : ', isPrime(a))