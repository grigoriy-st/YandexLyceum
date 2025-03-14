import pygame

pygame.init()
size = width, height = 501, 501
screen = pygame.display.set_mode(size)
coords = [(2, -1), (3,5, 0,5), 
              (4, -1), (5, 0), (4, 2), 
              (2, 1), (2, 3), (4, 5), 
              (4, 6), (2, 5), (1, 7), 
              (1, 8), (0, 7), (0, 9), 
              (-1, 7), (-2, 8), (-2, 7), 
              (-3, 7), (-2, 6), (-4, 6), 
              (-3, 5), (-4, 5), (-3, 4), 
              (-5, 4), (-4, 3), (-5, 3), 
              (-4, 2), (-6, 2), (-5, 1), 
              (-6, 1), (-5, 0), (-6, 0), 
              (-5, -1), (-6, -2), (-4, -2), 
              (-5, -3), (-3, -4), (-4, -5), 
              (-2, -5), (-1, -6), (3, -6), 
              (3, -5), (1, -5), (1, -4), 
              (2, -3), (2, -1)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.BUTTON_WHEELUP:
            for i in range(coords):
                coords[i] = coords[i][0] + 1, coords[i][1] + 1
    

    pygame.draw.polygon(screen, "white", tuple(coords))
    pygame.display.flip()
