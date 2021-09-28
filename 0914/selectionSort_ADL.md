selectionSort(a[], n)
    for (i <-1; i < n; i <- i +1) do {
        minIndex <- i;
        for (j <- i + 1; i <= n; j <- j+1) do {
            if (a[j] < a[minIndex])
                then minIndex <- j;
        }
        temp = a[i];
        a[i] = a[minIndex];
        a[minIndex] = temp;
    }
end selectionSort()