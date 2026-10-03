class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += '#'
            res += s
        
        return res

    def decode(self, s: str) -> List[str]:
        decoded = []
        if s == "":
            return []
        
        i = 0
        while i < len(s):
            delimiter = s.find('#', i)
            length = int(s[i:delimiter])
            decoded.append(s[delimiter+1:delimiter+1+length])
            i = delimiter+1+length
      
        return decoded
            
