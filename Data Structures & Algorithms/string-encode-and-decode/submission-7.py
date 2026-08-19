class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            word_len = len(word)
            result+=str(word_len)
            result+="#"
            result+=word
        
        return result

    def decode(self, s: str) -> List[str]:
        print(s)
        result = []

        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j+=1
            
            word_len = s[i:j]
            int(word_len)

            word = s[j:j+word_len]
            result.append(word)

            i = j+word_len
        
        return result



