"""
２分探索法（再帰呼び出し版）

data = [1, 4, 5, 7, 9, 10, 16]
から
「９」の場所を見つけ出す
"""


def do_binary_search(data, target, lo, hi):
    """２分探索法（再帰呼び出し版）

    Args:
        data (list[int]): 検索対象の配列データ
        target (int): 検索する数値
        lo (int): 検索範囲の下限Index
        hi (int): 検索範囲の上限Index
    """
    mid = (lo + hi) // 2
    if data[mid] == target:
        print(f'data={data[mid]} => index={mid}')
        return
    elif data[mid] < target:
        lo = mid + 1
        do_binary_search(data, target, lo, hi)
    elif data[mid] > target:
        hi = mid - 1
        do_binary_search(data, target, lo, hi)
    return


if __name__ == '__main__':
    data = [1, 4, 5, 7, 9, 10, 16]
    lo = 0
    hi = len(data) - 1
    do_binary_search(data, 9, lo, hi)
