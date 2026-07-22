from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        need = Counter(t)
        required = len(need)
        window_count = {}
        formed = 0
        l = 0
        best_len, best_l, best_r = float('inf'), 0, 0

        for r in range(len(s)):
            c = s[r]
            window_count[c] = window_count.get(c, 0) + 1
            if c in need and window_count[c] == need[c]:
                formed += 1

            while formed == required:
                if r - l + 1 < best_len:
                    best_len, best_l, best_r = r - l + 1, l, r

                left_c = s[l]
                window_count[left_c] -= 1
                if left_c in need and window_count[left_c] < need[left_c]:
                    formed -= 1

                l += 1

        return "" if best_len == float('inf') else s[best_l:best_r + 1]