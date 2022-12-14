import pygame as p
import engine 


width = height = 400 #or 512
board_size = 8
cell_size = height // board_size
fps = 15
images = {}

def draw_image():
    figures = ["bR","bB","bQ","bK", "bN","bp",
    "wR","wB","wQ","wK","wN","wp"]
    for figure in figures:
        images[figure] = p.transform.scale(p.image.load("figures/" + figure + ".png"), (cell_size, cell_size))

def main():
    p.init()
    screen = p.display.set_mode((width, height))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    cb = engine.chess_board() 
    valid_moves = cb.all_valid_moves()
    move_made = False 
    draw_image()
    running = True
    selected_squere = ()
    player_clicks = []
    while running:
        for i in p.event.get():
            if i.type == p.QUIT:
                running = False

            elif i.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0]//cell_size
                row = location[1]//cell_size
                if selected_squere == (row, col):
                    selected_squere = () # deselcts
                    player_clicks = [] # also clears players clicks 
                else:
                    selected_squere = (row, col)
                    player_clicks.append(selected_squere)
                if len(player_clicks) == 2:
                    move = engine.Move(player_clicks[0], player_clicks[1], cb.board)
                    print(move.get_chess_notation())
                    if move in valid_moves:
                        cb.make_move(move)
                        move_made = True
                    selected_squere = ()
                    player_clicks = []

            elif i.type == p.KEYDOWN:
                if i.key == p.K_z:
                    cb.undo_move()
                    move_made = True

        if move_made:
            valid_moves = cb.all_valid_moves()
            move_made = False


        draw_game(screen, cb)
        clock.tick(fps)
        p.display.flip()

def draw_game(screen, cb):
    draw_board(screen)
    draw_pieces(screen, cb.board)

def draw_board(screen): #keeping in mind that the top left square is always white

    colors = [p.Color("white"), p.Color("grey")]
    for rows in range(board_size):
        for cols in range(board_size):
            color = colors[((rows + cols) % 2)]
            p.draw.rect(screen, color, p.Rect(cols*cell_size, rows*cell_size, cell_size, cell_size))


def draw_pieces(screen, board):
    
    for rows in range(board_size):
        for cols in range(board_size):
            piece = board[rows][cols]
            if piece != "--":
                screen.blit(images[piece], p.Rect(cols*cell_size, rows*cell_size, cell_size, cell_size))



if __name__ == "__main__":
    main()
