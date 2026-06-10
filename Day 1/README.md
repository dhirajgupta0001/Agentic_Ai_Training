# Two Sum - Java Solutions (Brute Force & HashMap)

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

You may assume that each input has **exactly one solution**, and you may not use the same element twice.

### Example

**Input:**

```text
nums = [2, 7, 11, 15]
target = 9
```

**Output:**

```text
[0, 1]
```

**Explanation:**

```text
nums[0] + nums[1] = 2 + 7 = 9
```

---

# Solution 1: Brute Force Approach

## Approach

The brute force method checks every possible pair of elements in the array.

### Algorithm

1. Iterate through each element using a nested loop.
2. Compare the current element with every subsequent element.
3. If their sum equals the target, return their indices.
4. If no pair is found, return `[-1, -1]`.

### Java Code

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(int i = 0; i < nums.length; i++) {
            for(int j = i + 1; j < nums.length; j++) {
                if(nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{-1, -1};
    }
}
```

### Complexity Analysis

| Complexity       | Value |
| ---------------- | ----- |
| Time Complexity  | O(n²) |
| Space Complexity | O(1)  |

### Pros

* Easy to understand.
* No extra data structure required.

### Cons

* Inefficient for large input sizes.
* Performs unnecessary comparisons.

---

# Solution 2: Optimized HashMap Approach

## Approach

Use a HashMap to store previously visited numbers and their indices.

For each element:

1. Calculate the complement:

```text
complement = target - nums[i]
```

2. Check if the complement already exists in the HashMap.
3. If it exists, return the stored index and current index.
4. Otherwise, store the current number and its index in the HashMap.

### Java Code

```java
import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i < nums.length; i++) {

            int need = target - nums[i];

            if(map.containsKey(need)) {
                return new int[]{map.get(need), i};
            }

            map.put(nums[i], i);
        }

        return new int[]{-1, -1};
    }
}
```

### Complexity Analysis

| Complexity       | Value |
| ---------------- | ----- |
| Time Complexity  | O(n)  |
| Space Complexity | O(n)  |

### Pros

* Much faster than brute force.
* Only one traversal of the array is required.
* Preferred solution in coding interviews.

### Cons

* Requires additional memory for the HashMap.

---

# Comparison

| Approach    | Time Complexity | Space Complexity |
| ----------- | --------------- | ---------------- |
| Brute Force | O(n²)           | O(1)             |
| HashMap     | O(n)            | O(n)             |

### Why HashMap is Better?

For an array of size `n`:

* Brute Force compares many pairs and grows quadratically.
* HashMap performs lookups in constant time on average.
* The optimized solution scales much better for large datasets.

---

## LeetCode

Problem: **Two Sum (#1)**

Practice Link: https://leetcode.com/problems/two-sum/

---

## Author

Implemented in Java using:

* Brute Force Approach
* Optimized HashMap Approach

to understand the trade-offs between time complexity and space complexity while solving the Two Sum problem.
