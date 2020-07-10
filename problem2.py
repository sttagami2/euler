fibonacchinums = [1,2]
fibonacchiLastNum = fibonacchinums[-2] + fibonacchinums[-1]
while fibonacchiLastNum <= 4*10**6:
  fibonacchinums.append(fibonacchiLastNum)
  fibonacchiLastNum = fibonacchinums[-2] + fibonacchinums[-1]

total = 0
for number in fibonacchinums:
  if number%2 == 0:
    total += number

print(total) 