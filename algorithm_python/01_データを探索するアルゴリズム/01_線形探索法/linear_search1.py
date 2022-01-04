"""
線形探索法

data = [7, 4, 2, 8, 10, 9, 1, 5, 3, 6]
から
「９」の場所を見つけ出す
"""

data = [7, 4, 2, 8, 10, 9, 1, 5, 3, 6]

for i in range(len(data)):
    if data[i] == 9:
        print(f'index={i}, data={data[i]}')
