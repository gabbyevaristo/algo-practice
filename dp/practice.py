def fibonacci_iterative(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


def fibonacci_recursive(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_dp(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    dp = {}
    dp[1], dp[2] = 0, 1
    return fibonacci_helper(n, dp)

def fibonacci_helper(n, dp):
    if n not in dp:
        dp[n] = fibonacci_helper(n - 1, dp) + fibonacci_helper(n - 2, dp)
    return dp[n]


def coin_change(n, coins):
    coins.sort()
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, len(dp)):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i - coin] + 1, dp[i])
    return dp[n] if dp[n] != float('inf') else -1


def helper(target, coins):
    array = [0] * (target + 1)
    for x in range(len(array)):
        if x > 0:
            array[x] = target

    for i in range(1, len(array)):
        for j in range(len(coins)):
            if i - coins[j] >= 0:
                array[i] = min(array[i - coins[j]] + 1, array[i])
                minimum = array[i]
    return minimum



# n = 7
# print(fibonacci_iterative(n))
# print(fibonacci_recursive(n))
# print(fibonacci_dp(n))

change, coins = 31, [1,10,25]
# print(coin_change(change, coins))
print(helper(change, coins))
