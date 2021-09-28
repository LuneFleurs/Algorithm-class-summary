1. 최대 공약수 구하는 함수 gcd()

gcd(a, b) 
    i <- 1;
    while (i <= a and i <= b) do {
        if (a mod i = 0 and b mod i = 0 ) 
            then g <- i;
        i <- i + 1
    } 
    return g;
end gcd()