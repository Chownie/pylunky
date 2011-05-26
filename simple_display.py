import pygame
import os
import sys
from readmap import *
import time
textures = {}

pygame.init()
window = pygame.display.set_mode((320,320))
pygame.display.set_caption('PyLunky!')
screen = pygame.display.get_surface()
clock = pygame.time.Clock()


def main():
    mapfile = open('./1.map','r').read()
    mapinfo = rMap(mapfile)
    while True:
        for i in mapinfo:
            for k in i:
                tile = pygame.image.load("./resources/"+k.mat)
                screen.blit(tile, (k.posx*32,k.posy*32))
        pygame.display.flip()
        clock.tick(60)
main()
