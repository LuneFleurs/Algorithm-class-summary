2. 소수 구하는 함수 isPrime()

isPrime(a) 
    i <- 2;
    while (i <= a/2) do {
        if (a mod i = 0) 
            then return false;
        i <- i + 1
    } 
    return true;
end isPrime()