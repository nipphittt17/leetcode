class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        step = 0
        water = capacity
        
        i = 0
        length = len(plants)
        
        while i < length: 
            if water >= plants[i]:
                water -= plants[i]
                step+=1 
                i+=1
                
            else:
                step += i*2
                water = capacity

        return step
            
        
        