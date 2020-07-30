number = 2
answer = 0
max = []
while number <= 100:
  print(number)
  while number != 1:
    if number % 2 == 0:
      max.append(number)
      number /= 2
    else:
      max.append(number)
      number = (3 * number) + 1

  if answer < len(max):
    answer = len(max)
    max = []
  else:
    max = []

print(answer)
  
