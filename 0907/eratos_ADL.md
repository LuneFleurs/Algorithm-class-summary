5. 에라토스테네스의 체를 이용한 소수를 판별하는 함수 eratos()
입력 : 리스트 a (0~N)
반환 : 소수만 0이 아닌 리스트 a

eratos(a[], n) 
    a[1] <- 0;
    i <- 2;
    while (i <= n/2) do {
        j <- 2
        while (i * j <= n) do {
            a[i*j] <- 0;
            j <- j + 1
        } 
        i <- i + 1
    } 
    return a;
end eratos()