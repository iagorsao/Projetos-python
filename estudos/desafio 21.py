import pygame
pygame.init()
pygame.mixer.music.load('ex021.wav')
pygame.mixer.music.play()
input()
pygame.event.wait()