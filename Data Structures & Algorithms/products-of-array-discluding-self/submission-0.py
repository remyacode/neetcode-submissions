class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftproduct = [1]*len(nums)
        rightproduct = [1]*len(nums)
        resultant = [1]*len(nums)

        for i in range(1,len(nums)):
            leftproduct[i] = nums[i-1] * leftproduct[i-1]

        j = len(nums)-2
        while(j>=0):
            rightproduct[j] = rightproduct[j+1]*nums[j+1]
            j = j - 1
        for k in range(len(nums)):
            resultant[k]=rightproduct[k]*leftproduct[k]
        return resultant
