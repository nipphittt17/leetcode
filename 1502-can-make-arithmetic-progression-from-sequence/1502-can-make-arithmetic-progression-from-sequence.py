class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sort_arr = arr.copy()
        sort_arr.sort()
        for i,x in enumerate(arr[:-2]):
            dif = (sort_arr[i+1]-sort_arr[i] == sort_arr[i+2]-sort_arr[i+1])
            if dif == False: return False
        return True