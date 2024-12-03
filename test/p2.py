def f(arr):
    arr.sort()
    for i in range(0, len(arr)-1):
        if arr[0] != arr[1]:
            x = arr[0]
        if (arr[i] != arr[i + 1] and
            arr[i] != arr[i - 1]):
            x = arr[i]
        if arr[i - 2] != arr[i - 1]:
            x = arr[i-2]
    return x 
 


if __name__ == "__main__": 
   print(f([7,7,8,7,7,7,7,7]))