def divisible(number):
  for i in range(2, 21):
    if number % i != 0:
      return False
  return True

number = 2
while True:
  if divisible(number):
    break
  number += 2

print(number)