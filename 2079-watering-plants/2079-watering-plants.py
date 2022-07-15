class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        step = 0
        water = capacity
        
        i = 0
        length = len(plants)
        while i < length: 
            if water >= plants[i]:
                if plants[i] != 0:
                    water -= plants[i]
                    plants[i] = 0
                step+=1 
                
            else:
                step += i
                water = capacity
                i = -1
            i+=1
            
        return step
            
        
        