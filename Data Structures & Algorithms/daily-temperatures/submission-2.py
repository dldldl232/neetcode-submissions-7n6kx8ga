"""
Optimized version: where we use the monotomic stack
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stk = []

        for j in range(len(temperatures)):
            while len(stk) != 0 and temperatures[j] > temperatures[stk[-1]]:
                i = stk.pop()
                result[i] = j-i
            stk.append(j)
        
        return result

        