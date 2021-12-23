import pygame
pygame.init()
pygame.mixer.music.load("filename="music.mp3")
pygame.mixer.music.play()
pygame.event.wait()