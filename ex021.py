"""
Faça um programa em Python que abra e reproduza o audio de um arquivo mp3
"""
import pygame.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input("music.mp3")