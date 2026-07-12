class Solution:
    def isPalindrome(self, s: str) -> bool:
        # case insensitive
        # ignores non-alphanumeric characters

        # we will use two pointers
        # that start from the left and right

        # if left == right: (includes space)
        # move one
        # else:
        # return False

        left, right = 0, len(s)-1

        while left < len(s) and right > -1: # maybe we could shortcut this more
            print(f"{s[left]}: {s[left].isalnum()}")
            print(f"{s[right]}: {s[right].isalnum()}")

            if s[left].isalnum() and s[right].isalnum():
                if s[left].upper() != s[right].upper():
                    return False
                elif left == right:
                    return True
                elif s[left].upper() == s[right].upper():
                    left += 1
                    right -= 1
            else:
                if not s[right].isalnum():
                    right -= 1
                elif not s[left].isalnum():
                    left += 1
            
        return True
                
