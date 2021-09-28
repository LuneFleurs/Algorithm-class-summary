InsertionSort(a[], n)

    // 원소 v는 a[i], 1 <= i <= n,
    // 원소 v(=a[i], 1 <= i, 1 <= i <= n)를 부분배열 a[1 : i-1]에 오름차순 순으로 삽입

     for ( i <- 2; i <= n; i <- i+1 ) do { // 두 번째 원소 a[2]부터
        v <- a[i]; // v는 임시 저장공간
        j <- i;

        while ( a[j-1] > v ) do {
            a[j] <- a[j-1]; // a[j-1];
            j = j-1
        }

        a[j] <- v;  // v를 빈자리에 삽입
    }

end InsertionSort()