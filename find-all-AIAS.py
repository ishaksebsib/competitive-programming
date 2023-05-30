class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        him, res, pL, sL = defaultdict(int), [], len(p), len(s)
        if pL > sL: return []

        for ch in p: him[ch] += 1

        for i in range(pL-1):
            if s[i] in him: him[s[i]] -= 1
            
        for i in range(-1, sL-pL+1):
            if i > -1 and s[i] in him:
                him[s[i]] += 1
            if i+pL < sL and s[i+pL] in him: 
                him[s[i+pL]] -= 1
                
            if all(v == 0 for v in him.values()): 
                res.append(i+1)
                
        return res
