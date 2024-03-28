from collections import Counter, defaultdict


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        c = dict(Counter(s))
        c = [(k, v) for k, v in c.items()]
        c.sort(key=lambda x: x[1], reverse=True)
        no_of_press = defaultdict(list)
        total_press = 0
        press = 1
        for k, v in c:
            if len(no_of_press[press]) == 9:
                press += 1

            no_of_press[press].append(k)
            total_press += v * press

        return total_press


# count the no of charater occurance
# then sort them in descending order
# one key press can have 9 letter
# so from the left to right and the count and that letter to a dict
# when 1 is full move to two and so on at the end return the total
