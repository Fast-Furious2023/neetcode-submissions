class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #create a trie to store all the words
        root = TrieNode()

        for w in words:
            curr = root
            for char in w:
                if char not in curr.children:
                    curr.children[char]=TrieNode()
                curr = curr.children[char]
            curr.word = w

        #dfs to explore the board
        R, C = len(board), len(board[0])
        res = set()

        def dfs(r,c,node):
            char = board[r][c]
            if char not in node.children:
                return
            
            next_node = node.children[char]
            if next_node.word:
                res.add(next_node.word)

            board[r][c]="#" #mark as used

            #explore next cell in four directions
            for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < R and 0<= nc < C and board[nr][nc] != "#":
                    dfs(nr, nc, next_node)
            
            board[r][c]= char


        #pass every cell into the dfs
        for r in range(R):
            for c in range(C):
                dfs(r,c,root)
        return list(res)