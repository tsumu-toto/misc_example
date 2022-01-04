"""
線形探索法（関数化・モジュール化対応版）

data = [7, 4, 2, 8, 10, 9, 1, 5, 3, 6]
から
「９」の場所を見つけ出す

if __name__ == '__main__'は「該当のファイルがコマンドラインからスクリプトとして実行された場合にのみ以降の処理を実行する」という意味となる。他のファイルからインポートされたときは処理は実行されない。
"""


def do_linear_search(data, target):
    """線形探索法

    Args:
        data (list[int]): 検索対象の配列データ
        target (int): 検索する数値
    """
    for i in range(len(data)):
        if data[i] == target:
            print(f'data={data[i]} => index={i}')


if __name__ == '__main__':
    data = [7, 4, 2, 8, 10, 9, 1, 5, 3, 6]
    do_linear_search(data, 9)
