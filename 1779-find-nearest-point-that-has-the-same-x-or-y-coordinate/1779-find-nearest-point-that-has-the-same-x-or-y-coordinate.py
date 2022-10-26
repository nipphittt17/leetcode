class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        min_man = inf
        min_idx = -1
        idx = -1
        
        for loc in points:
            idx+=1
            if loc[0] != x and loc[1] != y:
                continue
            
            curr_man = abs(x - loc[0]) + abs(y - loc[1])
            if curr_man < min_man:
                min_man = curr_man
                min_idx = idx
            elif curr_man == min_man and idx < min_idx:
                min_idx = idx
        
        return min_idx

        