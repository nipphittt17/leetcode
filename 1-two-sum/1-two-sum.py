class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}

        for i,num in enumerate(nums):
            if num not in numbers:
                numbers[num] = [i]
                
                for number in numbers:
                    if num+number == target and num != number:
                        return [numbers[number][0],i]
                        break
                        
            else:
                numbers[num].append(i)
                for index in numbers[num]:
                    if num+num == target:
                        return [index,i]
                        break
                
                
                
        
            
        
        