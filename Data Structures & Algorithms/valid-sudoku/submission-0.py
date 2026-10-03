class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # board is valid if there are no duplicates in one row, column, or subboxes
        # can use a hashset for each row and column

        cols = collections.defaultdict(set) #hashmap?
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                # check for duplicates
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True


        