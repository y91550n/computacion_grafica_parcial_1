import pygame
from lib20202.grafica import *

ls = [[600,345],[595,350],[605,350]]
ls2 = [[[600,345],[595,350],[605,350]]]

def PintarTriangulos():
    a = 0
    for e in ls2:
        print('Mostrando la lista: ',ls2)
        valor = ls2[a]
        pygame.draw.polygon(pantalla,BLANCO,valor,2)
        a+=1
    pygame.display.update()
    print('Termino lista')

def CrearTriangulos():
        ls[0] = [ls2[i][0][0],ls2[i][0][1]-10]
        ls[1] = [ls2[i][1][0]-10,ls2[i][1][1]+10]
        ls[2] = [ls2[i][2][0]+10,ls2[i][2][1]+10]
        ls2.append(ls)
        
if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    centro=[600,350]
    Plano(pantalla,centro)
    i = 0
    fin=False
    reloj = pygame.time.Clock()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
        PintarTriangulos()
        CrearTriangulos()
        i+=1
        print('Hasta aqui vamos.')