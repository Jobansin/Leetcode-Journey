class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded+=(str(len(s))+'/'+s)
        return ''.join(encoded)
    def decode(self, s: str) -> List[str]:
        decoded=[]
        i=0
        while i < len(s):
            j=i
            while s[j] != '/':
                j+=1
            length= int(s[i:j])
            i= j+1
            j=i +length
            string=s[i:j]
            decoded.append(string)
            i=j
        return decoded
        
