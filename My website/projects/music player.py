import pygame
import os

pygame.init()
pygame.mixer.init()

# set up the screen
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Music Player")

# set up the font
font = pygame.font.SysFont("Arial", 20)

# set up the music
pygame.mixer.music.load("D:\project\&01ATIF ASLAM Songs 2020 - Best Of Atif Aslam 2020 - Latest Bollywood Romantic Songs Hindi Song (320  kbps).mp3")

# set up the play button
play_button = pygame.Rect(50, 100, 50, 50)

# set up the pause button
pause_button = pygame.Rect(150, 100, 50, 50)

# set up the stop button
stop_button = pygame.Rect(250, 100, 50, 50)

# set up the loop variable
running = True

# play the music
pygame.mixer.music.play()

# loop to keep the window open
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # handle button clicks
            if play_button.collidepoint(event.pos):
                pygame.mixer.music.unpause()
            elif pause_button.collidepoint(event.pos):
                pygame.mixer.music.pause()
            elif stop_button.collidepoint(event.pos):
                pygame.mixer.music.stop()

    # draw the buttons
    pygame.draw.rect(screen, (255, 0, 0), play_button)
    pygame.draw.rect(screen, (0, 255, 0), pause_button)
    pygame.draw.rect(screen, (0, 0, 255), stop_button)

    # draw the button labels
    play_text = font.render("Play", True, (255, 255, 255))
    pause_text = font.render("Pause", True, (255, 255, 255))
    stop_text = font.render("Stop", True, (255, 255, 255))
    screen.blit(play_text, (play_button.x + 10, play_button.y + 15))
    screen.blit(pause_text, (pause_button.x + 5, pause_button.y + 15))
    screen.blit(stop_text, (stop_button.x + 5, stop_button.y + 15))

    # update the screen
    pygame.display.update()

# quit pygame
pygame.quit()
