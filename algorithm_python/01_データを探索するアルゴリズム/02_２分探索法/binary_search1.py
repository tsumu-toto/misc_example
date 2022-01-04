"""
２分探索法（While版）

data = [1, 4, 5, 7, 9, 10, 16]
から
「９」の場所を見つけ出す
"""


def do_binary_search(data, target):
    """２分探索法（While版）

    Args:
        data (list[int]): 検索対象の配列データ
        target (int): 検索する数値
    """
    lo = 0
    hi = len(data) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if data[mid] == target:
            print(f'data={data[mid]} => index={mid}')
            break
        elif data[mid] < target:
            lo = mid + 1
        elif data[mid] > target:
            hi = mid - 1
    return


if __name__ == '__main__':
    data = [1, 4, 5, 7, 9, 10, 16]
    do_binary_search(data, 9)
