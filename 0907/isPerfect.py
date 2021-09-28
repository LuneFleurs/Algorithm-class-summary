def isPerfect(a):
    s = 0
    i = 1
    while i <= a/2 :
        if a % i == 0 :
            s = s + i
        i = i + 1
    if s == a :
        return True
    else :
        return False
    

a = int(input('a = '))

print('완전수여부 : ', isPerfect(a))