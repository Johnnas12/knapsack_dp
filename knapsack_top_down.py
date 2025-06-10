import time 

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

    for i in range(1, len(weights)+1):
        wt = weights[:i]
        vt = values[:i]

        start_time = time.perf_counter()
        max_value = knapsackTopDownWrapper(W, wt, vt)
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(f"{i} items: Value = {max_value}, Time = {elapsed_time:.8f} sec")
