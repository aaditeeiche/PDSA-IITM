Ram has an list of integers $a_1, a_2,.......a_n$ of size $n$. Each integer at index $i$ denotes the money placed at that index $i$. He can do the following **operation exactly once**:

Pick a subsegment of the list and cyclically rotate it in the clockwise direction by any amount. i.e. pick integer $l$ and $r$ such that $1 ≤ l ≤ r ≤ n$, and rotate the list $a_l, a_{l + 1}, …… a_r$ in the clockwise direction by any amount. Ram wants the maximum amount of money by performing this particular operation exactly once. After performing the operation , Ram will collect $a_n - a_1$ amount of money.

Determine the maximum value of $a_n - a_1$ that he can obtain. 

Write a function **Max_Amount(a)** that accept a list **a** and returns the maximum value of $a_n - a_1$ that Ram can obtain.

**Sample Input**

```
[1, 9, 8, 4, 6]
```

**Output**

```
8
```

**Sample Input**

```
[3, 2, 10, 8] 
```

**Output:**

```
7
```

