target = int(input())
n = int(input())
l = list(map(int, input().strip().split()))
index = -1
for i in range(n):
   if l[i] == target:
       index = i
       break
      
if index == -1:
   print("Target is not present")
else:
   print("Target is present at index:", index)
