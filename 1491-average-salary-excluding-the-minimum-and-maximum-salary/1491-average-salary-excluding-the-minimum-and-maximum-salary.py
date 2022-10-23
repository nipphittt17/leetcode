class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        sum = 0
        for s in salary:
            sum = sum + s
        avg = (sum - salary[0] -salary[len(salary)-1])/(len(salary)-2)
        return avg
        