from collections import Counter
from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count_letters = Counter(s)
        l, r = 0, 0
        count = defaultdict(int)
        res = []
        letters_per_word = 0

        while r < len(s):
            curr = s[r]
            count[curr] += 1
            r += 1
            if count[curr] == count_letters[curr]:
                letters_per_word += count.pop(curr)
            if not count:
                l = r
                res.append(letters_per_word)
                letters_per_word = 0

        return res

            


        