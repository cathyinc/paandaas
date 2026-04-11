def display5():
    code = '''def minEatingSpeed(piles, H):
    def can_eat_all_bananas(S):
        hours = 0
        for pile in piles:
            hours += pile // S
            if pile % S != 0:
                hours += 1
            if hours > H:
                return False
        return True

    left, right = 1, max(piles)

    while left < right:
        mid = (left + right) // 2
        if can_eat_all_bananas(mid):
            right = mid
        else:
            left = mid + 1

    return left


piles = [3, 6, 7, 11]
H = 8
print(minEatingSpeed(piles, H))'''
    print(code)
