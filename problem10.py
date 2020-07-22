number = 2000000                  # 素因数分解する数
divisor = 2                       # 素因数の初期値
primeFactors = []                 # 素因数を格納する変数

while divisor**2 <= number:       # 素因数の2乗が素因数分解する数より小さい場合下記実行
  while number % divisor == 0:    # 素因数で徐算した際に余りが無い場合下記実行
    number //= divisor            # 素因数分解する数を更新
    primeFactors.append(divisor)  # 素因数を変数に格納
  divisor += 1                    # 素因数を更新


if number > 1:                    # 素因数の最大値を格納するためのもの
  primeFactors.append(number)

print(sum(primeFactors))
