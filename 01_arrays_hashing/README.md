# 01 · Arrays & Hashing

## Pattern in one line
Trade O(n) space for O(1) average lookups: use a hash set for "have I seen this?", a hash map for "how many / where / which group?".

## Recognise it when
- You need membership checks, counts, or grouping.
- A brute force compares every pair (O(n²)).
- Order does not matter, or you can rebuild it afterwards.

## Python toolkit
| Tool | Use | Note |
|---|---|---|
| `set()` | Membership, dedupe | Unordered. Ordered dedupe: `list(dict.fromkeys(xs))` |
| `dict.get(k, default)` | Safe lookup | `d[k]` raises `KeyError` |
| `collections.Counter` | Frequency counts | Missing keys return 0 via `__missing__`; `==` compares counts |
| `collections.defaultdict(list)` | Grouping | No need to initialise keys |
| `"".join(sorted(s))` | Canonical key for anagrams | `sorted()` on a string returns a list |

## Problems

| # | Problem | Difficulty | Approach | Time | Space | Status | Re-solve by |
|---|---|---|---|---|---|---|---|
| 1 | [Contains Duplicate](https://neetcode.io/problems/duplicate-integer) | Easy | Hash set, early exit | O(n) | O(n) | ✅ Accepted 2026-11-01 | 2026-11-08 |
| 2 | [Valid Anagram](https://neetcode.io/problems/is-anagram) | Easy | | | | ⏳ Next | |
| 3 | [Two Sum](https://neetcode.io/problems/two-integer-sum) | Easy | | | | | |
| 4 | [Group Anagrams](https://neetcode.io/problems/anagram-groups) | Medium | | | | | |
| 5 | [Top K Frequent Elements](https://neetcode.io/problems/top-k-elements-in-list) | Medium | | | | | |
| 6 | [Encode and Decode Strings](https://neetcode.io/problems/string-encode-and-decode) | Medium | | | | | |
| 7 | [Product of Array Except Self](https://neetcode.io/problems/products-of-array-discluding-self) | Medium | | | | | |
| 8 | [Valid Sudoku](https://neetcode.io/problems/valid-sudoku) | Medium | | | | | |
| 9 | [Longest Consecutive Sequence](https://neetcode.io/problems/longest-consecutive-sequence) | Medium | | | | | |

**Module progress:** 1 / 9

---

## Feedback

### 1. Contains Duplicate · 2026-11-01 · Grade: A-

**What went well**
- Stated brute force (nested loops, O(n²) time, O(1) space) and the optimal hash-set approach (O(n)/O(n)) before coding.
- Identified the advantage of the loop over `len(set(nums)) != len(nums)`: **early exit** when the duplicate appears early.
- Accepted on first submission.

**To improve**
- Redundant `else` after `return`. Flatten it:
  ```python
  if num in num_set:
      return True
  num_set.add(num)
  ```
- Sorting alternative: gave O(n log n) time but missed **space** (Timsort can use up to O(n)) and the **side effect** (`nums.sort()` mutates the caller's list).
- Edge cases: listed only the empty array. Practise deriving them from assumptions. Negative numbers matter for solutions that index an array by value; all-equal input verifies the early exit.

**Interview talking points**
- Three approaches and their trade-offs: brute force, sort + adjacent compare, hash set.
- Hash set lookups are average O(1), worst O(n) under collisions.

---

## Module report card

| Skill | Status |
|---|---|
| Choosing set vs map vs Counter | 🟢 Solid |
| Python cost of operations | 🟡 Reviewing |
| Stating trade-offs (time, space, side effects) | 🟡 Improving |
| Edge-case derivation | 🟡 Improving |

**Teacher's note:** a confident start. For the remaining problems, say the trade-off of each approach out loud, including what it costs in memory and whether it mutates the input.
