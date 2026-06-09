class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def fits(cells):
            n = len(word)
            # Check forward
            if len(cells) == n:
                if all(c == ' ' or c == word[i] for i, c in enumerate(cells)):
                    return True
                # Check backward
                if all(c == ' ' or c == word[n-1-i] for i, c in enumerate(cells)):
                    return True
            return False
        
        # Check all horizontal slots
        for r in range(rows):
            slot = []
            for c in range(cols):
                if board[r][c] != '#':
                    slot.append(board[r][c])
                else:
                    if fits(slot):
                        return True
                    slot = []
            if fits(slot):
                return True
        
        # Check all vertical slots
        for c in range(cols):
            slot = []
            for r in range(rows):
                if board[r][c] != '#':
                    slot.append(board[r][c])
                else:
                    if fits(slot):
                        return True
                    slot = []
            if fits(slot):
                return True
        
        return False