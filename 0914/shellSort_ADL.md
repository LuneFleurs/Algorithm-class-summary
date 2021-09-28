shellSort(a[], n)
    for (h ← 1; 3×h+1 < n; h ← 3×h+1) do { }; // 첫 번째 h 값 계산
        for ( ; h > 0; h ← h/3) do { // h 값을 감소시키며 진행
            for (i ← h + 1; i ≤ n; i ← i+1) do {
                v ← a[i];
                j ← i;
                while (j > h and a[j-h] > v) do {
                    a[j] ← a[j-h];
                    j ← j-h;
                } // while
            a[j] ← v;
        } // for
    } // for
end shellSort()