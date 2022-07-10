class Solution:
        
    def maxArea(self, height: List[int]) -> int:
        
#         temp = height.copy()
#         max_area = 0
#         i,j = 0,0
        
#         while abs(i-j) < len(height)-1 :
#             x,i = self.maxWidth(temp)
#             print(f'max{x,i}')
#             for j,y in enumerate(height):
#                 print(y,j)
#                 if i != j:
#                     area = min(x,y) * abs(i-j)
#                     if area > max_area:
#                         max_area = area
#                     print(area)
#             temp[i] = 0
#             print(temp)
        left = 0
        right = len(height)-1
        max_area = 0
        while left<right:
            if height[left] > height[right]:
                area = height[right] * (right-left)
                right-=1
            else:
                area = height[left] * (right-left)
                left+=1
            if area > max_area:
                max_area = area
            
        return max_area
                
        
        
        # max_area = 0
        # for i,x in enumerate(height):
        #     for j in range(len(height)-1,i,-1):
        #         area = min(x,height[j]) * (j-i)
        #         if area > max_area:
        #             max_area = area
                      
        
            