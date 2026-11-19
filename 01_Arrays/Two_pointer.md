# 167. Two Sum II – Input Array Is Sorted

## Problem Statement

You are given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order.

Find two numbers such that they add up to a specific target number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers `index1` and `index2` as an integer array `[index1, index2]` of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

## Examples

**Example 1:**

Input:
```python
numbers = [2,7,11,15]
target = 9
```

Output:
```python
[1,2]
```

Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2.

**Example 2:**

Input:
```python
numbers = [2,3,4]
target = 6
```

Output:
```python
[1,3]
```

Explanation: The sum of 2 and 4 is 6.

**Example 3:**

Input:
```python
numbers = [-1,0]
target = -1
```

Output:
```python
[1,2]
```

## Approach: Two Pointers

Since the array is already sorted, we can use the Two Pointer technique.

1. Initialize `l = 0` (left pointer).
2. Initialize `r = len(numbers) - 1` (right pointer).
3. Calculate the sum of `numbers[l] + numbers[r]`.
4. If the sum equals the target, return the indices (1-based).
5. If the sum is smaller than the target, increment the left pointer.
6. If the sum is greater than the target, decrement the right pointer.
7. Continue until the two pointers meet.

## Python Solution

```python
class Solution(object):
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return l + 1, r + 1

            elif numbers[l] + numbers[r] < target:
                l += 1

            elif numbers[l] + numbers[r] > target:
                r -= 1

        return l + 1, r + 1
```

## Complexity Analysis

**Time Complexity: O(n)**

Each pointer moves towards the other pointer. Every element is visited at most once.

**Space Complexity: O(1)**

Only two pointers (`l` and `r`) are used. No additional data structures are required.

## Key Takeaway

The Two Pointer technique is useful when working with sorted arrays. Instead of using nested loops, we can solve the problem in O(n) time and O(1) extra space.

## LeetCode

Problem: 167. Two Sum II – Input Array Is Sorted

---
