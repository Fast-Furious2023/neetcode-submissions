from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #BFS search
        #treat every word as a node, and two nodes are connected if
        #they differ by exactly one character
        #comparing: generate one-letter mutation of the current word, check if it is a valid word

        words_set = set(wordList) #O(1)lookup and keep track of unvisited words

        queue = deque([(beginWord,1)])

        while queue:
            current, step = queue.popleft()

            if current == endWord:
                return step

            for i in range(len(current)):
                c = current[i]

                for char in "abcdefghijklmnopqrstuvwxyz":
                    if char == c:
                        continue
                    
                    next_word = current[:i] + char + current[i+1:]

                    if next_word in words_set:
                        words_set.remove(next_word)
                        queue.append((next_word,step+1))

        return 0

