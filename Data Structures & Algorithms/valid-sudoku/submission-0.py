class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if not num.isdigit(): continue
                if num in rows[r]: return False
                if num in cols[c]: return False
                box_index = (r//3)*3 + c//3
                if num in boxes[box_index]: return False
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)

        return True