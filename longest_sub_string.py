class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len

"""
Sliding Window Technique

We use a set to keep track of the characters we have seen so far.
We use two pointers, left and right, to define the current window (substring without duplicates).
- `right` moves forward one step at a time, expanding the window.
- When `s[right]` is already in the set, we shrink the window by moving `left` forward and removing `s[left]` from the set until the duplicate is gone.
- At each step, we update `max_len` with the current window size (`right - left + 1`).

TL;DR:
`right` always moves forward.  
`left` only moves forward when a duplicate is found, and keeps going until the window is clean (no duplicates).
"""
