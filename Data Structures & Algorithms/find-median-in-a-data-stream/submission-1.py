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
        print(self.data)
        if length == 1:
            return float(self.data[0])
        else:
            return sum / length
         
        
        