class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
  
        waterA = capacityA
        waterB = capacityB
        
        refill = 0
    
        length = len(plants)
        a = 0
        b = length-1 
        
        while a < b:
            each = 0
            if waterA >= plants[a]:
                waterA -= plants[a]
                plants[a] = 0
                
            elif waterA < plants[a]:
                each += 1
                waterA = capacityA
                
            if waterB >= plants[b]:
                waterB -= plants[b]
                plants[b] = 0
                
            elif waterB < plants[b]:
                each += 1
                waterB = capacityB
            
            if each == 0:
                a+=1
                b-=1
            refill+=each
        
        if a == b:
            if waterA == waterB and waterA < plants[a]:
                refill+=1
            elif max(waterA,waterB) < plants[a]:
                refill+=1
                
        return refill
            
            