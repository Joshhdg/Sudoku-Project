import pygame
from sudoku_generator import *

def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((630, 630))
        pygame.display.set_caption("sudoku game name here")
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("white")
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

if __name__ == '__main__':
    main()