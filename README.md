# python-dsa

Data structures and algorithms practice in Python, following the NeetCode 150 roadmap. Each pattern folder has its own README with per-problem feedback.

## Workflow
1. State brute force and its time/space complexity before coding.
2. Find a better approach and state its complexity.
3. List edge cases by asking "what am I assuming about the input?"
4. Solve on NeetCode/LeetCode until accepted.
5. Save the accepted solution here with a docstring: link, approach, time, space, alternatives considered.
6. Re-solve from memory after 1 week and mark it below.

## Structure
One folder per pattern, numbered in roadmap order:

| Folder | Pattern | Status |
|---|---|---|
| [01_arrays_hashing](01_arrays_hashing/) | Arrays & Hashing | In progress |
| 02_two_pointers | Two Pointers | Not started |
| 03_sliding_window | Sliding Window | Not started |
| 04_stack | Stack | Not started |
| 05_binary_search | Binary Search | Not started |
| 06_linked_list | Linked List | Not started |
| 07_trees | Trees | Not started |
| 08_heap | Heap / Priority Queue | Not started |
| 09_backtracking | Backtracking | Not started |
| 10_graphs | Graphs | Not started |
| 11_intervals | Intervals | Not started |
| 12_dynamic_programming | Dynamic Programming | Not started |
| 13_greedy | Greedy | Not started |

## Progress

| # | Problem | Pattern | Difficulty | Time | Space | Date | Re-solved |
|---|---|---|---|---|---|---|---|
| 1 | [Contains Duplicate](https://neetcode.io/problems/duplicate-integer) | Arrays & Hashing | Easy | O(n) | O(n) | 2026-11-01 | |
| 2 | [Valid Anagram](https://neetcode.io/problems/is-anagram) | Arrays & Hashing | Easy | O(n) | O(1) | 2026-11-01 | |

**Solved:** 2 · **Re-solved from memory:** 0 · **Target:** 110–120 solved, 60+ re-solved

---

## Report card

_Last updated: 2026-11-01 · Sessions: 1_

| Area | Grade | Evidence |
|---|---|---|
| Big-O theory | B+ | Correct on nested loops, Counter space, binary search halving. Described binary search as "leaves moving up" instead of root down. |
| Python cost model | C | Quiz 3/6. Missed: slices copy, `pop(0)` vs `deque.popleft()`, Timsort, `str +=` in a loop is O(n²). |
| Python built-ins for DSA | A- | Accurate predictions for `set`, `dict.get`, `Counter`, `defaultdict`, `sorted`. Missed `__missing__` and believed `OrderedSet` exists. |
| Problem-solving process | A | Brute force → optimal → edge case stated before coding. Reached three approaches for Valid Anagram, including the O(1)-space array. |
| Code quality | A- | Correct and readable. Redundant `else` after `return` (Contains Duplicate); one provably redundant final loop (Valid Anagram). |
| Explaining the "why" | B | Improving within the session: proved why the final loop is redundant and why a single loop loses the early exit. Still first reaches for the wrong mechanism (hash collisions for Unicode). |
| Constraint changes (follow-ups) | B- | Spotted that the 26-slot array breaks for Unicode, but didn't move to "switch to a dict, space O(k distinct)" on first try. |

**Overall: B+ (trending A-).** Strong fundamentals and a disciplined process. Gaps: Python cost model and reasoning through follow-up constraint changes.

## Teacher's recommendations

1. **Always name the mechanism.** "Sets are O(1) because hashing maps the value straight to a bucket; average O(1), worst O(n)" scores; "sets are optimized" does not. Practise saying the *why* out loud.
2. **Learn the Python cost model, not just Big-O.** Keep [Python TimeComplexity](https://wiki.python.org/moin/TimeComplexity) open for two weeks. Before submitting, scan for hidden O(n): slices, `in list`, `pop(0)`, `insert(0, x)`, string `+=`.
3. **Call out side effects.** Mention when an approach mutates the input (e.g. `nums.sort()`). It signals production thinking.
4. **Derive edge cases from assumptions.** Ask "what does my solution assume about values, size, order, type?" rather than listing generic cases.
5. **Flatten control flow.** Drop `else` after `return`/`continue`; early returns read better (Ruff `RET505`).
6. **Prove, then delete.** Before writing a final verification loop, ask whether earlier invariants already guarantee the result. Removing provably dead code is a strong interview signal.
7. **For every follow-up, ask "which assumption just broke?"** Then pick the structure that no longer depends on it (fixed array → dict when the alphabet is unbounded).

**Strengths to keep:** you resist jumping to code, you think about early exit, and you ask clarifying questions when a prompt is ambiguous. That is exactly how interviewers want you to work.

## Feedback log

| Date | Session | Highlights |
|---|---|---|
| 2026-11-01 | Big-O quiz, built-ins, Contains Duplicate, Valid Anagram | Big-O 3/6 (Python costs), built-ins mostly correct. Contains Duplicate (A-) and Valid Anagram (A) accepted with optimal approaches. Next: Two Sum, and re-solve both on 2026-11-08. |
