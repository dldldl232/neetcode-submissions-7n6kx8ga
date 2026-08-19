class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root;

        for a in word:
            if a not in curr.children:
                curr.children[a] = TrieNode()
            curr = curr.children[a] #move pointer to child node
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for a in word:
            if a not in curr.children:
                return False
            curr = curr.children[a]

        return curr.endOfWord
            

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for a in prefix:
            if a not in curr.children:
                return False
            curr = curr.children[a]
        return True
        