"Brute Force"

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prereq pairs are unique
        # from constraints as input is not that big will not
        # consider a lot about performance

        # check if prereq can't be filled
        past_records = []

        for i in range(len(prerequisites)):
            # check circular dependencies
            switched = [prerequisites[i][1], prerequisites[i][0]]
            
            if switched in past_records:
                return False

            # case: [5, 5]
            if switched == prerequisites[i]:
                return False

            past_records.append(prerequisites[i])
        
        if len(past_records) > numCourses:
            return False
        
        return True


        