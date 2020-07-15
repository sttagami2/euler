# 100個の自然数の2乗の和
def addition(number):
  sum_additional = 0
  for i in range(1, number+1):
    sum_additional += i**2
  return sum_additional

# 100個の自然数の和の2乗
def multiplier(number):
  sum_multiplier = 0
  for i in range(1, number+1):
    sum_multiplier += i
  return sum_multiplier**2

number = 100
answer = multiplier(number) - addition(number)

print(answer)
