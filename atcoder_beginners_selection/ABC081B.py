def is_all_even(num_list):
    """リストの中身がすべて偶数がどうかチェックする
    """
    for num in num_list:
        if num % 2 != 0:
            return False
    return True

N = input()
list_ = list(map(int, input().split()))
cnt = 0
while is_all_even(list_):
    list_ = list(map(lambda x: x/2, list_))
    cnt += 1
print(cnt)