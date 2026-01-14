class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def find_word(r,c,index_,traveled):
            nonlocal word
            # word is not present
            if board[r][c] != word[index_]:
                return False
            if board[r][c] == word[index_] and index_ == len(word) - 1 :
                return True
            
            traveled.add((r,c))
            for ri, ci in [(0,-1),(0,1),(-1,0),(1,0)]:
                if 0 <= r + ri < m and 0 <= c + ci < n and (r + ri,c + ci) not in traveled:
                    if find_word(r + ri,c + ci,index_+1,traveled):
                        return True
            traveled.remove((r, c)) 
            return False


        for r in range(m):
            for c in range(n):
                if find_word(r,c,0,set()):
                    return True
        return False