def lcs(a, b):
    """Longest common subsequence (string)."""
    dp = [[""] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            dp[i + 1][j + 1] = dp[i][j] + x if x == y else max(dp[i][j + 1], dp[i + 1][j], key=len)
    return dp[-1][-1]


def edit_distance(a, b):
    """Levenshtein distance, O(len(b)) memory."""
    prev = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        cur = [i]
        for j, y in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[-1] + 1, prev[j - 1] + (x != y)))
        prev = cur
    return prev[-1]


def knapsack(weights, values, cap):
    """0/1 knapsack, max total value."""
    dp = [0] * (cap + 1)
    for w, v in zip(weights, values):
        for c in range(cap, w - 1, -1):
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[cap]


def lis(a):
    """Length of the longest strictly increasing subsequence in O(n log n)."""
    from bisect import bisect_left
    tails = []
    for x in a:
        i = bisect_left(tails, x)
        tails[i:i + 1] = [x]
    return len(tails)


def coin_change(coins, amount):
    """Fewest coins to make `amount`, or -1."""
    dp = [0] + [float("inf")] * amount
    for a in range(1, amount + 1):
        dp[a] = min((dp[a - c] + 1 for c in coins if c <= a), default=float("inf"))
    return -1 if dp[amount] == float("inf") else dp[amount]
