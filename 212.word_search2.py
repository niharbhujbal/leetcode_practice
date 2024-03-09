import collections


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        word_hm = collections.defaultdict(list)
        for i, word in enumerate(words):
            word_hm[word[0]].append(i)

        def get_neighbours(x, y, traveled_set):
            neighbours = []
            if y - 1 >= 0 and (x, y - 1) not in traveled_set:
                neighbours.append((x, y - 1))
            if x - 1 >= 0 and (x - 1, y) not in traveled_set:
                neighbours.append((x - 1, y))
            if y + 1 < len(board[0]) and (x, y + 1) not in traveled_set:
                neighbours.append((x, y + 1))
            if x + 1 < len(board) and (x + 1, y) not in traveled_set:
                neighbours.append((x + 1, y))
            return neighbours

        def find_the_word(x, y, traveled_set, word, pointer):

            if pointer == len(word) - 1 and board[x][y] == word[pointer]:
                return True

            if board[x][y] == word[pointer]:
                traveled_set.add((x, y))
                neg = []
                for xn, yn in get_neighbours(x, y, traveled_set):
                    set_copy = traveled_set.copy()
                    neg.append(find_the_word(xn, yn, set_copy, word, pointer + 1))

                return sum(neg)
            return False

        res = set()
        for x, row in enumerate(board):
            for y, val in enumerate(row):
                if board[x][y] in word_hm:
                    for i in word_hm[board[x][y]]:
                        if find_the_word(x, y, set(), words[i], 0):
                            res.add(words[i])

        return res
