from settings import *
import pygame
import sys


pygame.init()


screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Connect Four!!")
board = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]


def draw_board():
    for row in range(HEIGHT):
        for col in range(WIDTH):
            pygame.draw.rect(screen, (255, 255, 255), (col * CELL_SIZE, (row + 1) * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.circle(screen, (0, 0, 0), (col * CELL_SIZE + CELL_SIZE // 2, (row + 1) * CELL_SIZE + CELL_SIZE // 2), RADIUS)

            if board[row][col] == "X":
                pygame.draw.circle(screen, PLAYER1_COLOR, (col * CELL_SIZE + CELL_SIZE // 2, (row + 1) * CELL_SIZE + CELL_SIZE // 2), RADIUS)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, PLAYER2_COLOR, (col * CELL_SIZE + CELL_SIZE // 2, (row + 1) * CELL_SIZE + CELL_SIZE // 2), RADIUS)

    pygame.display.flip()


def drop_disc(col, player):
    for row in range(HEIGHT - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = player
            return True
    return False


def check_winner(player):
    # Check horizontally
    for row in range(HEIGHT):
        for col in range(WIDTH - 3):
            if board[row][col] == player and board[row][col + 1] == player and board[row][col + 2] == player and board[row][col + 3] == player:
                return True

    # Check vertically
    for row in range(HEIGHT - 3):
        for col in range(WIDTH):
            if board[row][col] == player and board[row + 1][col] == player and board[row + 2][col] == player and board[row + 3][col] == player:
                return True

    # Check diagonally (from bottom-left to top-right)
    for row in range(3, HEIGHT):
        for col in range(WIDTH - 3):
            if board[row][col] == player and board[row - 1][col + 1] == player and board[row - 2][col + 2] == player and board[row - 3][col + 3] == player:
                return True

    # Check diagonally (from top-left to bottom-right)
    for row in range(3, HEIGHT):
        for col in range(3, WIDTH):
            if board[row][col] == player and board[row - 1][col - 1] == player and board[row - 2][col - 2] == player and board[row - 3][col - 3] == player:
                return True

    return False


def is_board_full():
    return all(cell != ' ' for row in board for cell in row)

def main():
    current_player = "X"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                col = event.pos[0] // CELL_SIZE
                if drop_disc(col, current_player):
                    draw_board()
                    if check_winner(current_player):
                        print(f"Player {current_player} wins!")
                        pygame.quit()
                        sys.exit()
                    elif is_board_full():
                        print("It's a draw!")
                        pygame.quit()
                        sys.exit()
                    else:
                        current_player = 'O' if current_player == 'X'  else 'X'



if __name__ == "__main__":
    draw_board()
    main()
