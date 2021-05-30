if __name__ == '__main__':
    N = input()
    cards = list(map(int, input().split()))
    cards_sorted = sorted(cards, reverse=True)

    Alice = []
    Bob = []
    while len(cards_sorted) > 0:
        if len(Alice) <= len(Bob):
            Alice.append(cards_sorted.pop(0))
        else:
            Bob.append(cards_sorted.pop(0))
    print(sum(Alice) - sum(Bob))