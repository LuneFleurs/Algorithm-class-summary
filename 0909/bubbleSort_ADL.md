BubbleSort(a[], n)

    for ( i <- n; i >= 1; i <- i-1) do {
        for ( j <- 1; j < i; j <- j+1) do {
           if ( a[j] > a[j+1] ) then A[j]와 A[j+1]을 교환;
        }
    }
end BubbleSort()