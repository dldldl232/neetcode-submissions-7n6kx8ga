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
                else:
                    day += 1
        
        if len(temperatures) > len(result):
            diff = len(temperatures) - len(result)
            while diff > 0:
                result.append(0)
                diff -= 1
        
        return result

