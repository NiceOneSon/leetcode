class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        prevrow = self.getRow(rowIndex-1)
        row = [1]
        for prev, next in zip(prevrow[:-1], prevrow[1:]):
            row.append(prev + next)
        row.append(1)
        return row
            