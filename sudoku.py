import pygame
from sudoku_generator import *

pygame.init()
screen = pygame.display.set_mode((630, 630))
pygame.display.set_caption("Sudoku")
clock = pygame.time.Clock()

game_font = pygame.font.Font(None, 20)
title_font = pygame.font.Font(None, 50)
subtitle_font = pygame.font.Font(None, 40)

title_screen = True
difficulty = None
game_over = False
winner = 0

def draw_title_screen():    # still have to add text for each button
    screen.fill("light blue")
    title_text = "Welcome to Sudoku!"
    title_surf = title_font.render(title_text, 1, "black")
    title_rect = title_surf.get_rect(center=(630 // 2, 100))
    screen.blit(title_surf, title_rect)
    subtitle_text = "Select Your Difficulty:"
    subtitle_surf = subtitle_font.render(subtitle_text, 1, "black")
    subtitle_rect = subtitle_surf.get_rect(center = (630//2, 400))
    screen.blit(subtitle_surf, subtitle_rect)
    pygame.draw.rect(screen, "forest green", pygame.Rect(90,450,100,40))
    pygame.draw.rect(screen, "forest green", pygame.Rect(270,450,100,40))
    pygame.draw.rect(screen, "forest green", pygame.Rect(450,450,100,40))
    difficulty_text = "Easy"
    difficulty_surf = game_font.render(difficulty_text, 1, "black")
    difficulty_rect = difficulty_surf.get_rect(center=(90 + 50, 450 + 20))
    screen.blit(difficulty_surf, difficulty_rect)
    difficulty_text = "Medium"
    difficulty_surf = game_font.render(difficulty_text, 1, "black")
    difficulty_rect = difficulty_surf.get_rect(center=(270 + 50, 450 + 20))
    screen.blit(difficulty_surf, difficulty_rect)
    difficulty_text = "Hard"
    difficulty_surf = game_font.render(difficulty_text, 1, "black")
    difficulty_rect = difficulty_surf.get_rect(center=(450 + 50, 450 + 20))
    screen.blit(difficulty_surf, difficulty_rect)
    img = pygame.image.load("./images/sudoku.jpg").convert()
    img = pygame.transform.scale(img, (200, 200))
    screen.blit(img, (225, 150))

def draw_game_over():   # work in progress
    screen.fill("white")
    if winner != 0:
        title_text = "Game Won!"
    else:
        title_text = "Game Over :("
    title_surf = title_font.render(title_text, 1, (255, 255, 255))
    title_rect = title_surf.get_rect(center=(630//2, 200))
    screen.blit(title_surf, title_rect)

screen.fill("white")


def draw_board():
    screen.fill("light blue")
    for i in range(1, 9):
        pygame.draw.line(
            screen,
            "aquamarine4",
            (0, i * (630 / 9)),
            (630, i * (630/9)),
            2
        )
        pygame.draw.line(
            screen,
            "aquamarine4",
            (i * (630 / 9), 0),
            (i * (630 / 9), 630),
            2
        )
        for i in range(1, 9):
            if i % 3 == 0:
                pygame.draw.line(screen,
                "deepskyblue4",
                (0, i * (630 / 9)),
                (630, i * (630/9)),
                5)
            if i % 3 == 0:
                pygame.draw.line(
                    screen,
                    "deepskyblue4",
                    (i * (630 / 9), 0),
                    (i * (630 / 9), 630),
                    5
                )




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and title_screen:
            x, y = event.pos
            if 450 < y < 490:
                if 90 < x < 190:
                    print("easy")
                    difficulty = "easy"
                    title_screen = False
                if 270 < x < 370:
                    print("med")
                    difficulty = "medium"
                    title_screen = False
                if 450 < x < 550:
                    print("hard")
                    difficulty = "hard"
                    title_screen = False

        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            game_over = False
        if event.type == pygame.MOUSEBUTTONDOWN and not title_screen and not game_over:
            x, y = event.pos
            col, row = x//70, y//70
    if title_screen:
        draw_title_screen()
    else:
        draw_board()
    if game_over:
        draw_game_over()
    pygame.display.flip()
    clock.tick(60)