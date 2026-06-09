class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # P A Y P A L I S H I R I N G
        # 0 1 2 3 4 5 6 7 8 9 0 1 2 3

        if numRows == 1:
            return s

        arr = [""] * numRows # = ["PA" , "AP" , "Y"]

        # numRows = 3
        row = 0 # 0 1 2 3 2 1 0 1
        count = 0 # 0 1 2 3 4 
        bounce = False # True ,

        while count != len(s):
            # falling Down
            if row < numRows and bounce == False:
                arr[row] += s[count]
                row += 1
                if row == numRows:
                    bounce = True
                    row -= 1

            # bunce
            elif row > 0 and bounce == True:
                row -= 1
                arr[row] += s[count]
                if row == 0:
                    bounce = False
                    row += 1

            count += 1

        result = ""
        for i in arr:
            result += i
        
        return result
        