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
if __name__ == "__main__":
    W = 50  # Maximum weight capacity of the knapsack
    wt = [10, 20, 30]  # Weights of the items
    vt = [60, 100, 120]  # Values of the items  

    max_value = knapsackBruteForce(W, wt, vt)
    print(f"The maximum value that can be obtained is: {max_value}")