class Solution:
    def isValidSudoku(self, nums: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        square = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if nums[i][j] == ".":
                    continue
                if nums[i][j] in rows[i] or nums[i][j] in cols[j] or nums[i][j] in square[(i//3)*3 + (j//3)]:
                    return False
                rows[i].add(nums[i][j])
                cols[j].add(nums[i][j])
                square[(i//3)*3 + (j//3)].add(nums[i][j])
        return True
        