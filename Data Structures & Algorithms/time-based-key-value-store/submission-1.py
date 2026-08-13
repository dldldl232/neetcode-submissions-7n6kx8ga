class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        
        l, r = 0, len(self.data[key]) - 1
        result = ""

        while l <= r:
            mid = l + ((r-l) // 2)
            val, ts = self.data[key][mid]

            if ts == timestamp:
                return val

            # move search range to right
            elif ts < timestamp:
                result = val
                l = mid + 1
            
            else:
                r = mid - 1
        
        return result
                
