from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        To achieve minimum we must seperate identical tasks
        We only use n when identical tasks cannot be seperated
        """
        freq = {}
        for char in tasks:
            if char not in freq:
                freq[char] = 0
            freq[char] += 1
        
        maxFreq = max(freq.values())
        tied = 0
        print(freq)
        for key, val in freq.items():
            if val == maxFreq:
                tied += 1
        
        print(maxFreq)
        print(tied)
        
        skeleton = max(len(tasks), (maxFreq - 1) * (n + 1) + tied)

        return skeleton

        