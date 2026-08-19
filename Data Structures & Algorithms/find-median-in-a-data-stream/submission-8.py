import math
#python always floors the result in division
class MedianFinder:

    def __init__(self):
        self.data = []
        

    def addNum(self, num: int) -> None:
        self.data.append(num)
        

    def findMedian(self) -> float:
        self.data.sort() #as sorted() creates a copy that costs memory
        sum = 0
        for num in self.data:
            sum += num

        length = len(self.data)
        print(f"length: {length}")
        if length == 1:
            return float(self.data[0])
        elif length % 2 == 1:
            print(sum)
            return sum / length
        else:
            mid1 = length / 2
            mid2 = mid1 - 1
            print(f"mid1: {mid1}")
            print(f"mid2: {mid2}")
            result = (self.data[int(mid1)] + self.data[int(mid2)]) / 2
            print(f"result: {result}")
            return result
         
        
        