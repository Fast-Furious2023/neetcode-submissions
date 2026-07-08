class PrefixTree:

    def __init__(self):
        self.root = {}

        

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["#"] = True #mark the end of a word


    def search(self, word: str) -> bool:
        node = self._find_word(word)
        return node is not None and "#" in node
        

    def startsWith(self, prefix: str) -> bool:
        node = self._find_word(prefix)
        return node is not None

    def _find_word(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return None
            node = node[char]
        return node
        
        