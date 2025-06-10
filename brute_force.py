import time
import matplotlib.pyplot as plt

def knapsackRec(W, wt, vt, n):

    # Base case: no items left or no capacity left
    if W == 0 or n == 0:
        return 0
    
    pick = 0

    if wt[n-1] <= W:
        pick = vt[n-1] + knapsackRec(W - wt[n-1], wt, vt, n - 1)

    not_pick = knapsackRec(W, wt, vt, n - 1)

    return max(pick, not_pick)

def knapsackBruteForce(W, wt, vt):
    n = len(wt)
    return knapsackRec(W, wt, vt, n)


# Example usage:
# Benchmark and plotting
if __name__ == "__main__":
    # Base capacity
    W = 50

    # Sample item data (values and weights grow)
    weights = [10, 20, 30, 40, 15, 25, 35, 5]
    values = [60, 100, 120, 240, 50, 150, 210, 30]

    item_counts = []
    times = []
    max_values = []

    for i in range(1, len(weights) + 1):
        wt = weights[:i]
        vt = values[:i]

        start_time = time.time()
        max_value = knapsackBruteForce(W, wt, vt)
        end_time = time.time()

        elapsed_time = end_time - start_time

        item_counts.append(i)
        times.append(elapsed_time)
        max_values.append(max_value)

        print(f"{i} items: Value = {max_value}, Time = {elapsed_time:.4f} sec")

    # Plotting Time vs Number of Items
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(item_counts, times, marker='o')
    plt.title('Execution Time vs Number of Items')
    plt.xlabel('Number of Items')
    plt.ylabel('Time (seconds)')
    plt.grid(True)

    # Plotting Max Value vs Number of Items
    plt.subplot(1, 2, 2)
    plt.plot(item_counts, max_values, marker='o', color='green')
    plt.title('Max Value vs Number of Items')
    plt.xlabel('Number of Items')
    plt.ylabel('Max Value Obtained')
    plt.grid(True)

    plt.tight_layout()
    plt.show()