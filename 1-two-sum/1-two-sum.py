class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        out = []

        for i,num in enumerate(nums):
            if num not in numbers:
                numbers[num] = [i]
                
                for number in numbers:
                    if num+number == target and num != number:
                        out.append(numbers[number][0])
                        out.append(i)
                        break
                        
            else:
                numbers[num].append(i)
                for index in numbers[num]:
                    if num+num == target:
                        out.append(index)    
                        out.append(i)
                        break
                
        return out        
                
                
        
            
        
        