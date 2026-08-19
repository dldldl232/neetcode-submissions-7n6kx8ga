class Trie:

    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        curr = self.root
        for a in word:
            if a not in curr.children:
                curr.children[a] = Trie()
            curr.children[a]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        # since . can be matched with any letter
        # we have to use dfs for situations such as .all and we have call rall 
        def dfs(index: int, node: Trie):
            curr = node
            for i in range(index, len(word)):
                char = word[i]

                if char == ".":
                    for child in curr.children.values():
                        if (dfs+1, child):
                            return True
                
                    return False
                
                # when char is just an alphabet
                else:
                    if char not in curr.children:
                        return False
                    
                    curr = curr.children[char] #move point to the child 
            
            return curr.is_end
        
        return dfs(0, self.root)
        

        
  




