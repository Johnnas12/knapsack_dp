import time
import matplotlib.pyplot as plt
import random

from brute_force import knapsackBruteForce
from knapsack_dp import knapsackBottomUp
from knapsack_top_down import knapsackTopDownWrapper

# Benchmarking with small dataset
# W = 50
# weights = [10, 20, 30, 40, 15, 25, 35, 5]
# values = [60, 100, 120, 240, 50, 150, 210, 30]


W = 500
weights = [random.randint(1, 50) for _ in range(20)]
values = [random.randint(10, 500) for _ in range(20)]

item_counts = list(range(1, len(weights)+1))
times_brute, times_bottom, times_topdown = [], [], []
values_brute, values_bottom, values_topdown = [], [], []

print("Benchmarking Results:\n")

for i in item_counts:
    wt, vt = weights[:i], values[:i]

    # Brute-force
    start = time.perf_counter()
    val_brute = knapsackBruteForce(W, wt, vt)
    elapsed_brute = time.perf_counter() - start
    times_brute.append(elapsed_brute)
    values_brute.append(val_brute)

    # Bottom-up DP
    start = time.perf_counter()
    val_bottom = knapsackBottomUp(W, wt, vt)
    elapsed_bottom = time.perf_counter() - start
    times_bottom.append(elapsed_bottom)
    values_bottom.append(val_bottom)

    # Top-down DP
    start = time.perf_counter()
    val_topdown = knapsackTopDownWrapper(W, wt, vt)
    elapsed_topdown = time.perf_counter() - start
    times_topdown.append(elapsed_topdown)
    values_topdown.append(val_topdown)

    print(f"{i} items:")
    print(f"  Brute Force    -> Value: {val_brute}, Time: {elapsed_brute:.6f} sec")
    print(f"  Bottom-Up DP   -> Value: {val_bottom}, Time: {elapsed_bottom:.6f} sec")
    print(f"  Top-Down DP    -> Value: {val_topdown}, Time: {elapsed_topdown:.6f} sec")
    print("-" * 50)

# Plotting the benchmark
plt.figure(figsize=(12,6))
plt.plot(item_counts, times_brute, 'o-', label='Brute Force')
plt.plot(item_counts, times_bottom, 's-', label='Bottom-Up DP')
plt.plot(item_counts, times_topdown, '^-', label='Top-Down DP')
plt.xlabel("Number of Items")
plt.ylabel("Execution Time (seconds)")
plt.title("Knapsack Algorithm Benchmark Comparison")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Summary
avg_brute = sum(times_brute) / len(times_brute)
avg_bottom = sum(times_bottom) / len(times_bottom)
avg_topdown = sum(times_topdown) / len(times_topdown)

print("\nAverage Execution Time Summary:")
print(f"  Brute Force  : {avg_brute:.6f} sec")
print(f"  Bottom-Up DP : {avg_bottom:.6f} sec")
print(f"  Top-Down DP  : {avg_topdown:.6f} sec")

fastest = min(avg_brute, avg_bottom, avg_topdown)
if fastest == avg_bottom:
    print("\n✅ Bottom-Up DP was overall the fastest approach.")
elif fastest == avg_topdown:
    print("\n✅ Top-Down DP was overall the fastest approach.")
else:
    print("\n✅ Brute Force (surprisingly) was fastest — likely for very small item counts.")
