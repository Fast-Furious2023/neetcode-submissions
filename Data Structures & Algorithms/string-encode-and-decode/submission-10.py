class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])
            sub_s = s[j+1: j+1+length]
            res.append(sub_s)
            i = j + 1 + length
        return res

