class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        step = 0
        water = capacity
        
        i = 0
        length = len(plants)
        passed = [False for i in range(length)] 
        
        while i < length: 
            if water >= plants[i]:
                if passed[i] == False:
                    water -= plants[i]
                    passed[i] = True
                step+=1 
                
            else:
                step += i
                water = capacity
                i = -1
            i+=1
            
        return step
            
        
        