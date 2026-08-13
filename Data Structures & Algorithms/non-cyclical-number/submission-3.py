class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_squares_digits(num):
            digits = str(num)
            total = 0
            for digit in digits:
                total += int(digit)**2
            return total

        # use a set to detect duplicate
        lookup = set()
        curr = n
        while curr != 1 and curr not in lookup:
            lookup.add(curr)
            curr = sum_squares_digits(curr)
         
        return curr == 1


        