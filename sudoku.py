import pygame
from sudoku_generator import *

pygame.init()
screen = pygame.display.set_mode((630, 630))
pygame.display.set_caption("sudoku game name here")
clock = pygame.time.Clock()

game_font = pygame.font.Font(None, 20)
title_font = pygame.font.Font(None, 50)
subtitle_font = pygame.font.Font(None, 40)

title_screen = True
difficulty = None
game_over = False
winner = 0

def draw_title_screen():    # still have to add text for each button
    screen.fill("white")
    title_text = "Welcome to Sudoku game name here!"
    title_surf = title_font.render(title_text, 1, "black")
    title_rect = title_surf.get_rect(center=(630 // 2, 100))
    screen.blit(title_surf, title_rect)
    subtitle_text = "Select Your Difficulty:"
    subtitle_surf = subtitle_font.render(subtitle_text, 1, "black")
    subtitle_rect = subtitle_surf.get_rect(center = (630//2, 400))
    screen.blit(subtitle_surf, subtitle_rect)
    pygame.draw.rect(screen, "orange", pygame.Rect(90,450,100,40))
    pygame.draw.rect(screen, "orange", pygame.Rect(270,450,100,40))
    pygame.draw.rect(screen, "orange", pygame.Rect(450,450,100,40))

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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and title_screen:
            x, y = event.pos()
        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            game_over = False
        if event.type == pygame.MOUSEBUTTONDOWN and not title_screen and not game_over:
            x, y = event.pos()
            col, row = x//70, y//70
    if title_screen:
        draw_title_screen()
    if game_over:
        draw_game_over()
    pygame.display.flip()
    clock.tick(60)