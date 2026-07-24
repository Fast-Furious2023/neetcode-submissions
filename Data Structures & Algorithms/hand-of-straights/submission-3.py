from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #number of groups = len(hand) / groupSize
        #sort hand, start from smallest -> group_1, 
        #keep iterating, if consecutive for group 1, add to g_1, until reaching size
        #then add to group 2...

        n = len(hand)
        if n % groupSize == 0:
            n_groups = n//groupSize
        else:
            return False
        

        # res = [[] for _ in range(n_groups)]

        # hand.sort()
        # res[0].append(hand[0])

        # for v in hand[1:]:
        #     for i in range(n_groups):
        #         if not res[i]:
        #             res[i].append(v)
        #             break
        #         elif len(res[i]) < groupSize and v == res[i][-1] + 1:
        #             res[i].append(v)
        #             break
        
        # for i in range(n_groups):
        #     if len(res[i]) != groupSize:
        #         return False
        # return True


        #for the smallest card, build its group of groupSize by deducting the cards_count, if count <= 0, then False

        cards_count = Counter(hand)

        #distinct cards:
        cards = sorted(cards_count.keys())

        for card in cards:
            count = cards_count[card]

            if count == 0:
                continue


            for i in range(1,groupSize):
                if cards_count[card+i] < count:
                    return False
                cards_count[card+i] -= count
        
        return True




