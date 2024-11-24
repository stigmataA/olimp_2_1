P, M, K, X, Z = map(int, input().split())

def calculate_days_to_reach_z(P, M, K, X, Z):
    mushrooms = X
    days = 2

    while mushrooms < Z:
        days += 1
        mushrooms += K

        if days % 7 == 6:
            mushrooms -= P

        if days % 7 == 0:
            mushrooms -= M

        if days > 1e6:
            return -1

    return days


result = calculate_days_to_reach_z(P, M, K, X, Z)
print(result)

