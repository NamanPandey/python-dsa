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
| 2 | [Valid Anagram](https://neetcode.io/problems/is-anagram) | Easy | 26-slot count array, early exit | O(n) | O(1) | ✅ Accepted 2026-11-01 | 2026-11-08 |
| 3 | [Two Sum](https://neetcode.io/problems/two-integer-sum) | Easy | Single-pass value→index map, check then insert | O(n) | O(n) | ✅ Accepted 2026-11-01 | 2026-11-08 |
| 4 | [Group Anagrams](https://neetcode.io/problems/anagram-groups) | Medium | `defaultdict(list)` keyed by 26-count signature | O(n·k) | O(n·k) | ✅ Accepted 2026-11-01 | 2026-11-08 |
| 5 | [Top K Frequent Elements](https://neetcode.io/problems/top-k-elements-in-list) | Medium | | | | ⏳ Next | |
| 6 | [Encode and Decode Strings](https://neetcode.io/problems/string-encode-and-decode) | Medium | | | | | |
| 7 | [Product of Array Except Self](https://neetcode.io/problems/products-of-array-discluding-self) | Medium | | | | | |
| 8 | [Valid Sudoku](https://neetcode.io/problems/valid-sudoku) | Medium | | | | | |
| 9 | [Longest Consecutive Sequence](https://neetcode.io/problems/longest-consecutive-sequence) | Medium | | | | | |

**Module progress:** 4 / 9

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

### 2. Valid Anagram · 2026-11-01 · Grade: A

**What went well**
- Length check first, then three approaches: two Counters (O(n)/O(1)), sort and compare (O(n log n)/O(n)), and a 26-slot array (O(n)/O(1), no hashing).
- Coded the strongest one, with a correct early exit: check `== 0` *before* decrementing, so a count never goes negative.
- Proved why the final verification loop can never fail: counts sum to `len(s) - len(t) = 0` and none is negative, so all are 0.
- Explained why a single up/down loop loses the early exit (counts can dip negative temporarily).

**To improve**
- Gave one approach when asked for two; the sort approach needed a hint.
- Started with O(n) space for the Counter before correcting to O(1) for a fixed alphabet. State the alphabet bound up front.
- Unicode follow-up: first answer blamed hash collisions. The real change is that the fixed array breaks (about 1.1M code points), so switch to a dict/Counter with O(k) space for the k distinct characters present.
- Remove the redundant final loop in the saved solution.

**Interview talking points**
- Fixed alphabet → array of counts; unbounded alphabet → hash map.
- Unicode normalisation: `"é"` can be one or two code points; use `unicodedata.normalize("NFC", s)` before comparing.

### 3. Two Sum · 2026-11-01 · Grade: A-

**What went well**
- Brute force (O(n²)/O(1)) and the single-pass value→index map stated before coding.
- Explained why sort + two pointers fits badly: it loses the original indices, and sorting `(value, index)` pairs adds O(n log n) and complexity for no gain.
- Applied earlier feedback unprompted: flat `if` with no `else` after `return`.
- Correct reasoning that returned indices are always ascending (map entries come from earlier indices).

**To improve**
- Initially described the miss case as "no pair" instead of "no pair *yet*, store `nums[i] → i`". That step is the algorithm.
- Didn't state complexity for the optimal approach until asked (O(n)/O(n)).
- Claimed the map never overwrites. It does (`[3, 1, 3, 5]`, target 8, overwrites index 0 with 2). It's safe because any index holding that value is a valid partner.
- Naming: `num_set` holds a dict. Use `seen` or `index_of`. Prefer `{}` over `dict()`.

**Interview talking points**
- Check-then-insert ordering is what prevents reusing the same element.
- `return []` is unreachable given the problem's guarantee; say so.

### 4. Group Anagrams · 2026-11-01 · Grade: A-

**What went well**
- Two key designs with correct complexity: sorted string O(n·k log k), 26-count signature O(n·k).
- Chose `defaultdict(list)`, and knew lists aren't hashable while tuples are.
- Asked why the sorted-key solution runs faster despite worse Big-O. That's exactly the right instinct.

**To improve**
- First key design, `"".join(str(x) ...)`, collides when counts reach 10 (`[1, 11]` vs `[11, 1]` both give `"111"`). Always stress-test composite keys.
- First fix used `ord(idx)`; the reverse mapping is `chr(ord('a') + idx)`. Know `ord`/`chr` directions cold.
- "Lists aren't hashable": give the mechanism too. They're mutable, so their hash could change after insertion.
- Prefer `tuple(counts)` over `"|".join(map(str, counts))`: hashable, collision-free, one C-level copy.
- Naming: `createHashKey` → `anagram_key`, `hash_list` → `counts`, `dictionary` → `groups` (PEP 8 and intent-revealing names).

**Why sorted keys win in CPython**
- `sorted()` and `join` run in C; a `for c in s` loop runs as interpreted bytecode.
- k is small (≤ 100), so k log k barely differs from k.
- The count key always pays a fixed 26-element conversion, even for 3-letter words.
- Runtime percentiles are noisy; resubmitting can shift them by 20–30 points.

---

## Module report card

| Skill | Status |
|---|---|
| Choosing set vs map vs Counter vs array | 🟢 Solid |
| Python cost of operations | 🟡 Reviewing |
| Stating trade-offs (time, space, side effects) | 🟡 Improving |
| Edge-case derivation | 🟡 Improving |
| Proving invariants / removing dead code | 🟢 Solid |
| Adapting to follow-up constraints | 🟡 Improving |
| Hashable key design (tuple vs list, collisions) | 🟡 Improving |
| Python naming (PEP 8) | 🟡 Improving |

**Teacher's note:** four accepted solutions in one session, including your first Medium, and you're already applying earlier feedback without being told. Next focus: name things by intent, stress-test any key you build, and state complexity for every approach without being asked.
