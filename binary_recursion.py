def binary_search(arr,n,low,high,key):
    mid = (low + high) // 2
    if(low > high):
       return 0
    if(arr[mid] == key):
      return mid+1
    elif(arr[mid] < key):
      low = mid+1
    elif(arr[mid] > key):
      high = mid-1
    else:
      return binary_search(arr,n,low,high,key)
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
if(ans!=0):
 print("element found at position",ans)
else:
 print("element not found")





