n = int(input("Number: "))

if n < 0:
  print("Error")
else:
  sum = 0
  i = n
  while i > 0:
    sum += i
    i -= 1
  print(sum)