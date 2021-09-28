4. 회문을 판별하는 함수 isPalinedrome()

isPalindrome(s) 
    i <- 0;
    j <- len(s) - 1;
    while (i < j) do {
        if (s[i] != s[j]) 
            return false;
        i <- i + 1;
        j <- j - 1;
    } 
    return true;
end isPalindrome()