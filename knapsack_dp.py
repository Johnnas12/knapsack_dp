import time
import matplotlib.pyplot as plt

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

def knapsackBottomUp(W, wt, vt):
    n = len(wt)
    return knapsackDP(W, wt, vt, n)

# Example usage:
if __name__ == "__main__":
    # Base capacity
    W = 50

    # Sample item data (values and weights grow)
    weights = [10, 20, 30, 40, 15, 25, 35, 5, 12, 18, 22, 28, 32, 38, 42, 48]
    values = [60, 100, 120, 240, 50, 150, 210, 30, 55, 95, 110, 135, 160, 190, 205, 250]

    item_counts = []
    times = []
    max_values = []

    for i in range(1, len(weights) + 1):
        wt = weights[:i]
        vt = values[:i]
        n = len(wt)

        start_time = time.perf_counter()
        max_value = knapsackDP(W, wt, vt, n)
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time

        item_counts.append(i)
        times.append(elapsed_time)
        max_values.append(max_value)

        print(f"{i} items: Value = {max_value}, Time = {elapsed_time:.6f} sec")

    # Plotting Time vs Number of Items
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(item_counts, times, marker='o')
    plt.title('DP Execution Time vs Number of Items')
    plt.xlabel('Number of Items')
    plt.ylabel('Time (seconds)')
    plt.grid(True)

    # Plotting Max Value vs Number of Items
    plt.subplot(1, 2, 2)
    plt.plot(item_counts, max_values, marker='o', color='green')
    plt.title('Max Value vs Number of Items (DP)')
    plt.xlabel('Number of Items')
    plt.ylabel('Max Value Obtained')
    plt.grid(True)

    plt.tight_layout()
    plt.show()