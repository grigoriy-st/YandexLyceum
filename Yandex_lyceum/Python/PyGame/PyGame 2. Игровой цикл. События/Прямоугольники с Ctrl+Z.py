import pygame

def main():
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    
    running = True
    drawing = False
    start_pos = None
    rectangles = []  

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    drawing = True
                    start_pos = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:  
                    end_pos = event.pos
                    rectangles.append((start_pos, end_pos))
                    drawing = False
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    end_pos = event.pos
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_CTRL:  
                    if rectangles:
                        rectangles.pop()  

        
        screen.fill("black")  
        for rect in rectangles:
            (x1, y1), (x2, y2) = rect
            pygame.draw.rect(screen, "white", (min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1)), 5)

        if drawing and start_pos is not None:
            end_pos = pygame.mouse.get_pos()
            pygame.draw.rect(screen, "white", (min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]),
                                                    abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1])), 5)

        pygame.display.flip()  

    pygame.quit()

if __name__ == '__main__':
    main()