class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        length = len(letters)
        left = 0
        right = length-1
        mid = 0
        
        while left <= right:
            mid = (left+right)//2          
            if letters[mid] == target:
                if mid!=length-1 and letters[mid+1] > target:
                    return letters[mid+1]
                else: left = mid+1
            elif letters[mid] > target:
                if mid!=0 and letters[mid-1] > target:
                    right = mid-1
                else:
                    return letters[mid]             
            else: left = mid+1
                
        return letters[0]