n=int(input())
print(1,end=" ")
for num in range(11,n+1):
  order = len(str(num))
  sum = 0
  temp = num
  while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
  if num == sum:
    print(num,end=" ")
