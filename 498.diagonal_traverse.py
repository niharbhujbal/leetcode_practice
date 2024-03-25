class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        ans = []

        def get_diag(r, c, res, reversal):
            if r >= len(mat) or c >= len(mat[0]) or r < 0 or c < 0:
                if reversal:
                    res = res[::-1]
                ans.extend(res)
                return
            else:
                res += [mat[r][c]]
                get_diag(r - 1, c + 1, list(res), reversal)

        # vertical loop
        reversal = False
        for r in range(len(mat)):
            get_diag(r, 0, [], reversal)
            reversal = not reversal

        # horizontal
        for c in range(1, len(mat[0])):
            get_diag(len(mat) - 1, c, [], reversal)
            reversal = not reversal

        return ans


# just traversal diagonally and keep reversing the direction and adding it to answer
