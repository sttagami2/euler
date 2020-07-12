answer = 0
for i in range(100, 1000):
  for j in range(100, 1000):
    volume_list = list(str(i * j))
    volume = int(''.join(volume_list))
    reversal_list = list(reversed(volume_list))
    reversal = int(''.join(reversal_list))
    if volume == reversal:
      if answer < volume:
        answer = volume
print(answer)