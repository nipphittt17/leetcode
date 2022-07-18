class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = 1
        while arr[right]>arr[left]:
            left = right
            right+=1
        return left
        