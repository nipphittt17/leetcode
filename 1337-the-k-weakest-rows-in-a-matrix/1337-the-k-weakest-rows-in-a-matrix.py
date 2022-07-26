class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        soldier = {}
       
        for i,m in enumerate(mat):
            soldier[i] = m.count(1)
        
        weakestList = list(sorted(soldier, key=soldier.get))
        return weakestList[:k]

        
        