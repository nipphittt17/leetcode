class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        arr.sort(reverse=True)
        print(arr)
        for a in range(len(arr)):
            
            
            if arr[a] >= 0:
                left = a
                right = len(arr)-1
            else:
                right = a
                left = 0
                
            print(f'a {arr[a]}')
            while left <= right:
                mid = left + (right-left)//2
                # print(mid)
                print(arr[mid])
                if mid != a and arr[mid]*2 == arr[a]: return True
                elif arr[mid]*2 < arr[a]: right = mid-1
                else: left = mid+1

           
        return False
        