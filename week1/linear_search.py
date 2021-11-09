def linear_search(arr,n,key):
    for i in range(0,n):
      if(arr[i] == key):
        return i
    return -1
n = int(input("enter number of elements in array"))
arr = []
for i in range(0,n):
 ele = int(input("enter the array elements"))
 arr.append(ele)
print(arr)
key = int(input("enter the search element"))
ans = linear_search(arr , n, key)
if(ans == -1):
   print("element not found")
else:
   print("element found at position",ans+1)
