import pygame
from lib20202.grafica import *

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    centro=[600,350]
    Plano(pantalla,centro)
    ls = [[600,345],[595,350],[605,350]]
    #pygame.draw.circle(pantalla,ROJO,ls[0],1)
    #pygame.draw.circle(pantalla,ROJO,ls[1],1)
    #pygame.draw.circle(pantalla,ROJO,ls[2],1)
    #pygame.draw.polygon(pantalla,VERDE,ls,1)
    #pygame.display.update()
    def trasladarPuntos():
        ls[0] = [ls[0][0],ls[0][1]-5]
        ls[1] = [ls[1][0]-5,ls[1][1]+5]
        ls[2] = [ls[2][0]+5,ls[2][1]+5]
    
    fin=False
    reloj = pygame.time.Clock()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
        pygame.draw.polygon(pantalla,BLANCO,ls,3)
        trasladarPuntos()
        pygame.display.update()
        pantalla.fill(NEGRO)
        reloj.tick(30)

        