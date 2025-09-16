# BIG_O


## O(1)	Constant

```java
  FindMin(x, y) {
    if (x < y) {
        return x
    }
    else {
        return y
    }
  }
```

## O(log N)	Logarithmic

```java
  BinarySearch(numbers, N, key) {
    mid = 0
    low = 0
    high = N - 1

    while (high >= low) {
        mid = (high + low) / 2
        if (numbers[mid] < key) {
          low = mid + 1
        }
        else if (numbers[mid] > key) {
          high = mid - 1
        }
        else {
          return mid
        }
    }

    return -1   // not found
  }
```

## O(N)	Linear

```java
  LinearSearch(numbers, numbersSize, key) {
    for (i = 0; i < numbersSize; ++i) {
        if (numbers[i] == key) {
          return i
        }
    }

    return -1 // not found
  }
```

## O(N log N)	Linearithmic

```java
  MergeSort(numbers, i, k) {
    j = 0
    if (i < k) {
        j = (i + k) / 2              // Find midpoint

        MergeSort(numbers, i, j)     // Sort left part
        MergeSort(numbers, j + 1, k) // Sort right part
        Merge(numbers, i, j, k)      // Merge parts
    }
  }
```

## O(N)	Quadratic

```java
  SelectionSort(numbers, numbersSize) {
    for (i = 0; i < numbersSize; ++i) {
        indexSmallest = i
        for (j = i + 1; j < numbersSize; ++j) {
          if (numbers[j] < numbers[indexSmallest]) {
              indexSmallest = j
          }
        }

        temp = numbers[i]
        numbers[i] = numbers[indexSmallest]
        numbers[indexSmallest] = temp
    }
  }
```

## O(c)	Exponential

```java
  Fibonacci(N) {
    if ((1 == N) || (2 == N)) {
      return 1
    }
    return Fibonacci(N-1) + Fibonacci(N-2)
  }
```
