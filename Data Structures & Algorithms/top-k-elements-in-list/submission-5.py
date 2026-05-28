class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = []
        x = [nums[0]]
        r = 0
        v = {}
        m=[]
        for num in nums:
            v[num]=nums.count(num)
        print(v)
        v=dict(sorted(v.items(), key=lambda x: x[1], reverse = True))    
        print(v)
        for i, (key, value) in enumerate(v.items()):
            print(i, key, value)
            arr.append(key)
            if(k==i+1):
                break
        return arr