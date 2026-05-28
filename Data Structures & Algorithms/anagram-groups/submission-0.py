class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        stry = strs
        seen = []
        for i in range(len(strs)):
            x = "".join(sorted(strs[i]))
            arr = []
            if i not in seen:
                arr.append(strs[i])
                seen.append(i)
            for j in range(len(strs)):
                y = "".join(sorted(strs[j]))
                if(x==y and i!=j and j not in seen):
                    seen.append(j)
                    arr.append(strs[j])
            if len(arr) > 0:
                result.append(arr)
        return result

        