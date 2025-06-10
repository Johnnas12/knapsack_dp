import time

def knapsackDP(W, wt, vt, n):
    # initialize DP table
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build the table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], vt[i - 1] + dp[i - 1][w - wt[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


# Example usage:
if __name__ == "__main__":
    # Base capacity
    W = 50

    # Sample item data
    weights = [10, 20, 30, 40, 15, 25, 35, 5, 12, 18, 22, 28, 32, 38, 42, 48]
    values =  [60, 100, 120, 240, 50, 150, 210, 30, 55, 95, 110, 135, 160, 190, 205, 250]

    for i in range(1, len(weights) + 1):
        wt = weights[:i]
        vt = values[:i]
        n = len(wt)

        start_time = time.perf_counter()
        max_value = knapsackDP(W, wt, vt, n)
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time

        print(f"{i} items: Value = {max_value}, Time = {elapsed_time:.6f} sec")
