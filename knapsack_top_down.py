import time 
import matplotlib.pyplot as plt

def knapsackTopDown(W, wt, vt, n, memo):
    if n == 0 or W == 0:
        return 0

    if (n, W) in memo:
        return memo[(n, W)]

    if wt[n-1] <= W:
        pick = vt[n-1] + knapsackTopDown(W - wt[n-1], wt, vt, n-1, memo)
        not_pick = knapsackTopDown(W, wt, vt, n-1, memo)
        memo[(n, W)] = max(pick, not_pick)
    else:
        memo[(n, W)] = knapsackTopDown(W, wt, vt, n-1, memo)

    return memo[(n, W)]


def knapsackTopDownWrapper(W, wt, vt):
    n = len(wt)
    memo = {}
    return knapsackTopDown(W, wt, vt, n, memo)

if __name__ == "__main__":
    W = 50
    weights = [10, 20, 30, 40, 15, 25, 35, 5]
    values  = [60, 100, 120, 240, 50, 150, 210, 30]

    item_counts = []
    top_down_times = []
    max_values = []

    for i in range(1, len(weights)+1):
        wt = weights[:i]
        vt = values[:i]

        item_counts.append(i)

        start_time = time.perf_counter()
        max_value = knapsackTopDownWrapper(W, wt, vt)
        elapsed_time = time.perf_counter() - start_time

        top_down_times.append(elapsed_time)
        max_values.append(max_value)

        print(f"{i} items: Value = {max_value}, Time = {elapsed_time:.6f} sec")

    # Plotting Benchmark Results
    plt.figure(figsize=(12, 5))

    # Execution Time vs Number of Items
    plt.subplot(1, 2, 1)
    plt.plot(item_counts, top_down_times, marker='o', color='purple')
    plt.xlabel('Number of Items')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Top-down DP: Execution Time vs Number of Items')
    plt.grid(True)

    # Max Value vs Number of Items
    plt.subplot(1, 2, 2)
    plt.plot(item_counts, max_values, marker='o', color='green')
    plt.xlabel('Number of Items')
    plt.ylabel('Max Value Obtained')
    plt.title('Top-down DP: Max Value vs Number of Items')
    plt.grid(True)

    plt.tight_layout()
    plt.show()