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

---

# Add Two Numbers (Linked List)

## Problem Statement

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each node contains a single digit.

Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zeros, except the number 0 itself.

### Example

**Input:**

```text
l1 = [2,4,3]
l2 = [5,6,4]
```

**Output:**

```text
[7,0,8]
```

**Explanation:**

```text
342 + 465 = 807
```

---

## Approach

Use a dummy node to build the resulting linked list while traversing both input lists simultaneously.

At each step:

1. Read values from both lists.
2. Add them along with the carry from the previous step.
3. Create a new node with `sum % 10`.
4. Update carry using `sum / 10`.
5. Move to the next nodes.
6. Continue until both lists and carry are exhausted.

---

## Java Solution

```java
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        ListNode dummy = new ListNode(0);
        ListNode current = dummy;

        int carry = 0;

        while (l1 != null || l2 != null || carry != 0) {

            int v1 = (l1 != null) ? l1.val : 0;
            int v2 = (l2 != null) ? l2.val : 0;

            int sum = v1 + v2 + carry;

            carry = sum / 10;

            current.next = new ListNode(sum % 10);
            current = current.next;

            if (l1 != null) {
                l1 = l1.next;
            }

            if (l2 != null) {
                l2 = l2.next;
            }
        }

        return dummy.next;
    }
}
```

---

## Complexity Analysis

| Complexity       | Value        |
| ---------------- | ------------ |
| Time Complexity  | O(max(m, n)) |
| Space Complexity | O(max(m, n)) |

Where:

* `m` = length of first linked list
* `n` = length of second linked list

---

## Key Takeaways

* Demonstrates linked list traversal.
* Uses a dummy node to simplify list construction.
* Efficiently handles carry propagation.
* One-pass solution with linear time complexity.

---

## LeetCode

Problem: **Add Two Numbers (#2)**

Practice Link: https://leetcode.com/problems/add-two-numbers/

