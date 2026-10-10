class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        for every step, its the number of steps before -1 and -2
        '''
        if n <= 2:
            return n

        steps = [0] * (n + 1) 

        steps[1] = 1
        steps[2] = 2

        for i in range(3,len(steps)):
            steps[i] = steps[i-1] + steps[i - 2]
        
        return steps[-1]
        