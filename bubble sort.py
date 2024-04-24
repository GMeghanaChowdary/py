n = int(input())
l = list(map(int, input().split()))


fixThis = n - 1
while fixThis > 0:
   for index in range(fixThis):
       if l[index] > l[index + 1]:
           l[index], l[index + 1] = l[index + 1], l[index]
   fixThis -= 1
print(*l)
