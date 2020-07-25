import numpy as np


if __name__ == '__main__':
  src = '''
  08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
  49 49 99 ...
  ''' # too long

  ROW = 20
  COLUMN = 20
  DIMENSION = 4
  greatest_product = 0

  src = src.replace('\n', '').split(' ')
  src = filter(lambda i: i != '', src)
  src = np.array(src).reshape(ROW, COLUMN)
  src = np.append(src, np.zeros((DIMENSION - 1, COLUMN)), axis=0)

  for i in range(0, ROW - DIMENSION + 1):
    for j in range(0, COLUMN - DIMENSION + 1):
      dest = src[i:i + DIMENSION, j:j + DIMENSION]
      h_product  = reduce(lambda x, y: int(x) * int(y), dest[0])
      v_product  = reduce(lambda x, y: int(x) * int(y), dest.T[0])
      d_product  = reduce(lambda x, y: int(x) * int(y), np.diag(dest))
      rd_product = reduce(lambda x, y: int(x) * int(y), np.diag(dest[::, ::-1]))

      greatest_product = max([h_product, v_product, d_product, rd_product, greatest_product])

  print('greatest product is %d' % greatest_product)