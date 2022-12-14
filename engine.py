class chess_board():
    def __init__(self):
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp", "bp","bp","bp","bp","bp","bp","bp"],
            ["--", "--","--","--","--","--","--","--",],
            ["--", "--","--","--","--","--","--","--",],
            ["--", "--","--","--","--","--","--","--",],
            ["--", "--","--","--","--","--","--","--",],
            ["wp", "wp","wp","wp","wp","wp","wp","wp",],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
        ]

        self.move_functions = {'p' : self.get_pown_moves, 'R' : self.get_rook_moves,'N' : self.get_knight_moves,
                                'B' : self.get_bishop_moves,'Q' : self.get_queen_moves,'K' : self.get_king_moves}

        self.white_to_move = True
        self.move_log = []  
      
    def make_move(self,move):
        self.board[move.start_row][move.start_col] = "--"
        self.board[move.end_row][move.end_col] = move.moved_pieces 
        self.move_log.append(move) 
        self.white_to_move = not self.white_to_move

    def undo_move(self):
        if len(self.move_log) != 0: # makes sure that there is a move to be undone 
            move = self.move_log.pop()
            self.board[move.start_row][move.start_col] = move.moved_pieces
            self.board[move.end_row][move.end_col] = move.captured_pieces
            self.white_to_move = not self.white_to_move # switches turns 


    def all_valid_moves(self):
        return self.possible_moves()


    def possible_moves(self):
        moves = []
        for row in range(len(self.board)):
            for cols in range(len(self.board[row])):
                turn = self.board[row][cols][0]
                if (turn == 'w' and self.white_to_move) or (turn == 'b' and not self.white_to_move):
                    piece = self.board[row][cols][1]
                    self.move_functions[piece](row, cols, moves)
        return moves 

    def get_pown_moves(self, row, cols, moves):
        if self.white_to_move:
            if self.board[row - 1][cols] == "--":
                moves.append(Move((row, cols), (row - 1, cols), self.board))
                if row == 6 and self.board[row - 2][cols] == "--":
                    moves.append(Move((row, cols), (row - 2, cols), self.board))
            if cols - 1 >= 0:
                if self.board[row - 1][cols - 1][0] == 'b':
                    moves.append(Move((row, cols), (row - 1, cols - 1), self.board))
            if cols + 1 <= 7:
                if self.board[row - 1][cols + 1][0] == "b":
                    moves.append(Move((row, cols), (row - 1, cols + 1), self.board)) 

        else:
            if self.board[row + 1][cols] == "--":
                moves.append(Move((row, cols), (row + 1, cols), self.board))
                if row == 1 and self.board[row + 2][cols] == "--":
                    moves.append(Move((row, cols), (row + 2, cols), self.board))
            if cols - 1 >= 0:
                if self.board[row + 1][cols - 1][0] == 'w':
                    moves.append(Move((row, cols), (row + 1, cols - 1), self.board))
            if cols + 1 <= 7:
                if self.board[row + 1][cols + 1][0] == "w":
                    moves.append(Move((row, cols), (row + 1, cols + 1), self.board))

    
    def get_rook_moves(self, row, cols, moves):
        directions = ((-1, 0), (0, -1), (1,0), (0, 1))
        opposite_color = "b" if self.white_to_move else "w"
        for d in directions:
            for i in range(1,8):
                end_row = row + d[0] * i 
                end_col = cols + d[1] * i
                if 0 <= end_row < 8 and 0 <= end_col < 8:
                    end_piece = self.board[end_row][end_col]
                    if end_piece == "--":
                        moves.append(Move((row, cols), (end_row, end_col), self.board))
                    elif end_piece[0] == opposite_color:
                        moves.append(Move((row, cols), (end_row, end_col), self.board))
                        break
                    else:
                        break
                else:
                    break
                

                

    def get_knight_moves(self, row, cols, moves):
        knight_moves = ((-2, -1), (-2, -1), (-1, -2), (-1, -2), (1, 2), (2, -1), (2, 1))
        op_color = "w" if self.white_to_move else "b"
        for k in knight_moves:
            end_row = row + k[0]
            end_col = cols + k[1]
            if 0 <= end_row < 8 and 0 <= end_col < 8:
                end_piece = self.board[end_row][end_col]
                if end_piece[0] != op_color:
                    moves.append(Move((row, cols), (end_row, end_col), self.board))




    def get_bishop_moves(self, row, cols, moves):
        directions = ((-1, -1), (-1, 1), (1,-1), (1, 1))
        opposite_color = "b" if self.white_to_move else "w"
        for d in directions:
            for i in range(1, 8):
                end_row = row + d[0] * i 
                end_col = cols + d[1] * i
                if 0 <= end_row < 8 and 0 <= end_col < 8:
                    end_piece = self.board[end_row][end_col]
                    if end_piece == "--":
                        moves.append(Move((row, cols), (end_row, end_col), self.board))
                    elif end_piece[0] == opposite_color:
                        moves.append(Move((row, cols), (end_row, end_col), self.board))
                        break
                else:
                    break
            else:
                break
                


    def get_queen_moves(self, row, cols, moves): #easy :)))
        self.get_bishop_moves(row, cols, moves)
        self.get_rook_moves(row, cols, moves)

    def get_king_moves(self, row, cols, moves):
        king_moves = ((-1, -1), (-1, -0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        op_color = "w" if self.white_to_move else "b"
        for i in range(8):
            end_row = row + king_moves[i][0]
            end_col = cols + king_moves[i][1]
            if 0 <= end_row < 8 and 0 <= end_col < 8:
                end_piece = self.board[end_row][end_col]
                if end_piece[0] != op_color:
                    moves.append(Move((row, cols), (end_row, end_col), self.board))    

class Move():

    ranks_to_rows = {"1" : 7, "2" : 6, "3" : 5, "4" : 4, 
                    "5" : 3, "6" : 2, "7" : 1, "8" : 0}
    row_to_ranks = {v: k for k, v in ranks_to_rows.items()}

    files_to_cols = {"a" :0 , "b" : 1, "c" : 2, "d" : 3,
                    "e" : 4, "f" : 5, "g" : 6, "h" : 7}
    cols_to_files = {v: k for k, v in files_to_cols.items()}
    

    def __init__(self, starting_square, ending_square, board):
        self.start_row = starting_square[0]
        self.start_col = starting_square[1]
        self.end_row = ending_square[0]
        self.end_col = ending_square[1]
        self.moved_pieces = board[self.start_row][self.start_col]
        self.captured_pieces = board[self.end_row][self.end_col]
        self.move_ID = self.start_row * 1000 + self.start_col * 100 + self.end_row * 10 + self.end_col
        print(self.move_ID)

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.move_ID == other.move_ID
        return False


    def get_chess_notation(self):
        return self.get_rank_file(self.start_row, self.start_col) + self.get_rank_file(self.end_row, self.end_col)


    def get_rank_file(self, r, c):
        return self.cols_to_files[c] + self.row_to_ranks[r]