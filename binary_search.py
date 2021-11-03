def binary_search(arr,n,low,high,key):
  while(low <= high):
    mid = (low + high) // 2
    if(arr[mid] == key):
      return mid+1
    elif(arr[mid] < key):
      low = mid+1
    else:
      high = mid-1
  return -1
n = int(input("enter number of array elements"))
print("enter array elements")
arr = []
for i in range(0,n):
  ele = int(input())
  arr.append(ele)
arr.sort()
print(arr)
key = int(input("enter search key"))
ans = binary_search(arr,n,0,n-1,key)
if(ans == -1):
 print("element not found")
else:
 print("element found at position:",ans)


