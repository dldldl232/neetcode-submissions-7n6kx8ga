class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []

        for i in range(len(temperatures)):
            currTemp = temperatures[i]
            day = 0
            print(f"currTemp: {currTemp}")

            for j in range(i, len(temperatures)):
                print(f"j: {temperatures[j]}")
                if temperatures[j] > currTemp:
                    result.append(day)
                    print(f"result: {result}")
                    break
                # higher temp does not exist
                elif j == len(temperatures) - 1:
                    result.append(0)
                else:
                    day += 1
        
        return result

        """
        Use nested loops
        include currTemp too
        Pop once we find bigger temperature -> to catch cases where we cannot initiate pop, we check
        if stk is empty if not we put 0 in result.
        """

