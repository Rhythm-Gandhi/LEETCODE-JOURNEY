class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0] * 26

        # Count frequency of each letter
        for ch in word:
            freq[ord(ch) - ord('a')] += 1

        # Sort frequencies in descending order
        freq.sort(reverse=True)

        ans = 0

        # Assign costs greedily
        for i in range(26):
            if freq[i] == 0:
                break
            cost = i // 8 + 1
            ans += freq[i] * cost

        return ans