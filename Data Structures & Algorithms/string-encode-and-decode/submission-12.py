class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            res+=len(word) + "#" + word
        
        return result

    def decode(self, s: str) -> List[str]:
        print(s)
        result = []

        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j+=1
            
            word_len = int(s[i:j])
            i = j + 1

            word = s[i:i+word_len]
            result.append(word)

            i+=word_len
        
        return result



