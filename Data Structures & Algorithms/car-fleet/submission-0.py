class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # car cannot pass another car ahead of it ->only possible to catch up to another car
        # and drive at the same speed as the car ahead of it

        # car fleet = nonempty sets of cars driving at the same position and same speed
        # single car is also considered a fleet

        # car catches up to a car fleet the moment the fleet reaches the destination, then the
        # car is considered to be part of the fleet

        # RETURN number of diff car fleets that will arrive at the destination

        # car merges if car behind is fast enough to catch up before crossing the finish line
        output = 0
        time = []
        n = len(position)

        for i in range(n):
            total_time = (target-position[i]) / speed[i]
            time.append(total_time)

        for j in range(n):
            for z in range(j+1, n):
                if time[j] == time[z]:
                    if position[j] < position[z]:
                        if speed[j] > speed[z]:
                            output += 1
                    else:
                        if speed[z] > speed[j]:
                            output += 1
        
        remains = n - (output * 2)

        return output + remains

        

