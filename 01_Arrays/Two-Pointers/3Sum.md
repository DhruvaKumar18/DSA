# 15. 3Sum

## Problem Statement

Given an integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` such that:

- `i != j`, `i != k`, and `j != k`.
- `nums[i] + nums[j] + nums[k] == 0`.
- The solution must not contain duplicate triplets.

## Python Solution (Two Pointers)

```python
class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()  # Sort the array

        for i, pos in enumerate(nums):

            if i > 0 and pos == nums[i - 1]:  # Skip duplicates
                continue

            left, right = i + 1, len(nums) - 1  # Two pointers

            while left < right:
                three_sum = pos + nums[left] + nums[right]

                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.append([pos, nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1  # Skip duplicates

        return res
```

## Example

**Input:**
```python
nums = [-1, 0, 1, 2, -1, -4]
```

**Output:**
```python
[[-1, -1, 2], [-1, 0, 1]]
```

## Complexity Analysis

- **Time Complexity:** `O(n²)` – Sorting takes `O(n log n)` and the two-pointer traversal takes `O(n²)`.
- **Space Complexity:** `O(1)` auxiliary space, excluding sorting space and output storage.
