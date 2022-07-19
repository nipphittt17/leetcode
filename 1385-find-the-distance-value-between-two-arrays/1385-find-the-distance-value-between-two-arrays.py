class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
  
        arr2.sort()
        
        for i in range(len(arr1)):
            dis = True
            
            left = 0
            right = len(arr2)-1
            while left <= right:
        
                mid = (left+right)//2
                if abs(arr1[i]-arr2[mid]) <= d:              
                    dis = False
                    break
                elif arr2[mid] > arr1[i]:
                    right = mid-1
                elif arr2[mid] < arr1[i]:
                    left = mid+1
              
            if dis == True:
                count+=1
        return count
                
                
                