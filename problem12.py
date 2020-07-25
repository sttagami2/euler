triangle_number = [1]

while sum(divisors) < 500:
  divisors = []
  divide_number = 1
  while sum(triangle_number) >= divide_number:
    if sum(triangle_number) % divide_number == 0:
      divisors.append(divide_number)
    divide_number += 1
  triangle_number.append(triangle_number[-1] + 1)

print(sum(triangle_number))
print(divisors)