"""
FizzBuzz問題

3の倍数の場合は「Fizz」（Bizz Buzzの場合は「Bizz」）、5の倍数の場合は「Buzz」、3の倍数かつ5の倍数の場合（すなわち15の倍数の場合）は「Fizz Buzz」
"""


for i in range(1, 100):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)