length = 20
side = 20
total_path = length + side
numerator = 1
denominator1 = 1
denominator2 = 1

for x in range(total_path):
  numerator *= x+1

for y in range(length):
  denominator1 *= y+1

for z in range(side):
  denominator2 *= z+1

answer = numerator / (denominator1 * denominator2)

print(int(answer))