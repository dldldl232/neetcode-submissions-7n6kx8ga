class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        output = 0
        pairs = sorted(zip(position, speed), reverse=True)
        currMaxTime = 0

        for pair in pairs:
            time = (target - pair[0]) / pair[1]
            if time <= currMaxTime:
                continue
            else:
                currMaxTime = time
            
            output += 1
        
        return output