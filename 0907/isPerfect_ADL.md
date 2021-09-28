3. 완전수를 판별하는 함수 isPerfect()

isPerfect(a) 
    s <- 0;
    i <- 1;
    while (i <= a/2) do {
        if (a mod i = 0) 
            then s <- s + i;
        i <- i + 1;
    } 
    if (s = a)
        then return true;
        else return false;
end isPerfect()