class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        sub = {}
        s = 0
        
        col = {} #(num,index): row
        for i,x in enumerate(board):
            
            if i == 3 or i == 6:
                sub = {}
            s = 0
            row = {} #num: index
            for j,y in enumerate(board[i]):
                
                if j == 3 or j == 6:
                    s+=1
                    
                if (y,s) in sub and y != '.': return False
                else:
                    sub[(y,s)] = j
                                 
                if y in row and y != '.': return False
                else:
                    row[y] = j
                              
                if (y,j) in col and y != '.': return False
                else:
                    col[(y,j)] = i

        return True
        