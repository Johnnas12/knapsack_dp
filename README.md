# 📦 0/1 Knapsack Algorithm Benchmarking

This project implements and benchmarks **three classic approaches** for solving the **0/1 Knapsack Problem**:

- 🐌 Brute-Force Recursive Search  
- ⚡ Bottom-Up Dynamic Programming (Tabulation)  
- ⚡ Top-Down Dynamic Programming (Memoization)

We analyze their performance under various input conditions by comparing execution times and result consistency using **matplotlib** visualizations.

---


---

## 📊 Implementations Overview

### ✅ Brute-Force Recursive (Exhaustive Search)
- Recursively considers both including and excluding each item.
- Explores all possible combinations.
- Exponential time complexity: **O(2ⁿ)**

**File:** `brute_force.py`

---

### ✅ Bottom-Up Dynamic Programming (Tabulation)
- Iteratively builds a DP table of optimal values for smaller subproblems.
- Fills up a 2D table based on item count and capacity.
- Time complexity: **O(nW)**  
- Space complexity: **O(nW)**

**File:** `knapsack_dp.py`

---

### ✅ Top-Down Dynamic Programming (Memoization)
- Recursively computes optimal values while storing subproblem results in a cache (memoization).
- Reduces redundant calculations.
- Time complexity: **O(nW)**  
- Space complexity: **O(nW)**

**File:** `knapsack_top_down.py`

---

## 📊 Benchmarking & Results

**Benchmark script:** `benchmark.py`  
- Measures and logs execution time for each approach.
- Plots execution time vs number of items using `matplotlib`.
- Displays value consistency and performance trends.

---

## 📈 Observations / Analytics

| Scenario | Optimal Algorithm |
|:------------|:--------------------|
| Small number of items (≤8) and small capacity | 🐌 **Brute-Force** surprisingly efficient due to low recursion depth |
| Medium capacity (W=500) and moderate items (~20) | ⚡ **Top-Down DP** performed best due to reduced redundant recursion |
| Larger problem sizes (30+ items) | ⚡ **Bottom-Up DP** consistently outperformed others in execution time |

**Takeaway:**  
- **Brute-force is fine for tiny inputs.**
- **Top-Down DP shines in moderate-size problems with higher capacities.**
- **Bottom-Up DP scales better for large instances.**

---

## 📦 Setup Instructions

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run Benchmark
```
python benchmark.py
```
