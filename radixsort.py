def countingSort(arr,P):
    n=len(arr)
    res=[0]*n
    c=[0]*10
    for i in range(0,n):
        temp=arr[i]//P
        c[temp%10]+=1
    for i in range(1,10):
        c[i]=c[i]+c[i-1]
    i = n - 1
    while i >= 0:
      temp = arr[i]//P
      res[c[temp % 10]-1]= arr[i]
      c[temp % 10]-=1
      i = i- 1
    for i in range(0,n):
            arr[i] = res[i]

def RadixSort(arr):
    maximum = max(arr)
    p=1
    while maximum // p > 0:
        countingSort(arr,p)
        p = p*10
