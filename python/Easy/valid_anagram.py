# Using string operators
class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!= len(t):
            return False
        
        s = sorted(s)
        t = sorted(t)

        if s == t:
            return True
        else:
            return False
        
# Using hashmap(dict)
class Solution(object):
    def isAnagram(self, s, t):
        char_count = {}

        if len(s) != len(t):
            return False
        
        for c in s:
            char_count[c] = char_count.get(c,0) + 1
        
        for c in t:
            if c not in char_count:
                return False
            
            char_count[c] -= 1
            
            if char_count[c] < 0:
                return False

        return True
        

        