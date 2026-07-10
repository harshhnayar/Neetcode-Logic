class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) < len(t) or len(t) < len(s):
            return False


        Ssort = "".join(sorted(s))
        Tsort = "".join(sorted(t))

        if  Ssort == Tsort :
            return True
        else:
            return False    