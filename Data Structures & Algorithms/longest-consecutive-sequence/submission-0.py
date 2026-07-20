class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)
        maxc = 0
        for i in setnums:
            curr = i
            count = 0
            if(i-1 not in setnums):
                while(curr in setnums):
                 count = count + 1
                 curr = curr + 1
                if(maxc<count):
                    maxc = count
        return maxc
        