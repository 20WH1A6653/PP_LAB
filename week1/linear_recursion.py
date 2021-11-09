def linear_search(arr,n,key,i):
  if(i>=n):
    return 0
  elif(arr[i] == key):
    return i+1
  else:
    return linear_search(arr,n,key,i+1)
n = int(input("enter the number of elements in array"))
print("enter the array elements")
arr = []
for i in range(0,n):
   ele = int(input())
   arr.append(ele)
key = int(input("enter the search element"))
ans = linear_search(arr,n,key,0)
if(ans != 0):
 print("element found at position:",ans)
else:
 print("element not found")
