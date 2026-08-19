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
            if s[i].isdigit():
                word_len = int(s[i])

            print(f"Word length: {word_len}")
            
            i += 2 #skip "#" and start at char

            word = s[i:i+word_len]
            print(word)

            result.append(word)
        
            i += word_len

        return result



