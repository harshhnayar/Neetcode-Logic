class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = defaultdict(set)
        rows = defaultdict(set)
        cols = defaultdict(set)

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue

                result = (r // 3, c // 3)

                if( value in rows[r] 
                or value in cols[c] or 
                value in res[result] ) : return False

                rows[r].add(value)
                cols[c].add(value)
                res[result].add(value)
        return True         

