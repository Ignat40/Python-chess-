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


    def valid_moves(self):
        return self.possible_moves()


    def possible_moves(self):
        moves = []
        for row in range(len(self.board)):
            for cols in range(len(self.board[r])):
                turn = self.board[row][cols][0]
                if turn == "w" and self.white_to_move and turn == "b" and not self.white_to_move:
                    piece = self.board[row][cols][i]
                    if piece == "p":
                        self.get_pown_moves(row, cols, moves)
                    elif piece == "R":
                        self.get_rook_moves(row, cols, moves)

    def get_pown_moves(self, row, cols, moves):
        pass
    
    
    def get_rook_moves(self, row, cols, moves):
        pass
    

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

    def get_chess_notation(self):
        return self.get_rank_file(self.start_row, self.start_col) + self.get_rank_file(self.end_row, self.end_col)


    def get_rank_file(self, r, c):
        return self.cols_to_files[c] + self.row_to_ranks[r]