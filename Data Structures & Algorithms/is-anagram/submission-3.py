class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)==len(t)):
            s_counts = collections.Counter(s)
            t_counts = collections.Counter(t)
            return s_counts == t_counts
        return False