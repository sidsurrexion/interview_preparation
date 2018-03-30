def minimum_coin_change(total_cost, coins):
    c = [[0] * len(coins) for i in range(total_cost+1)]
    for i in range(total_cost):
        c[0][i] = int(i/coins[0])
    for i in range(1, len(coins)):
        for j in range(total_cost+1):
            if coins[i] > j:
                c[i][j] = c[i-1][j]
            else:
                div = int(j/coins[i])
                if div + c[i][j % coins[i]] < c[i-1][j]:
                    c[i][j] = div + c[i][j % coins[i]]
    return c[len(coins) - 1][len(total_cost)]


def init_change():
    pass
