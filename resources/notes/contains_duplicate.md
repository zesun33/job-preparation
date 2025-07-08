# Contains Duplicate – Study Note

**Problem link:** [NeetCode 150 – Contains Duplicate](https://neetcode.io/problems/duplicate-integer?list=neetcode150)  
**LeetCode link:** https://leetcode.com/problems/contains-duplicate/

---
## 1. Problem Statement
Given an integer array `nums`, return **True** if any value appears *at least twice*, otherwise **False**.

---
## 2. Solution Space
| Approach | Idea | Time | Space | Pros | Cons |
|----------|------|------|-------|------|------|
| Brute‐force nested loops | Compare every pair | `O(n²)` | `O(1)` | Simple | Very slow for `n > ~1e3` |
| **Sort & Scan** | Sort, then check adjacent elements | `O(n log n)` | `O(1)` (in-place sort) | No extra memory | Slower than hash-set; mutates order |
| **Hash-Set scan** (accepted) | Insert into `set`, detect duplicate on lookup | `O(n)` avg. | `O(n)` | Fastest time | Uses extra memory |
| Bitmap / Bitset | One bit per possible value | `O(n)` | Range/8 bytes | Tiny memory when range ≪ n | Needs small, known numeric range |

---
## 3. Detailed Walk-through of the Hash-Set Solution
```python
seen = set()
for x in nums:
    if x in seen:
        return True
    seen.add(x)
return False
```
* **Data-structure:** *Hash table* under the hood – average `O(1)` insert & lookup.
* **Why it works:** First time you meet a value you mark it; second time the membership test succeeds ⇒ duplicate.

---
## 4. Edge-Cases & Their Implications
1. **Empty array `[]`** – return `False`; loop never executes.  
2. **Single element `[5]`** – no duplicate, `False`.  
3. **All identical `[7,7,7]`** – early exit on second element, `True`.  
4. **Large unique list** – tests linear behavior and memory usage.  
5. **Mixed signs / 0** – hashing handles negatives; beware if using bitmap w/o offset.  
6. **Min/Max ints** – watch overflow in fixed-width languages.  
7. **Already sorted** – can skip sort step if detecting sortedness (`O(n)` check).  
8. **Duplicate far apart** – worst-case memory for hash-set; sort uses less space.  
9. **Non-hashable items (Python)** – lists/sets can’t be in a set; convert to tuple or choose other structure.  
10. **Tiny value range, huge `n`** – bitmap beats hash-set in memory.

---
## 5. Bitmap vs. Hash-Set Quick Comparison
| Metric | Bitmap | Hash-Set |
|--------|--------|----------|
| Memory proportional to | **Value range** | **#Distinct values** |
| Lookup time | `O(1)` bit operations | `O(1)` expected |
| Works with negatives? | need offset | yes |
| Iterating stored values | scan whole range | direct iteration |
| Best when | range small & dense | range large / unknown |

---
## 6. Detecting Pre-sorted Input (bonus)
Early optimization for sort approach:
```python
is_sorted = all(nums[i] <= nums[i+1] for i in range(len(nums)-1))
if is_sorted:
    # only need the single scan, skip nums.sort()
```

---
## 7. Take-aways & Interview Talking Points
* **Membership check** pattern ⇒ hash-set first choice.
* Always discuss **time vs. space** trade-offs (hash vs. sort vs. bitmap).
* Mention language constraints (*hashable types*, integer overflow).
* Show awareness of edge cases and input characteristics.

---
*Prepared: 2025-07-08*